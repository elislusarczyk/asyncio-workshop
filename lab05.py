import asyncio
import httpx


async def main():
    with httpx.Client() as client:
        for _ in range(5):
            r = client.get('https://httpbin.org/delay/1')
            print(r)


asyncio.run(main())