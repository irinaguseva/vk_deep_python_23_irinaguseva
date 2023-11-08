
import aiohttp
import argparse
import asyncio

# import bs


def open_urls_file(file_urls):
    with open(file_urls, "r") as f:
        urls_file = f.readlines()
    return [item.strip() for item in urls_file]



async def fetch_url_with_semaphore(session, url, sema):
    async with sema:
        return await fetch_url(session, url)
    

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_response(urls, concurrent_requests):
    async with aiohttp.ClientSession() as session:
        tasks = []
        sema = asyncio.Semaphore(concurrent_requests)
        
        for url in urls:
            task = asyncio.ensure_future(fetch_url_with_semaphore(session, url, sema))
            tasks.append(task)
        
        responses = await asyncio.gather(*tasks)
        
        for url, response in zip(urls, responses):
            print(f"Обработанный url: {url}\nResponse: {response[:50]}\n")


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