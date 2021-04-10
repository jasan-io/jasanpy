# JasanPy

JasanPy is a Python package to access data powered by [jasan.io](https://www.jasan.io).

## Installation
`pip install jasanpy`

<br />


# Features
## Lookup
Using JasanPy, you can retrieve a list of companies that are publicly traded on NYSE, NASDAQ, KOSPI and KOSDAQ [(example)](https://github.com/jasan-io/jasanpy/blob/main/example/lookup.py)
```
from jasanpy.lookup.lists import Lists
def list_example(self):
    ls = Lists()
    ls.get_companies_by_keywords("TSLA")
    # [{'symbol': 'TSLA', 'name': 'Tesla Inc', 'localName': 'Tesla Inc', 'market': 'NASDAQ'}]
```


