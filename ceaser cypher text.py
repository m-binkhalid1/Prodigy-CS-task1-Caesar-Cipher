alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here is our encrypted text: {cipher_text}")

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"Here is our decrypted text: {plain_text}")

whatToDo = input("Type 'encrypt' to encryption, and 'decrypt' for decryption:\n")
text = input("Type your message:\n")
shift = int(input("Enter Shift key:\n"))

if whatToDo == "encrypt":
    encryption(plain_text=text, shift_key=shift)
elif whatToDo == "decrypt":
    decryption(cipher_text=text, shift_key=shift)
else:
    print("Invalid option. Please choose 'encrypt' or 'decrypt'.")
