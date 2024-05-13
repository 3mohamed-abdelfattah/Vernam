def vernam_cipher(plaintext, key):

        # Check if key length is shorter than message..?, then loop the key
    if len(key) < len(plaintext):
        key = key * ((len(plaintext) // len(key)) + 1)

        # Ensure key length matches or is more than message
    key = key[:len(plaintext)]

        # Convert inputs to lists
    plaintext = [int(bit) for bit in plaintext]
    key = [int(bit) for bit in key]

        # Perform XOR operation between each bit of message and key
    ciphertext = [plaintext[i] ^ key[i] for i in range(len(plaintext))]

        # Convert ciphertext list back to normal input
    ciphertext_str = ''.join(str(bit) for bit in ciphertext)

    return ciphertext_str

def main():

        # Inputs from User
    plaintext = input("Enter the Message: ")
        #ASCII
    plaintext_binary = ''.join(format(ord(char), '08b') for char in plaintext)
    print(plaintext_binary)

    key = input("Enter the key: ")
        #ASCII
    key_binary = ''.join(format(ord(char), '08b') for char in key)
    print(key_binary)

        # Encrypt the plaintext
    ciphertext = vernam_cipher(plaintext_binary, key_binary)
    print("Ciphertext:", ciphertext)

if __name__ == "__main__":
    main()
