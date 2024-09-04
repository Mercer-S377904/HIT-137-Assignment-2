def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key  # Reverse the key used in encryption
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
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

key = 13  # Decryption key explanation below code

# Our encrypted code
encrypted_code = """
VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY
NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"""

#call function to decrypt the code then print
decrypted_code = decrypt(encrypted_code, key)
print(decrypted_code)

#I just looked at the first two letters 'VZ' and looked for a two letter word where the letters are 4 characters apart (V(86)-Z(90) is -4). 
#I found IM is 4 letters apart. Then counted the space between I(73) and V(86), and M(77) and Z(90), which is 13. Used 13 as the key and it gave the decrypted string.
