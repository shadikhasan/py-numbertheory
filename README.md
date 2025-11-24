numbertheory
============

Compact, classroom-friendly number theory helpers for Python projects and scripts.

Features
--------
- Basic arithmetic: `gcd`, `lcm`, `extended_gcd`, `is_perfect_square`
- Primes: `is_prime`, `sieve`, `prime_factors`
- Modular arithmetic: `mod_pow` (fast exponentiation), `mod_inv`, `chinese_remainder`

Installation
------------
Requires Python 3.9+.

```bash
pip install numbertheory
```

Or from source for development:

```bash
pip install -e .[test]
```

Usage
-----
```python
from numbertheory import (
    gcd, lcm, extended_gcd, is_perfect_square,
    is_prime, sieve, prime_factors,
    mod_pow, mod_inv, chinese_remainder,
)

gcd(12, 18)                      # 6
is_prime(97)                     # True
sieve(20)                        # [2, 3, 5, 7, 11, 13, 17, 19]
prime_factors(60)                # [2, 2, 3, 5]
mod_pow(2, 10, 1000)             # 24
mod_inv(3, 11)                   # 4
chinese_remainder([2, 3, 2], [3, 5, 7])  # 23
```

Testing
-------
```bash
python -m pytest
```

License
-------
MIT
