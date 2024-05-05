import string

def generate_cipher_key(shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    cipher_key = dict(zip(alphabet, shifted_alphabet))
    print(cipher_key)
    return cipher_key

def encrypt(message, shift):
    cipher_key = generate_cipher_key(shift)
    encrypted_message = ''.join(cipher_key.get(char, char) for char in message.lower())
    return encrypted_message

def decrypt(encrypted_message, shift):
    cipher_key = generate_cipher_key(shift)
    reversed_cipher_key = {v: k for k, v in cipher_key.items()}
    decrypted_message = ''.join(reversed_cipher_key.get(char, char) for char in encrypted_message.lower())
    return decrypted_message

message = input("Enter the message: ")
shift = int(input("Enter the shift (an integer): "))

encrypted_message = encrypt(message, shift)
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = decrypt(encrypted_message, shift)
print(f"Decrypted Message: {decrypted_message}")