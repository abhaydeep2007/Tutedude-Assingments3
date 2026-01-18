def factorial(n):
    """
    Calculates the factorial of a non-negative integer n using recursion.
    Returns the factorial value or None if input is invalid.
    """
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    try:
        # Get input from user
        user_input = input("Enter a number: ")
        
        # Convert to integer
        number = int(user_input)
        
        # Calculate factorial
        result = factorial(number)
        
        if result is None:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"Factorial of {number} is: {result}")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
