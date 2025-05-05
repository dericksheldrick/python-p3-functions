#!/usr/bin/env python3

print("Hello, programmer!")

def greet(name):
    print(f"Hello,{name}!")

greet("Marion")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}")

greet_with_default()

def add(num1, num2):
    num_sum = num1 +num2
    print(num_sum)
    return num_sum

add(2, 3)

def halve(number):
    result = number / 2
    print(result)
    return result

halve(8)
