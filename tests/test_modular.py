from numbertheory import mod_pow, mod_inv, chinese_remainder


def test_mod_pow():
    assert mod_pow(2, 10, 1000) == 24
    assert mod_pow(3, 0, 7) == 1


def test_mod_inv():
    assert (3 * mod_inv(3, 11)) % 11 == 1


def test_chinese_remainder():
    # x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7) => x = 23
    x = chinese_remainder([2, 3, 2], [3, 5, 7])
    assert x == 23
