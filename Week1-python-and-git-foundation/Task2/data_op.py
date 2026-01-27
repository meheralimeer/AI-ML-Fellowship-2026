"""Data Manipulation | Remove duplicates, Sort, Max/Min/Average, Complexity"""

def remove_duplicates(data):
    seen = set()
    result = []
    for item in data:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def bubble_sort(data):
    arr = data.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def find_max_min(data):
    if not data:
        return None, None
    return max(data), min(data)

def calculate_average(data):
    if not data:
        return 0
    return sum(data) / len(data)

def calculate_statistics(data):
    if not data:
        return {"error": "Empty dataset"}
    
    sorted_data = sorted(data)
    n = len(data)
    mean = sum(data) / n
    
    median = sorted_data[n // 2] if n % 2 != 0 else (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = variance ** 0.5
    
    return {
        "count": n,
        "mean": round(mean, 2),
        "median": median,
        "min": min(data),
        "max": max(data),
        "std_dev": round(std_dev, 2)
    }

def group_by(data, key):
    groups = {}
    for item in data:
        group_key = item.get(key)
        if group_key not in groups:
            groups[group_key] = []
        groups[group_key].append(item)
    return groups

if __name__ == "__main__":
    numbers = [5, 2, 8, 2, 9, 1, 5, 8, 3, 7]
    
    print("Data Operations Demo =-\n")
    
    print("Original:", numbers)
    print("Remove duplicates:", remove_duplicates(numbers))
    print("Quick sort:", quick_sort(numbers))
    print("Max, Min:", find_max_min(numbers))
    print("Average:", calculate_average(numbers))
    print("Statistics:", calculate_statistics(numbers))
    
    students = [
        {"name": "Ali", "grade": "A", "score": 95},
    ]
    
    print("\nGrouped by grade:", group_by(students, "grade"))
