import asyncio


async def square(number: int):
    print(f'squere {number=}')
    return number ** 2


async def main():
    squares = [square(i) for i in range(10)]

    print(await asyncio.gather(*squares))


asyncio.run(main())