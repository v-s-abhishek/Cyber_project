def caesar_encrypt(message, shift):
  
    encrypted = ''
    for char in message:
        if char.isalpha():
            
            if char.isupper():
                encrypted += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(message, shift):

    decrypted = ''
    for char in message:
        if char.isalpha():
            
            if char.isupper():
                decrypted += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted += char
    return decrypted

message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

encrypted_message = caesar_encrypt(message, shift)
print("Encrypted message:", encrypted_message)

decrypted_message = caesar_decrypt(encrypted_message, shift)
print("Decrypted message:", decrypted_message)