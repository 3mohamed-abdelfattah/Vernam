def vernam_cipher(Decryption, key):
    """
    Args:
        Decryption (str): The Decryption to be encrypted.
        key (str): The encryption key.  
    Returns:
        str: The ciphertext.
    """
    if len(key) < len(Decryption):
        key = key * ((len(Decryption) // len(key)) + 1)


    key = key[:len(Decryption)]


    Decryption = [int(bit) for bit in Decryption]
    key = [int(bit) for bit in key]


    ciphertext = [Decryption[i] ^ key[i] for i in range(len(Decryption))]


    ciphertext_str = ''.join(str(bit) for bit in ciphertext)

    return ciphertext_str

def main():
    """
    Prompts the user to enter the Decryption and key, and then displays the ciphertext.
    """

    Decryption = input("Enter the Decryptiontext: ")


    key = input("Enter the Cipher key: ")
    ciphertext = vernam_cipher(Decryption,key)
    print("Decryption:", ciphertext)

if __name__ == "__main__":
    main()
