
def calculate_average(numbers: list) -> float:
    if not numbers:  # Check if the list is empty
        return 0.0  # Return 0.0 or raise an exception as per use-case requirements
    return sum(numbers) / len(numbers)

# Example usage protected by __name__ guard to prevent execution on import
if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    try:
        average = calculate_average(numbers)
        print("Average:", average)
    except ZeroDivisionError:
        print("The list is empty. Cannot compute the average of an empty list.")
