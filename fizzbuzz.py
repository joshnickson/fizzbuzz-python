def fizzbuzz(x):
    if x % 15 == 0:
        return 'Fizzbuzz!'
    elif x % 3 == 0:
        return 'Fizz'
    elif x % 5 == 0:
        return 'Buzz'
    else:
        return x

for i in range(1,101):
    print fizzbuzz(i)