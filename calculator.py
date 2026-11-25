"""A simple command-line calculator."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Oops, you cannot divide by zero")
    return a / b
