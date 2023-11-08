import asyncio
import aiohttp
import argparse

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main(concurrency, urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Async URL fetcher")
    parser.add_argument("concurrency", type=int, help="Number of concurrent requests")
    parser.add_argument("urls_file", type=argparse.FileType('r'), help="File containing list of URLs")

    args = parser.parse_args()
    concurrency = args.concurrency
    urls = [url.strip() for url in args.urls_file.readlines()]

    asyncio.run(main(concurrency, urls))