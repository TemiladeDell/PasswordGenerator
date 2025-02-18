import re
import secrets
import string

# Function to check if the user likes the generated password
def check_password(new_password):
    user_choice = input(f'Your generated password is: {new_password}\nDo you like the password (y/n): ')
    if user_choice == 'y':
        print(f'Your new password is: {new_password}')
    elif user_choice == 'n':
        print("Generating a new password...")
        new_password = generate_password()  # Generate a new password
        check_password(new_password)  # Recursively call check_password to recheck the new password

# Function to generate a password with specific constraints
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Prompt user to input desired password length
    length = int(input('Enter the length of password you want: '))

    # Ensure the length is between 8 and 16 characters
    while length < 8 or length > 16:
        print('Password must be between 8 and 16 characters!')
        length = int(input('Input the length: '))

    # Define the character sets to be used in the password
    letters = string.ascii_letters  # Uppercase and lowercase letters
    digits = string.digits  # Numeric digits (0-9)
    symbols = string.punctuation  # All punctuation symbols
    accepted_symbols = '!@#$%^&*-_=+?:;.'  # Custom set of acceptable symbols

    # Combine all characters that can be used in the password
    all_characters = letters + digits + accepted_symbols

    # Loop until the password meets all specified constraints
    while True:
        password = ''  # Start with an empty password string

        # Generate a random password of the specified length
        for _ in range(length):
            password += secrets.choice(all_characters)  # Append a random character from all_characters
        
        # Define the constraints for the password
        constraints = [
            (nums, r'\d'),  # At least 'nums' digits
            (special_chars, fr'[{symbols}]'),  # At least 'special_chars' special characters
            (uppercase, r'[A-Z]'),  # At least 'uppercase' uppercase letters
            (lowercase, r'[a-z]')  # At least 'lowercase' lowercase letters
        ]

        # Check if all constraints are satisfied
        if all(
            constraint <= len(re.findall(pattern, password))  # Ensure the count of matched pattern meets the constraint
            for constraint, pattern in constraints
        ):
            break  # If all constraints are met, break the loop and return the password
    
    return password  # Return the generated password

# Generate a password and check if the user likes it
new_password = generate_password()
check_password(new_password)
