#!/usr/bin/python3
""" run 10 times corotines """
import asyncio
import random


async def async_generator():
    """ generato r """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
