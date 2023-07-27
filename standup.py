def generate_fibonacci_numbers(limit):
    """
    Generate Fibonacci numbers up to the given limit.

    Parameters:
    limit (int): The maximum value for Fibonacci numbers.

    Returns:
    list: A list containing the Fibonacci numbers up to the given limit.
    """
    fibonacci_numbers = [0, 1]
    while True:
        next_fib = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        if next_fib > limit:
            break
        fibonacci_numbers.append(next_fib)
    return fibonacci_numbers

def main():
    try:
        limit = int(input("Enter the limit for Fibonacci numbers: "))
        if limit < 0:
            print("Limit should be a non-negative integer.")
            return

        fibonacci_numbers = generate_fibonacci_numbers(limit)
        print("Fibonacci numbers up to {}:".format(limit))
        print(fibonacci_numbers)

    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")

if __name__ == "__main__":
    main()
