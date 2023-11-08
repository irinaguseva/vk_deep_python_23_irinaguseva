import aiohttp
import argparse
import asyncio
from bs4 import BeautifulSoup
from collections import Counter


def open_urls_file(file_urls):
    with open(file_urls, "r") as f:
        urls_file = f.readlines()
    return [item.strip() for item in urls_file]

def html_page_preprocess():
    pass

async def fetch_url(session, url, semaphore=None):
    if semaphore:
        async with semaphore:
            async with session.get(url) as response:
                return await response.text()
    else:
        async with session.get(url) as response:
            return await response.text()


async def get_response(urls, concurrent_requests):
    async with aiohttp.ClientSession() as session:
        tasks = []
        sema = asyncio.Semaphore(concurrent_requests)
        
        for url in urls:
            task = asyncio.ensure_future(fetch_url(session, url, sema))
            tasks.append(task)
        
        responses = await asyncio.gather(*tasks)
        
        for u, r in zip(urls, responses):
            page = BeautifulSoup(r, 'html.parser')
            page_txt = page.text 
            with open("txt_page.txt", "w", errors='ignore') as f:
                f.write(page_txt)
            freq_words = Counter(page_txt.lower().split())
            result = {}
            for word, count in freq_words.most_common(5):
                result[word] = count
            print(f"{u} : {result}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Скрипт для асинхронной обкачки урлов (Fetcher)")
    parser.add_argument("-c", "--conc_reqs", type=int, help="Количество асинхронных вызовов")
    parser.add_argument("urls", type=str, help="Файл с url-ами")
    args = parser.parse_args()

    num_reqs = args.conc_reqs

    if not isinstance(num_reqs, int):
        raise TypeError("Переменная num_reqs должна быть типа int!")
    
    file_urls = args.urls

    if not isinstance(file_urls, str):
        raise TypeError("Переменная urls должна быть типа str!")

    urls_lst = open_urls_file(file_urls)
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(get_response(urls_lst, num_reqs))