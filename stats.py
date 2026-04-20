def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    minimum = min(numbers) if count > 0 else None
    maximum = max(numbers) if count > 0 else None

    return {
        "sum": total,
        "average": average,
        "min": minimum,
        "max": maximum
    }



user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(float, user_input.split()))

results = calculate_stats(numbers)

print("Sum:", results["sum"])
print("Average:", results["average"])
print("Min:", results["min"])
print("Max:", results["max"])