from MinaClient import CurrencyFormat, CurrencyUnderflow, Currency

precision = 10**9


def test_constructor_whole_int():
    n = 500
    assert Currency(n).nanominas() == n * precision


def test_constructor_whole_float():
    n = 5.5
    assert Currency(n).nanominas() == n * precision


def test_constructor_whole_string():
    n = "5.5"
    assert Currency(n).nanominas() == float(n) * precision


def test_constructor_nano_int():
    n = 500
    assert Currency(n, format=CurrencyFormat.NANO)


def test_add():
    assert (Currency(5) + Currency(2)).nanominas() == 7 * precision


def test_sub():
    assert (Currency(5) - Currency(2)).nanominas() == 3 * precision


def test_sub_underflow():
    try:
        Currency(5) - Currency(7)
        raise Exception("no underflow")
    except CurrencyUnderflow:
        pass
    except:
        raise


def test_mul_int():
    assert (Currency(5) * 2).nanominas() == 10 * precision


def test_mul_currency():
    assert (
        Currency(5) *
        Currency(2, format=CurrencyFormat.NANO)).nanominas() == 10 * precision


def test_random():
    assert Currency.random(Currency(5),
                           Currency(5)).nanominas() == 5 * precision
    for _ in range(25):
        rand = Currency.random(
            Currency(3, format=CurrencyFormat.NANO),
            Currency(5, format=CurrencyFormat.NANO),
        )
        assert 3 <= rand.nanominas() and rand.nanominas() <= 5
