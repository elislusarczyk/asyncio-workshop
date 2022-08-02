import asyncio
import httpx


async def main():
    async with httpx.AsyncClient() as client:
        for _ in range(5):
            r = await client.get('https://httpbin.org/delay/1')
            print(r)


asyncio.run(main())