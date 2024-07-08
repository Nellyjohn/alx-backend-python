#!/usr/bin/env python3
"""This module represents an async routine that takes in 2 int arguments...
...and return the list of all the delays"""

import asyncio
import heapq
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function Doc"""
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        heapq.heappush(delays, delay)


    return [heapq.heappop(delays) for _ in range(len(delays))]
