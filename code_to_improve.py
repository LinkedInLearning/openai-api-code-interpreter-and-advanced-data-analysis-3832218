def calculate_average(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    average = total_sum / len(numbers)
    return average

# Example usage
numbers = [10, 20, 30, 40, 50]
print("Average:", calculate_average(numbers))