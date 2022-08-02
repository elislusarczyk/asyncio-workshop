import asyncio
import httpx


async def get_response(client, url):
    r = await client.get(url)
    return r


async def main():
    async with httpx.AsyncClient() as client:
        tasks = []
        for _ in range(5):
            url = 'https://httpbin.org/delay/1'
            tasks.append(asyncio.create_task(get_response(client, url)))

        print(await asyncio.gather(*tasks))


asyncio.run(main())