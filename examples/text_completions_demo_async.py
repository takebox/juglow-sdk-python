#!/usr/bin/env -S uv run python

import asyncio

import juglow
from juglow import AsyncJuGloW


async def main() -> None:
    client = AsyncJuGloW()

    res = await client.completions.create(
        model="haijun-sonnet",
        prompt=f"{Juglow.HUMAN_PROMPT} how does a court case get to the Supreme Court? {Juglow.AI_PROMPT}",
        max_tokens_to_sample=1000,
    )
    print(res.completion)


asyncio.run(main())
