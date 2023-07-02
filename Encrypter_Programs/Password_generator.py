import random
import string
import time as t


def generate_password(length):
    """Generate a random password of the given length."""
    # Define the character set from which to choose characters.
    character_set = string.ascii_letters + string.digits + string.punctuation

    # Use the random module to generate a list of random characters.
    password_characters = [random.choice(character_set) for _ in range(length)]

    # Convert the list of characters to a string and return the result.
    return ''.join(password_characters)


lt = int(input("Enter Length :"))
password = generate_password(lt)
print(password)
t.sleep(12)
