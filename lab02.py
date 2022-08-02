import asyncio


async def one():
    print('one')


async def two():
    print('two')


async def three():
    print('three')


async def main():
    asyncio.gather(one(), two(), three())


asyncio.run(main())