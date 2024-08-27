import random

# Variables
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,_-"

# List to hold all characters
all = ""

print('Password Generator')
print('------------------')

# Function to get user input with validation
def get_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'n']:
            return response
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Collect user preferences
if get_input('Include lowercase letters? (y/n): ') == 'y':
    all += lower

if get_input('Include uppercase letters? (y/n): ') == 'y':
    all += upper

if get_input('Include numbers? (y/n): ') == 'y':
    all += numbers

if get_input('Include symbols? (y/n): ') == 'y':
    all += symbols

# Ensure at least one character set is selected
if not all:
    print("You must include at least one character type! Exiting...")
    exit()

# Password Length with exception handling
while True:
    try:
        length = int(input('Choose Password Length: ').strip())
        if length <= 0:
            print("Password length must be a positive number.")
        else:
            break  # Exit the loop if a valid length is entered
    except ValueError:
        print('Invalid input. Please enter a positive integer.')

# Generate Password
try:
    password = "".join(random.sample(all, length))
    print(f'Generated Password: {password}')
except ValueError as ve:
    print(f"Error: {ve}")
