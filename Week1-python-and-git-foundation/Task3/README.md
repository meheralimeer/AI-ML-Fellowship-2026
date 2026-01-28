# Task 3 - Object-Oriented & Advanced Python

## Overview
Advanced Python programming covering OOP principles, decorators, and generators.

## Files

### Core Modules
- `bank_account.py` - Bank account system demonstrating OOP concepts
- `decorators.py` - Custom decorators including execution time tracker
- `generators.py` - Iterator and generator implementations

## Concepts Covered

### OOP Concepts
- **Classes & Objects** - Creating and instantiating classes
- **Encapsulation** - Private attributes with underscore prefix
- **Inheritance** - Base class and child classes (SavingsAccount, CheckingAccount)
- **Polymorphism** - Method overriding in child classes
- **Magic Methods** - `__init__`, `__str__`, `__iter__`, `__next__`

### Decorators
- Execution time measurement
- Function call logging
- Input validation
- Memoization (caching)
- Parameterized decorators

### Iterators & Generators
- Fibonacci generator
- Custom range generator
- Iterator protocol implementation
- Generator expressions
- Infinite generators

## Running the Code

```bash
python bank_account.py
python decorators.py
python generators.py
```

## Key Features

### bank_account.py
- Base `BankAccount` class with deposit/withdraw
- `SavingsAccount` with interest calculation
- `CheckingAccount` with overdraft protection
- Transaction history tracking
- Encapsulation of account data

### decorators.py
- `@execution_time` - Measures function execution time
- `@log_calls` - Logs function calls and returns
- `@validate_positive` - Validates positive inputs
- `@memoize` - Caches function results
- `@repeat(n)` - Executes function n times

### generators.py
- `fibonacci_generator(n)` - Generates first n Fibonacci numbers
- `custom_range(start, end, step)` - Custom range implementation
- `CountDown` iterator class
- `EvenIterator` class
- Generator expressions

## OOP Principles Demonstrated

**Encapsulation**: Private attributes (`_balance`, `_account_number`)  
**Inheritance**: Child classes inherit from `BankAccount`  
**Polymorphism**: `withdraw()` method overridden in `CheckingAccount`  
**Abstraction**: Clean public interface hiding implementation details

## Debugging
Use Python's built-in debugger:
```bash
python -m pdb bank_account.py
```

Common pdb commands:
- `n` - Next line
- `c` - Continue
- `l` - List code
- `p variable` - Print variable
- `q` - Quit

## Author
Meher Ali - AI/ML Fellowship, GDGOC COMSATS Attock
