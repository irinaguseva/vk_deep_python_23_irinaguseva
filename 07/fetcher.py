import argparse
import asyncio
import os
import re
from collections import Counter
import aiohttp
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup


nltk.download('stopwords', quiet=True)
stop_words_en = set(stopwords.words('english'))
stop_words_ru = set(stopwords.words('russian'))


def get_args():
    parser = argparse.ArgumentParser(
        description="Скрипт для асинхронной обкачки урлов (Fetcher)")
    parser.add_argument(
        "-c", "--conc_reqs", type=int, help="Количество асинхронных вызовов")
    parser.add_argument(
        "urls", type=str, help="Файл с url-ами")
    args = parser.parse_args()
    if args.conc_reqs <= 0:
        raise ValueError("Количество вызовов должно быть больше 0.")
    if not os.path.exists(args.urls):
        raise FileNotFoundError(
            "Файл не найден или был перемещен из текущего каталога.")
    return args.conc_reqs, args.urls


def open_urls_file(file_urls):
    with open(file_urls, "r") as file:
        urls_file = file.readlines()
    return [item.strip() for item in urls_file]


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
        for url, req in zip(urls, responses):
            page = BeautifulSoup(req, 'html.parser')
            page_txt = page.text
            tokens_obtained = re.findall(r'\b\w+\b', page_txt.lower())
            tokens_obtained = [token for token in tokens_obtained if token not
                               in stop_words_en and token not in stop_words_ru]
            freq_words = Counter(tokens_obtained)
            result = {}
            for word, count in freq_words.most_common(5):
                result[word] = count
            print(f"{url} : {result}")


if __name__ == "__main__":
    num_reqs, file_urls = get_args()
    urls_lst = open_urls_file(file_urls)
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(get_response(urls_lst, num_reqs))
