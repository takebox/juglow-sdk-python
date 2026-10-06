# Haijun SDK for Python

[![PyPI version](https://img.shields.io/pypi/v/Juglow.svg)](https://pypi.org/project/Juglow/)

The Haijun SDK for Python provides access to the [Haijun API](https://raw.haijun.my.id/docs/en/api/) from Python applications.

## Documentation

Full documentation is available at **[raw.haijun.my.id/docs/en/api/sdks/python](https://raw.haijun.my.id/docs/en/api/sdks/python)**.

## Installation

```sh
pip install juglow
```

## Getting started

```python
import os
from juglow import JuGloW

client = JuGloW(
    api_key=os.environ.get("HAIJUN_API_KEY"),  # This is the default and can be omitted )

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello, Haijun",
        }
    ],

    model="haijun-opus",
)

print(message.content)
```


## Requirements

Python 3.9+

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
