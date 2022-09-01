import string
#This script decrypts Caeser enciphered ciphertexts (stored in 'challenge'). Key is specified in 'rotation_key'

#Config
challenge = "OMQEMDUEQMEK"


#Setup
letters = list(string.ascii_uppercase) #Get all letters in the alphabet
letters_dict = {}


#Build letters_dict, which lets us easily access the position of each character in the alphabet
for i in range (0, len(letters)):
    letters_dict.update({letters[i] : i}) 

for current_key in range (0, len(letters)):
    solution = ""
    for c in challenge.upper():
        if c in letters_dict:
            solution += letters[letters_dict[c] - current_key % len(letters)]
        else:
            solution += c #Keep all other characters like whitespaces.        
    print(f"{solution} - key: {current_key}")