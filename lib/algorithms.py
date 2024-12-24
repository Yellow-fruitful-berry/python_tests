import pytest

@pytest.mark.asyncio
async def sum(a, b):
    return a+b


@pytest.mark.asyncio
async def multiply(a, b):
    return a*b