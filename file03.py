# Ask the user for their name
name = input("Enter your name: ")

# Greet the user using an f-string
print(f"Hello, {name}! Welcome to Python.")

def check_even_odd(number):
    """ Function to check if a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Ask the user for an integer
try:
    user_num = int(input("Enter a whole number: "))
    result = check_even_odd(user_num)
    print(f"The number {user_num} is {result}.")
except ValueError:
    print("Please enter a valid integer.")
