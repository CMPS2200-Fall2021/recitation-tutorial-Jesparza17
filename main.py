def sum_of_squares(a):
  sum = 0
  for number in a :
    square = number**2
    sum +=square
  return sum

def test_one():
    assert sum_of_squares([1,2,3])

def test_2():
    assert sum_of_squares([2,3,4])

test_one()
test_2()
