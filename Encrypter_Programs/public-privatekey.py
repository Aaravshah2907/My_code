import random

# Generate a large prime number


def generate_large_prime():
    while True:
        p = random.randint(2**127, 2**128)
        if is_prime(p):
            return p

# Check if a number is prime


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Compute the greatest common divisor of two numbers


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Compute the modular inverse of a number


def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError('No modular inverse')
    return x % m

# Compute the extended Euclidean algorithm


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

# Generate a public/private key pair


def generate_key_pair():
    # Choose two large prime numbers
    p = generate_large_prime()
    q = generate_large_prime()

    # Compute n and phi(n)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose an encryption exponent e
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break

    # Compute the decryption exponent d
    d = mod_inverse(e, phi)

    # Return the public and private keys
    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key

# Encrypt a message using a public key


def encrypt(message, public_key):
    n, e = public_key
    message_int = int.from_bytes(message.encode(), 'big')
    ciphertext_int = pow(message_int, e, n)
    ciphertext_bytes = ciphertext_int.to_bytes(
        (n.bit_length() + 7) // 8, 'big')
    return ciphertext_bytes

# Decrypt a message using a private key


def decrypt(ciphertext, private_key):
    n, d = private_key
    ciphertext_int = int.from_bytes(ciphertext, 'big')
    message_int = pow(ciphertext_int, d, n)
    message_bytes = message_int.to_bytes((n.bit_length() + 7) // 8, 'big')
    message = message_bytes.decode()
    return message


# Generate a key pair
public_key, private_key = generate_key_pair()

# Encrypt a message
message = input("Enter message")
ciphertext = encrypt(message, public_key)
print(ciphertext)

# Decrypt the ciphertext
decrypted_message = decrypt(ciphertext, private_key)

# Print the decrypted message
print(decrypted_message)
