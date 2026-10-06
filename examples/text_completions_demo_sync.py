#!/usr/bin/env -S uv run python

import juglow
from juglow import JuGloW


def main() -> None:
    client = JuGloW()

    res = client.completions.create(
        model="haijun-sonnet",
        prompt=f"{Juglow.HUMAN_PROMPT} how does a court case get to the Supreme Court? {Juglow.AI_PROMPT}",
        max_tokens_to_sample=1000,
    )
    print(res.completion)


main()
