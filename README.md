# MLFIFA
**Coming soon:** *We are currently developing a website to __compare players__ using __statistical visualization__.*

This repo helps addicted FIFA players (like us) build a _Dream Team_ in Manager mode using player statistics from the [SoFIFA](https://sofifa.com) platform.

---
## Repo Contents

1. A [Web Crawler](src/sofifa_parser) to __scrape__ [_SoFIFA_](https://sofifa.com) website.
2. An [API](http://sofifa-api.herokuapp.com/api/v1/players/) to __search__ through _SoFIFA_ data.
3. A [Mixed-Integer Linear Optimization](https://en.wikipedia.org/wiki/Integer_programming) algorithm for help you choose the __best players and teams__ based on their __potential__ and your __budget__.

---
## Implementation

### 🕷️ Web Crawler

We built a [web crawler](src/sofifa_parser) to collect and parse information on __all 18000+ FIFA players__ avaliable at [_SoFIFA_](https://sofifa.com).

### ☁️ API

Do you want to have easy access to all SoFIFA data?  __We provide an API for that!__
Check out the [API folder](src/sofifa_api) for examples.

### 🎯 Optimization Algorithm

We determine optimized player configurations using the data collected from SoFIFA. A subset of player information is used to form an Integer Programming optimization problem. For optimization we use the [Pulp](https://pythonhosted.org/PuLP/pulp.html#module-pulp) python module.

Please see the example Jupyter [notebook](src/python/Model.ipynb) for implementation details.

---
## 👥 Authors

🧔 __Diogo Dantas__:

* diogoventura@cc.ci.ufpb.br
* [Github](https://github.com/DiogoDantas)

🤵 __Arnaldo Gualberto__:

* arnaldo.g12@gmail.com
* [Github](https://github.com/arnaldog12)
* [Personal Website](http://arnaldogualberto.com)
