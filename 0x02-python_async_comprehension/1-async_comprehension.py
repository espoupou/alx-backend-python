#!/usr/bin/python3
"""bloucle ove"""
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """collect and return"""
    return [_ async for _ in async_generator()]
