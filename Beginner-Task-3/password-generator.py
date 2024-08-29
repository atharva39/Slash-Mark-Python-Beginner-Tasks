# Slash Mark Python Internship (Beginner: Task 3)

import random
import string

def generate_password(pwlength):
    """
    Generate a list of passwords with the specified lengths.

    Parameters:
    pwlength (list): A list of integers where each integer represents the length of a password.

    Returns:
    list: A list of generated passwords.
    """
    # Define the alphabet, digits, and special characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # List to store generated passwords
    passwords = []

    # Generate a password for each specified length
    for length in pwlength:
        if length < 8:
            raise ValueError("Password length should be at least 8 characters.")
        password = "".join(random.choice(characters) for _ in range(length))

        # Ensure the password contains at least one number, one uppercase letter, one lowercase letter, and one special character
        password = ensure_complexity(password)

        # Add the generated password to the list
        passwords.append(password)

    return passwords

def ensure_complexity(password):
    """
    Ensure the password contains at least one number, one uppercase letter, one lowercase letter, and one special character.

    Parameters:
    password (str): The initial generated password.

    Returns:
    str: The password with guaranteed complexity.
    """
    if not any(c.isdigit() for c in password):
        password = replace_with_number(password)
    if not any(c.islower() for c in password):
        password = replace_with_lowercase_letter(password)
    if not any(c.isupper() for c in password):
        password = replace_with_uppercase_letter(password)
    if not any(c in string.punctuation for c in password):
        password = replace_with_special_character(password)

    return password

def replace_with_number(password):
    """
    Replace a random character in the password with a number.

    Parameters:
    password (str): The initial generated password.

    Returns:
    str: The password with a number replacing a character.
    """
    replace_index = random.randrange(len(password))
    return password[:replace_index] + str(random.randint(0, 9)) + password[replace_index + 1:]

def replace_with_uppercase_letter(password):
    """
    Replace a random character in the password with an uppercase letter.

    Parameters:
    password (str): The initial generated password.

    Returns:
    str: The password with an uppercase letter replacing a character.
    """
    replace_index = random.randrange(len(password))
    uppercase_letter = random.choice(string.ascii_uppercase)
    return password[:replace_index] + uppercase_letter + password[replace_index + 1:]

def replace_with_lowercase_letter(password):
    """
    Replace a random character in the password with a lowercase letter.

    Parameters:
    password (str): The initial generated password.

    Returns:
    str: The password with a lowercase letter replacing a character.
    """
    replace_index = random.randrange(len(password))
    lowercase_letter = random.choice(string.ascii_lowercase)
    return password[:replace_index] + lowercase_letter + password[replace_index + 1:]

def replace_with_special_character(password):
    """
    Replace a random character in the password with a special character.

    Parameters:
    password (str): The initial generated password.

    Returns:
    str: The password with a special character replacing a character.
    """
    replace_index = random.randrange(len(password))
    special_char = random.choice(string.punctuation)
    return password[:replace_index] + special_char + password[replace_index + 1:]

def main():
    """
    Main function to drive the password generation process.
    """
    while True:
        try:
            num_passwords = int(input("How many passwords do you want to generate? "))
            print(f"Generating {num_passwords} passwords")

            # List to store lengths of passwords to be generated
            password_lengths = []

            print("Minimum length of password should be 8")

            # Get the length of each password from the user
            for i in range(num_passwords):
                length = int(input(f"Enter the length of Password #{i + 1}: "))
                if length < 8:
                    raise ValueError("Password length should be at least 8 characters.")
                password_lengths.append(length)

            # Generate the passwords
            passwords = generate_password(password_lengths)

            # Print the generated passwords
            for i in range(num_passwords):
                print(f"Password #{i + 1} = {passwords[i]}")

        except ValueError as e:
            print(e)

        # Ask the user if they want to generate more passwords or quit
        continue_choice = input("Do you want to generate more passwords? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Exiting the program.")
            break

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
