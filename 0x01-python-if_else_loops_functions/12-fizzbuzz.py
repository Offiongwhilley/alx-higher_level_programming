#!/usr/bin/python3
def fizzBuzz():
    for item in range(101):
        
        if item % 15 == 0:
            print('FizzBuzz ')
        elif item % 3 == 0:
            print('Fizz ')
        elif item % 5 == 0:
            print('Buzz ')
        else:
            print(item)
