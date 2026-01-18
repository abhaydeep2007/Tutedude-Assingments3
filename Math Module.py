import math

def calculate_math_operations():
    try:
        # Get input from user
        user_input = input("Enter a number: ")
        
        # Convert to float to handle decimals
        number = float(user_input)
        
        # 1. Calculate Square root
        # Check if number is non-negative for square root
        if number >= 0:
            square_root = math.sqrt(number)
            print(f"Square root: {square_root}")
        else:
            print("Square root: Undefined for negative numbers in real number system")

        # 2. Calculate Natural logarithm (log base e)
        # Check if number is positive for log
        if number > 0:
            log_val = math.log(number)
            print(f"Logarithm: {log_val}")
        else:
            print("Logarithm: Undefined for non-positive numbers")

        # 3. Calculate Sine (in radians)
        sine_val = math.sin(number)
        print(f"Sine: {sine_val}")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    calculate_math_operations()
