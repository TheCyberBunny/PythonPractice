#simple module with basic calculator functions for writing tests against

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0: #need to check for dividing by 0 since that will break stuff
        raise ValueError("Cannot divide by zero")
    return a / b