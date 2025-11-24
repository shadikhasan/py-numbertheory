from __future__ import annotations

from .arithmetic import extended_gcd


def mod_pow(base: int, exponent: int, modulus: int) -> int:
    """
    Fast modular exponentiation: (base ** exponent) % modulus.
    """
    if modulus <= 0:
        raise ValueError("modulus must be positive")

    base %= modulus
    result = 1
    e = exponent

    while e > 0:
        if e & 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        e >>= 1

    return result


def mod_inv(a: int, m: int) -> int:
    """
    Modular inverse of a modulo m.
    Returns x such that (a * x) % m == 1.
    Raises ValueError if inverse does not exist.
    """
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"No modular inverse exists for {a} mod {m}")
    return x % m


def chinese_remainder(remainders: list[int], moduli: list[int]) -> int:
    """
    Solve system of congruences using the Chinese Remainder Theorem:

        x ≡ remainders[i] (mod moduli[i])

    Returns the smallest non-negative solution x.
    Raises ValueError if moduli are not pairwise coprime.
    """
    if len(remainders) != len(moduli):
        raise ValueError("remainders and moduli must have same length")

    from math import prod

    M = prod(moduli)
    x = 0

    for (ai, mi) in zip(remainders, moduli):
        Mi = M // mi
        inv = mod_inv(Mi, mi)  # may raise if not coprime
        x = (x + ai * Mi * inv) % M

    return x
