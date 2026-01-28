"""Generators & Iterators"""

def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def infinite_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def custom_range(start, end, step=1):
    current = start
    if step > 0:
        while current < end:
            yield current
            current += step
    else:
        while current > end:
            yield current
            current += step

def even_numbers(limit):
    num = 0
    while num <= limit:
        yield num
        num += 2

def squares_generator(n):
    for i in range(n):
        yield i ** 2

def read_file_lines(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"File {filename} not found")

class CountDown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

class EvenIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration
        result = self.current
        self.current += 2
        return result


if __name__ == "__main__":
    print("Generators & Iterators Demo =-\n")
    
    print("1. Fibonacci Generator:")
    fib = fibonacci_generator(10)
    print(f"First 10 Fibonacci numbers: {list(fib)}")
    print()
    
    print("2. Infinite Fibonacci (first 15):")
    inf_fib = infinite_fibonacci()
    first_15 = [next(inf_fib) for _ in range(15)]
    print(first_15)
    print()
    
    print("3. Custom Range:")
    print(f"custom_range(0, 10, 2): {list(custom_range(0, 10, 2))}")
    print(f"custom_range(10, 0, -1): {list(custom_range(10, 0, -1))}")
    print()
    
    print("4. Even Numbers Generator:")
    print(f"Even numbers up to 20: {list(even_numbers(20))}")
    print()
    
    print("5. Squares Generator:")
    print(f"Squares of 0-9: {list(squares_generator(10))}")
    print()
    
    print("6. CountDown Iterator:")
    countdown = CountDown(5)
    print(f"Countdown from 5: {list(countdown)}")
    print()
    
    print("7. Even Iterator:")
    evens = EvenIterator(10)
    print(f"Even numbers 0-10: {list(evens)}")
    print()
    
    print("8. Generator Expression:")
    squares_gen = (x**2 for x in range(10))
    print(f"Squares using generator expression: {list(squares_gen)}")
