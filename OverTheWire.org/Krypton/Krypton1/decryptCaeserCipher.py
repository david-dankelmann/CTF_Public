import string
#This script decrypts Caeser enciphered ciphertexts (stored in 'challenge'). Key is specified in 'rotation_key'

#Config
challenge = "YRIRY GJB CNFFJBEQ EBGGRA"
rotation_key = 13

#Setup
letters = list(string.ascii_uppercase) #Get all letters in the alphabet
letters_dict = {}
solution = ""

#Build letters_dict, which lets us easily access the position of each character in the alphabet
for i in range (0, len(letters)):
    letters_dict.update({letters[i] : i}) 

#'Decrypt' all characters, but keep whitespaces
for c in challenge.upper():
    if c in letters_dict:
        solution += letters[letters_dict[c] - 13 % len(letters)]
    else:
        solution += c #Keep all other characters like whitespaces.
        
print(solution)