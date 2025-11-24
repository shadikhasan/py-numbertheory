"""
numbertheory
============

A small utility library for number theory:
- Basic arithmetic (gcd, lcm, extended gcd)
- Prime utilities (is_prime, sieve, factorization)
- Modular arithmetic (modular inverse, fast exponentiation, CRT)
"""

from .arithmetic import gcd, lcm, extended_gcd, is_perfect_square
from .primes import is_prime, sieve, prime_factors
from .modular import mod_pow, mod_inv, chinese_remainder

__all__ = [
    "gcd",
    "lcm",
    "extended_gcd",
    "is_perfect_square",
    "is_prime",
    "sieve",
    "prime_factors",
    "mod_pow",
    "mod_inv",
    "chinese_remainder",
]
