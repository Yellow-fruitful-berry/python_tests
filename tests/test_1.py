from lib.algorithms import sum, multiply

async def test_sum():
    assert await sum(1, 2) == 3


async def test_multiply():
    assert await multiply(1, 2) == 2
