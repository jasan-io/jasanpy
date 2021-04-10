# JasanPy

JasanPy is a Python package to access data powered by [jasan.io](https://www.jasan.io).

## Installation
`pip install jasanpy`

<br />


# Features
## Lookup (Lists)
### `get_companies_by_keywords`
You can retrieve a company name, the company's local name, its ticker and the name of exchange where the ticker is traded.[(example)](https://github.com/jasan-io/jasanpy/blob/main/example/lookup.py)

```
from jasanpy.lookup.lists import Lists
def list_example(self):
    ls = Lists()
    ls.get_companies_by_keywords("TSLA")
    # [{'symbol': 'TSLA', 'name': 'Tesla Inc', 'localName': 'Tesla Inc', 'market': 'NASDAQ'}]
```

A list of available exchanges is as follows:
- NYSE (US)
- NASDAQ (US)
- KOSPI (Korea)
- KOSDAQ (Korea)


