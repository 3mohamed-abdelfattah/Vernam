def binary_to_text(binary_string):

  # Check if the binary string length is valid 
  if len(binary_string) % 8 != 0:
    print("Warning: Binary string length is not a multiple of 8. Decoding may produce unexpected results.")

  # Split the binary string into groups of 8 bits (assuming bytes)
  bytes = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

  # Convert each byte to its corresponding character (assuming 8-bit encoding)
  text = ''.join(chr(int(byte, 2)) for byte in bytes)
  return text

# Get binary string input from the user
binary_input = input("Enter a binary string: ")

# Convert binary to text and handle potential errors
text = binary_to_text(binary_input)

if text is None:
  print("Invalid binary input.")
else:
  print("The decoded text is:", text)

# hello world  = 0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100