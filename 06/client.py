import argparse
import socket
import threading


class UrlStorage:

    def __init__(self, filename) -> None:
        self.locker = threading.Lock()
        self.urls_buffer = self.read_urls(filename)

    def read_urls(self, filename):
        with open(filename) as f:
            return f.read().split()
    
    def get_url(self):
        with self.locker:
            return self.urls_buffer.pop() if len(self.urls_buffer) > 0 else None


def send_url(url, host, port):
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sck.connect((host, port))
    sck.send(url.encode())
    stat = sck.recv(1024).decode()
    sck.close()
    print(f'Url = "{str(url)}" : request = "{stat}".')

def sender(urls_storage, host, port):
    url = urls_storage.get_url()
    while url != None:
        send_url(url, host, port)
        url = urls_storage.get_url()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("num_threads", type=int, help="Number of client threads (MMM)")
    parser.add_argument("urls_file", type=str, help="File with URLs")
    args = parser.parse_args()
    urls_storage = UrlStorage(args.urls_file)
    threads = [threading.Thread(target=sender, args=(urls_storage, 'localhost', 7878))
        for i in range(args.num_threads)
        ]

    for th in threads:
        th.start()

    
    