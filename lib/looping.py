#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
        print("Happy New Year!")
    # code goes here!
    pass

def square_integers(int_list):
    squared_numbers = []
    for n in int_list:
        squared_numbers.append(n ** 2)
    return squared_numbers
    # code goes here!

    pass
def fizzbuzz():
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)
    # code goes here!

    pass
