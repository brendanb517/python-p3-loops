#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while num > 0:
        print(f"{num}")
        num -= 1
    if num == 0:
        print("Happy New Year!")

def square_integers(int_list):
    squares_list = [num ** 2 for num in int_list]
    return squares_list

def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)