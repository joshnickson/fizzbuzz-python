import pytest
import fizzbuzz

def test_fizzbuzz_normal_numbers():
    assert fizzbuzz.fizzbuzz(1) == 1
    assert fizzbuzz.fizzbuzz(7) == 7
    assert fizzbuzz.fizzbuzz(19) == 19

def test_fizzbuzz_multiples_of_3():
    assert fizzbuzz.fizzbuzz(3) == 'Fizz'
    assert fizzbuzz.fizzbuzz(24) == 'Fizz'
    assert fizzbuzz.fizzbuzz(57) == 'Fizz'    

def test_fizzbuzz_multiples_of_5():
    assert fizzbuzz.fizzbuzz(5) == 'Buzz'
    assert fizzbuzz.fizzbuzz(10) == 'Buzz'
    assert fizzbuzz.fizzbuzz(50) == 'Buzz'  

def test_fizzbuzz_multiples_of_5():
    assert fizzbuzz.fizzbuzz(15) == 'Fizzbuzz!'
    assert fizzbuzz.fizzbuzz(30) == 'Fizzbuzz!'
    assert fizzbuzz.fizzbuzz(60) == 'Fizzbuzz!'  