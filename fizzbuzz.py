def fizzbuzz(x):
    if x % 15 == 0:
        return 'Fizzbuzz!'
    if x % 3 == 0:
        return 'Fizz'
    elif x % 5 == 0:
        return 'Buzz'
    else:
        return x

