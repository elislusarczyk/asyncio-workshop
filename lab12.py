import asyncio
import typing

from concurrent.futures import ThreadPoolExecutor


async def execute_in_thread(executor: ThreadPoolExecutor, func: typing.Callable, *args):
    """
    Provide an async/await wrapper to execute multiple non-async functions
    in parallel with the given Thread-Executor ( @param executor ).
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, func, *args)
