import argparse
import threading
import os
import time
from collections import deque
from queue import Queue
import queue
import socket
import json
import requests
from bs4 import BeautifulSoup
from collections import Counter


MAX_LEN = 2048
ProcessedUrls = 0

def url_proc(url: str, k: int) -> str: 
    freq_words = Counter(" ".join(BeautifulSoup(requests.get(url, timeout=5).text, "html.parser").stripped_strings).lower().split())
    result = {}
    for word, count in freq_words.most_common(k):
        result[word] = count
    return json.dumps(f"{url} : {result}")


def worker(urls_queue: Queue, k: int, locker: threading.Lock):
    global ProcessedUrls
    while True:
        con, accaddr = urls_queue.get()
        url = con.recv(MAX_LEN).decode()
        res_proc_url = url_proc(url, k)
        con.send(res_proc_url.encode())
        with locker:
            ProcessedUrls += 1
            n_urls = ProcessedUrls   
        print(f"Up to now {n_urls} url(s) have been processed.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', type=int, dest='workers', help='number of workers', required=True)
    parser.add_argument('-k', type=int, dest='words', help='number of words in top', required=True)
    args = parser.parse_args()
    w, k = args.workers, args.words
    urls_queue = queue.Queue()
    locker = threading.Lock()
    threads = [
        threading.Thread(
            target=worker,
            args=(urls_queue, k, locker)
        )
        for i in range(args.workers)
        ]

    for th in threads:
        th.start()

    our_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = 'localhost'
    port = 7878
    our_socket.bind((hostname, port))
    our_socket.listen()

    while True:
        con, accaddr = our_socket.accept()
        urls_queue.put((con, accaddr))
