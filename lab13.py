from fastapi import FastAPI
import time
import asyncio

app = FastAPI()


async def square(number: int):
    return number ** 2


async def cube(number: int):
    return number ** 3


@app.get("/square/{num}")
async def root(num: int):
    return await asyncio.gather(*[square(i) for i in range(num)])


@app.get("/cube/{num}")
async def root(num: int):
    return await asyncio.gather(*[cube(i) for i in range(num)])

