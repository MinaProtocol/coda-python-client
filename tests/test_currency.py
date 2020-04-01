from CodaClient import CurrencyFormat, CurrencyUnderflow, Currency

precision = 10 ** 9

def test_constructor_whole_int():
  n = 500
  assert Currency(n).nanocodas() == n * precision

def test_constructor_whole_float():
  n = 5.5
  assert Currency(n).nanocodas() == n * precision

def test_constructor_whole_string():
  n = "5.5"
  assert Currency(n).nanocodas() == float(n) * precision

def test_constructor_nano_int():
  n = 500
  assert Currency(n, format=CurrencyFormat.NANO)

def test_add():
  assert (Currency(5) + Currency(2)).nanocodas() == 7 * precision

def test_sub():
  assert (Currency(5) - Currency(2)).nanocodas() == 3 * precision

def test_sub_underflow():
  try:
    Currency(5) - Currency(7)
    raise Exception('no underflow')
  except CurrencyUnderflow:
    pass
  except:
    raise

def test_mul_int():
  assert (Currency(5) * 2).nanocodas() == 10 * precision

def test_mul_currency():
  assert (Currency(5) * Currency(2, format=CurrencyFormat.NANO)).nanocodas() == 10 * precision
