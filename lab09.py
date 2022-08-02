import math
import asyncio
import httpx


def create_batches(li: list, batch_size: int) -> list:
    amount_batches = math.ceil(len(li) / batch_size)
    return [li[i::amount_batches] for i in range(amount_batches)]


async def get_response(client, url):
    r = await client.get(url)
    return r


async def main():
    async with httpx.AsyncClient() as client:
        urls = ['https://httpbin.org/delay/1' for _ in range(20)]
        batches = create_batches(urls, batch_size=5)

        from pprint import pprint
        pprint(batches)

        for batch in batches:
            print(batch)  
            tasks = []
            for url in batch:
                tasks.append(asyncio.create_task(get_response(client, url)))
            print(await asyncio.gather(*tasks))


asyncio.run(main())