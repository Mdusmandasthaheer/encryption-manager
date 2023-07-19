import os
import random
import string
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_random_string(length):
    """Generate a random string of specified length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def encrypt_file(plaintext_path, public_key_path, output_dir):
    # Load public key
    with open(public_key_path, 'r') as file:
        public_key = RSA.import_key(file.read())

    # Create cipher object
    cipher = PKCS1_OAEP.new(public_key)

    # Read plaintext file
    with open(plaintext_path, 'rb') as file:
        plaintext = file.read()

    # Encrypt the plaintext
    encrypted_data = cipher.encrypt(plaintext)

    # Generate a random name for the encrypted file
    encrypted_file_name = generate_random_string(8) + ".bin"

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Write encrypted data to output file
    output_file = os.path.join(output_dir, encrypted_file_name)
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

    print("Encryption completed successfully.")
    print("Encrypted file saved at:", output_file)

def decrypt_file(encrypted_path, private_key_path, output_dir):
    # Load private key
    with open(private_key_path, 'r') as file:
        private_key = RSA.import_key(file.read())

    # Create cipher object
    cipher = PKCS1_OAEP.new(private_key)

    # Read encrypted data file
    with open(encrypted_path, 'rb') as file:
        encrypted_data = file.read()

    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Generate a random name for the decrypted file
    decrypted_file_name = generate_random_string(8) + ".txt"

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Write decrypted data to output file
    output_file = os.path.join(output_dir, decrypted_file_name)
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

    print("Decryption completed successfully.")
    print("Decrypted file saved at:", output_file)

# Main program loop
while True:
    print("Choose an option:")
    print("1. Encrypt a file using RSA")
    print("2. Decrypt a file using RSA")
    print("3. Quit")
    choice = input("> ")
    if choice == "1":
        plaintext_file = input("Enter the path of the plaintext file: ")
        public_key_file = input("Enter the path of the public key: ")
        output_dir = "encrypted_files"
        encrypt_file(plaintext_file, public_key_file, output_dir)
    elif choice == "2":
        encrypted_file = input("Enter the path of the encrypted file: ")
        private_key_file = input("Enter the path of the private key: ")
        output_dir = "decrypted_files"
        decrypt_file(encrypted_file, private_key_file, output_dir)
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
