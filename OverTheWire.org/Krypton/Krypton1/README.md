# Krypton Level 1

Access data obtained through previous level:

    Username: _krypton1_
    Password: _KRYPTONISGREAT_

We are instructed to connect to _krypton.labs.overthewire.org_ using SSH on port 2231, so let's do it:

    ssh krypton1@krypton.labs.overthewire.org -p 2231

After entering the password we land on some server in the _/home/krypton1_ directory.

From https://overthewire.org/wargames/krypton/krypton1.html we know, that we must go into the _/krypton_ directory, so let's go there:

    cd /krypton/krypton1

Now we see two files. The README tells us, that the flag is encrypted in the other file _krypton2_ using an 'encryption' called _ROT13_ and some more tips.

Let's dump out the 'encryption' that yields or challenge:

    cat krypton2
    > YRIRY GJB CNFFJBEQ EBGGRA 

Let's check out what ROT13 is: https://en.wikipedia.org/wiki/ROT13 

Ah. Caesar Cipher. That rings a bell. So we just need to replace each character with the one that is 13 positions ahead of it in the alphabet (Before the A comes the Z and vice versa)

You can code your own solution (e.g. to decrypt all caeser ciphers, not only ROT13) like [that](decryptCaeserCipher.py) or use the shell built-in command _tr_


    cat krypton2 | tr "[a-zA-Z]" "[n-za-mN-ZA-M]"


<details>
  <summary>Solution</summary>
  LEVEL TWO PASSWORD ROTTEN
  
  Password: ROTTEN
</details>





