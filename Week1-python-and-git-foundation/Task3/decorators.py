"""Decorators | Execution Time & Custom Decorators"""

import time
import functools

def execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_duration = end_time - start_time
        print(f"{func.__name__} executed in {execution_duration:.6f} seconds")
        return result
    return wrapper

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Negative value not allowed: {arg}")
        return func(*args, **kwargs)
    return wrapper

def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Returning cached result for {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator


@execution_time
def slow_function():
    time.sleep(0.5)
    return "Done"

@log_calls
def add(a, b):
    return a + b

@validate_positive
def calculate_square_root(n):
    return n ** 0.5

@memoize
@execution_time
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

@repeat(3)
def roll_dice():
    import random
    return random.randint(1, 6)


if __name__ == "__main__":
    print("Decorators Demo =-\n")
    
    print("1. Execution Time Decorator:")
    slow_function()
    print()
    
    print("2. Log Calls Decorator:")
    add(5, 3)
    print()
    
    print("3. Validate Positive Decorator:")
    try:
        print(calculate_square_root(16))
        calculate_square_root(-4)
    except ValueError as e:
        print(f"Error: {e}")
    print()
    
    print("4. Memoize Decorator:")
    print(f"fibonacci(10) = {fibonacci_recursive(10)}")
    print(f"fibonacci(10) = {fibonacci_recursive(10)}")
    print()
    
    print("5. Repeat Decorator:")
    print(f"Rolling dice 3 times: {roll_dice()}")
