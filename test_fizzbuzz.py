import pytest
from fizzbuzz import fizzbuzz

def test_fizzbuzz_normal_numbers():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(7) == 7
    assert fizzbuzz(19) == 19

def test_fizzbuzz_multiples_of_3():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(24) == 'Fizz'
    assert fizzbuzz(57) == 'Fizz'    

def test_fizzbuzz_multiples_of_5():
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(10) == 'Buzz'
    assert fizzbuzz(50) == 'Buzz'  