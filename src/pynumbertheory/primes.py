from __future__ import annotations

from math import isqrt


def is_prime(n: int) -> bool:
    """
    Deterministic primality test for 32-bit-ish integers (simple trial division).
    Good enough for teaching / small competitive problems.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    limit = isqrt(n)
    f = 3
    while f <= limit:
        if n % f == 0:
            return False
        f += 2
    return True


def sieve(limit: int) -> list[int]:
    """
    Sieve of Eratosthenes.
    Return list of all primes <= limit.
    """
    if limit < 2:
        return []

    is_prime_arr = [True] * (limit + 1)
    is_prime_arr[0] = is_prime_arr[1] = False

    for p in range(2, isqrt(limit) + 1):
        if is_prime_arr[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime_arr[multiple] = False

    return [i for i, flag in enumerate(is_prime_arr) if flag]


def prime_factors(n: int) -> list[int]:
    """
    Return prime factors of n (with repetition) using trial division.
    Example: 60 -> [2, 2, 3, 5]
    """
    factors: list[int] = []
    if n < 0:
        n = -n  # ignore sign for factorization

    # factor out 2s
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # factor odd numbers
    f = 3
    limit = isqrt(n) + 1
    while f <= limit and n > 1:
        while n % f == 0:
            factors.append(f)
            n //= f
            limit = isqrt(n) + 1
        f += 2

    if n > 1:
        factors.append(n)

    return factors
