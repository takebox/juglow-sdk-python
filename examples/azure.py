# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "juglow",
# ]
#
# [tool.uv.sources]
# juglow = { path = "../", editable = true }
# ///

from juglow import JuGloWFoundry

cl = JuGloWFoundry(
    resource="your-resource-name",
    api_key="your-foundry-Juglow-api-key",
)

response = cl.messages.create(
    model="haijun-haiku",
    messages=[
        {"role": "user", "content": "Hello!"},
    ],
    max_tokens=1024,
)

print(response)
