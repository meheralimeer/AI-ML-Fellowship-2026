"""Utility Functions Module | *args, **kwargs, lambda functions"""

def sum_all(*numbers):
    return sum(numbers)

def concatenate_strings(*strings, separator=" "):
    return separator.join(strings)

def create_profile(**kwargs):
    return kwargs

def flexible_calculator(operation, *numbers, **options):
    operations = {
        'sum': sum,
        'avg': lambda nums: sum(nums) / len(nums),
        'max': max,
        'min': min
    }
    result = operations.get(operation, sum)(numbers)
    
    if 'round_to' in options:
        result = round(result, options['round_to'])
    
    return result

square = lambda x: x ** 2
is_even = lambda x: x % 2 == 0

def apply_operation(data, operation):
    return [operation(item) for item in data]

def filter_data(data, condition):
    return [item for item in data if condition(item)]

def remove_duplicates(data):
    seen = set()
    result = []
    for item in data:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def chunk_list(data, chunk_size):
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

if __name__ == "__main__":
    print("Utility Functions Demo =-\n")
    
    print("*args:", sum_all(1, 2, 3, 4, 5))
    print("**kwargs:", create_profile(name="Ali", age=25))
    print("Lambda:", apply_operation([1, 2, 3, 4, 5], square))
    print("Flexible calc:", flexible_calculator('avg', 10, 20, 30, round_to=2))
