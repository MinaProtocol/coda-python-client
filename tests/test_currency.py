from CodaClient import CurrencyFormat, CurrencyUnderflow, Currency

precision = 10 ** 9

def test_constructor_whole_int():
  n = 500
  assert Currency(n).microcodas() == n * precision

def test_constructor_whole_float():
  n = 5.5
  assert Currency(n).microcodas() == n * precision

def test_constructor_whole_string():
  n = "5.5"
  assert Currency(n).microcodas() == float(n) * precision

def test_constructor_micro_int():
  n = 500
  assert Currency(n, format=CurrencyFormat.MICRO)

def test_add():
  assert (Currency(5) + Currency(2)).microcodas() == 7 * precision

def test_sub():
  assert (Currency(5) - Currency(2)).microcodas() == 3 * precision

def test_sub_underflow():
  try:
    Currency(5) - Currency(7)
    raise Exception('no underflow')
  except CurrencyUnderflow:
    pass
  except:
    raise

def test_mul_int():
  assert (Currency(5) * 2).microcodas() == 10 * precision

def test_mul_currency():
  assert (Currency(5) * Currency(2, format=CurrencyFormat.MICRO)).microcodas() == 10 * precision
