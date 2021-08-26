def sum_of_squares(a):
  sum = 0
  for number in a :
    square = number**2
    sum +=square
  return sum

def test_one():
    assert sum_of_squares([1,2,3]) == 14

def test_two():
    assert sum_of_squares([2,3,4]) == 25

test_one()
test_two()
