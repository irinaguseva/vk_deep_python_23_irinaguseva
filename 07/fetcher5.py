import argparse
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_urls(urls, concurrent_requests):
    async with aiohttp.ClientSession() as session:
        tasks = []
        semaphore = asyncio.Semaphore(concurrent_requests)

        for url in urls:
            task = asyncio.ensure_future(fetch_url_with_semaphore(semaphore, session, url))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        return responses

async def fetch_url_with_semaphore(semaphore, session, url):
    async with semaphore:
        return await fetch_url(session, url)

def main():
    parser = argparse.ArgumentParser(description='Async URL Fetcher')
    parser.add_argument('-c', '--concurrency', type=int, default=10,
                        help='number of concurrent requests (default: 10)')
    parser.add_argument('filename', type=str,
                        help='name of the file containing URLs')

    args = parser.parse_args()

    with open(args.filename, 'r') as file:
        urls = [line.strip() for line in file]

    loop = asyncio.get_event_loop()
    responses = loop.run_until_complete(fetch_urls(urls, args.concurrency))

    for response in responses:
        print(response)

if __name__ == '__main__':
    main()