# test_simple_math.py
from simple_math import *
# the name of the testing function should
# also start with test_
def test_simple_add():
    assert simple_add(1,2) == 3

def test_simple_sub():
    assert simple_sub(1,2) == -1

def test_simple_mult():
    assert simple_mult(2,3) == 6

def test_simple_div():
    assert simple_div(6,3) == 2

def test_poly_first():
    assert poly_first(1,1,2) == 3

def test_poly_second():
    assert poly_second(1,1,2,3) == 6

