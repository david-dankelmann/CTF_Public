# Krypton Level 4

    username: krypton5
    password: CLEARTEXT

Connect via SSH and enter password:

    ssh krypton5@krypton.labs.overthewire.org -p 2231

Switch to correct directory
    
    cd /krypton/krypton5


README tells us this is again a polyalphabetic cipher, but now we know nothing about the key, we have just three intercepted ciphertexts that were encrypted using the same key from the encrypted password.

So we need to find the key length first. Luckily, there is a technique called the [Kasisiki-Test](https://en.wikipedia.org/wiki/Kasiski_examination). 

Essentially you search for reoccuring sequences in the text and assume, that these resemble the same words in plaintext. For this to be true, all of them have to have the same distance in the text (modulo the key length), so you can take educated guesses what the key length must be.

I created a small [script](kasiskiTest.py) to help me here. It builds all 3-letter combinations (as there are many reoccuring 3-letter words in english like _the_) and keeps those, that occur the most in the sequence. Then, it counts the distance of these sequences modulo all possible key lengths between 3 and 15. The more matches are counted for each key length, the higher the probability that we got the right one. The output:


    Distance matches with a keylength of 3: 38
    Distance matches with a keylength of 4: 15
    Distance matches with a keylength of 5: 8
    Distance matches with a keylength of 6: 17
    Distance matches with a keylength of 7: 11
    Distance matches with a keylength of 8: 6
    Distance matches with a keylength of 9: 28
    Distance matches with a keylength of 10: 2
    Distance matches with a keylength of 11: 6
    Distance matches with a keylength of 12: 10
    Distance matches with a keylength of 13: 2
    Distance matches with a keylength of 14: 4

The most matches are with 3 and 9. Note, that 3 is the square root of 9 so all matches from 9 are obviously enclosed within 3 too. Calling the script with not only 3-letter combinations but also with 2-, 4- and 5- letter combinations let us derive with high confidence that the key length must be 9.


From here, you have to do a frequence analysis as in the previous challenges. After some time you should find the:

<details>
  <summary>Solution</summary>
  Key: keylength
  
  Password: RANDOM
</details>