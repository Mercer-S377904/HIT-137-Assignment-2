def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha(): #Shifts letters only
            shifted = ord(char) + key #shift adds key only
            #Line 7 to 16 ensures letters dont get shifted into characters by shifting from z back to a
            if char.islower(): 
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26

            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

key = ????????????????
encrypted_code = encrypt(original_code, key)
print(encrypted_code)
