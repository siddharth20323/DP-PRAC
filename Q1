def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
     
    if mode == "decrypt":
        shift = -shift

    for char in text:
        
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        
        else:
            result += char

    return result

 
txt = "sidd2202@gmail.com"
s = 4


encrypted_text = caesar_cipher(txt, s, mode="encrypt")
print("Plain text:", txt)
print("Shift pattern:", s)
print("Encrypted text:", encrypted_text)

# Decryption
decrypted_text = caesar_cipher(encrypted_text, s, mode="decrypt")
print("Decrypted text:", decrypted_text)
