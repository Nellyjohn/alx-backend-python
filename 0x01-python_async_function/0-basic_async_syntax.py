#!/usr/bin/env python3
"""This module represents an asynchronous coroutine that takes in an integer...
...argument and waits for a random delay and eventually returns it."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Function Docs"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
