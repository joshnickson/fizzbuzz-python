import pytest
from fizzbuzz import fizzbuzz

def test_fizzbuzz_normal_numbers():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(7) == 7
    assert fizzbuzz(19) == 19