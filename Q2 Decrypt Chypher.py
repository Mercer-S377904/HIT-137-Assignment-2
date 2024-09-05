#function taken from Q3
def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        #shifts only letters
        if char.isalpha():
            # Reverse the key used in encryption
            shifted = ord(char) - key
            #If new values fall out of charachter range, from z back to a 
            if char.islower(): #This example doesnt need lowercase but kept it anyway
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            #Add shifted value to output
            decrypted_text += chr(shifted)
        else:
            #If not letter keep character unshifted
            decrypted_text += char
    #Function returns output
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
