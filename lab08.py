import asyncio
import httpx


async def get_response(client, url):
    r = await client.get(url)
    return r


async def main():
    async with httpx.AsyncClient(timeout=1) as client:
        tasks = []
        
        for page in range(1, 10):
            url = f'https://swapi.dev/api/people/?page={page}'
            tasks.append(asyncio.create_task(get_response(client, url)))

        print(await asyncio.gather(*tasks, loop=None, return_exceptions=True))


asyncio.run(main())