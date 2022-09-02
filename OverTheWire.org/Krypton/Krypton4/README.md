# Krypton Level 4

    username: krypton4
    password: BRUTE

Connect via SSH and enter password:

    ssh krypton4@krypton.labs.overthewire.org -p 2231

Switch to correct directory
    
    cd /krypton/krypton4


The README tells us right away that this challenge is about the Vigenère cipher and explains it afterwards. Make sure to understand how it works!

We are given 2 encrypted text files, the encrypted pw for the next stage, the information that the key has 6 letters and you can consult the HINT that will tell you that you have to do a frequence analysis again, but you have to adjust it to the Vigenère cipher as this is now a polyalphabetic cipher.

[My script](frequenceAnalysisVigenere.py) that helped me solve this got a bit more complex. First, i adjusted the _decrypt_ function from the previous challenge to decipher the Vigenere Cipher with a given key (just do the inverse operation of the encryption explained in the task). Then, i did a frequence analysis but this time, it is done for each letter of the key separately. We know the key is 6 letters long, so every 6 letters the same key is reused. 

When you have analyzed the occurrence of the letters relatively to the position in the key, you can take the first three letters that occur the most and make an educated guess that each of these were among the plaintext letters E, S, or I, because they are the most probable letters. Using this approach, you can derive 9 possibilites for each position in the key letters. This yields this dictionary of possibilites of letters for each position in the key.

    {0: ['O', 'A', 'K', 'E', 'Q', 'A', 'T', 'F', 'P'],
    1: ['G', 'S', 'C', 'R', 'D', 'N', 'U', 'G', 'Q'],
    2: ['E', 'Q', 'A', 'T', 'F', 'P', 'O', 'A', 'K'],
    3: ['Y', 'K', 'U', 'N', 'Z', 'J', 'X', 'J', 'T'],
    4: ['F', 'R', 'B', 'E', 'Q', 'A', 'O', 'A', 'K'],
    5: ['N', 'Z', 'J', 'Y', 'K', 'U', 'B', 'N', 'X']}


Trying out some combinations didn't help, so something is missing. Maybe there is a better approach? Looking at the given files, you can see that both begin with
    
    YYI

The most probably word to begin an english text is 'The'. Calculating this by hand, we can guess that the first three key letters are 'FRE'. Essentially we are reducing complexity with this Known-Plaintext!

Now, you only need the letters for position 3, 4 and 5. A bit more of trial and error yields the key _FREKEY_. Decrypting our password with this key yields the solution of this challenge:

    CLEARTEXT