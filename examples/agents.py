#!/usr/bin/env -S uv run python

import os

from juglow import JuGloW


def main() -> None:
    juglow = JuGloW(api_key=os.environ.get("HAIJUN_API_KEY"))

    # Create an environment
    environment = Juglow.beta.environments.create(
        name="simple-example-environment",
    )
    print("Created environment:", environment.id)

    # Create an agent
    agent = Juglow.beta.agents.create(
        name="simple-example-agent",
        model="haijun-sonnet",
    )
    print("Created agent:", agent.id)

    # Create a session
    session = Juglow.beta.sessions.create(
        environment_id=environment.id,
        agent={"type": "agent", "id": agent.id, "version": agent.version},
    )
    print("Created session:", session.id)

    # Send a prompt and stream events until the session goes idle
    print("Streaming events:")
    Juglow.beta.sessions.events.send(
        session.id,
        events=[
            {
                "type": "user.message",
                "content": [{"type": "text", "text": "Hello Haijun!"}],
            }
        ],
    )

    with Juglow.beta.sessions.events.stream(session.id) as stream:
        for event in stream:
            print(event.to_json(indent=2))
            if event.type == "session.status_idle":
                break


if __name__ == "__main__":
    main()
