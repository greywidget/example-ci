def add(a, b):
    return a + b


def subtract(a, b):
    return a - b  # <--- fix this in step 7


def multiply(a, b):
    return a * b


def chortle():
    print("Nya Nya Nya")


def absolute(a):
    return abs(a)


def convert_fahrenheit_to_celsius(fahrenheit):
    if fahrenheit < 0:
        raise AssertionError
    return multiply(subtract(fahrenheit, 32), 9 / 5)  # <-- Fix this in step 7
