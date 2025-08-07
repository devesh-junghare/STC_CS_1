def encrypt(text, shift):
    cipher_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            cipher_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            cipher_text += char
    return cipher_text

def decrypt(text, shift):
    return encrypt(text, -shift)

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
mode = input("Encrypt or Decrypt? (e/d): ").strip().lower()

if mode == "e":
    print("Encrypted:", encrypt(message, shift))
else:
    print("Decrypted:", decrypt(message, shift))
