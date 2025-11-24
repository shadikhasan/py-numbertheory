from numbertheory import is_prime, sieve, prime_factors


def test_is_prime():
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(97)


def test_sieve():
    primes = sieve(20)
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19]


def test_prime_factors():
    assert prime_factors(60) == [2, 2, 3, 5]
    assert prime_factors(97) == [97]
