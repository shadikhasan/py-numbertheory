from pynumbertheory import gcd, lcm, extended_gcd, is_perfect_square


def test_gcd_lcm():
    assert gcd(12, 18) == 6
    assert lcm(12, 18) == 36
    assert gcd(0, 5) == 5
    assert lcm(0, 5) == 0


def test_extended_gcd():
    g, x, y = extended_gcd(30, 12)
    assert g == 6
    assert 30 * x + 12 * y == g


def test_is_perfect_square():
    assert is_perfect_square(0)
    assert is_perfect_square(1)
    assert is_perfect_square(16)
    assert not is_perfect_square(15)
    assert not is_perfect_square(-1)
