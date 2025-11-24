from __future__ import annotations


def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor using Euclid's algorithm."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Compute the least common multiple of two integers."""
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Extended Euclidean algorithm.
    Returns (g, x, y) such that a*x + b*y = g = gcd(a, b).
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    # old_r is gcd, old_s and old_t are the Bezout coefficients
    return old_r, old_s, old_t


def is_perfect_square(n: int) -> bool:
    """Return True if n is a perfect square, False otherwise."""
    if n < 0:
        return False
    root = int(n**0.5)
    return root * root == n or (root + 1) * (root + 1) == n
