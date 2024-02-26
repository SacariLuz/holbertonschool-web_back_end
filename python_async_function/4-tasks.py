#!/usr/bin/env python3
"""
Tasks 
"""
import asyncio
from typing import List


task_wait_random = __import__("3-tasks").wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Define a function and it takes an int argument
    max_delay
    """
    task = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*task))
