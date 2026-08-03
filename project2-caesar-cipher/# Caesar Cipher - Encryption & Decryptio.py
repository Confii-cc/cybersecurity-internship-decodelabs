# Caesar Cipher - Encryption & Decryption

def encrypt(text, shift):
    result = ""  

    for char in text:
        if char.isalpha():
            # Determine uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

def decrypt(text, shift):
    result = "" 
    
    for char in text:
        if char.isalpha():
            # Determine uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char

    return result

    

# --- Main program ---
message = input("Enter your message: ")
shift = int(input("Enter shift key (number): "))

encrypted = encrypt(message, shift)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted:", decrypted)