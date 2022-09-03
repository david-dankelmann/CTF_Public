# Krypton Level 2

    user: krypton2
    password: ROTTEN

Connect via SSH and enter password:

    ssh krypton2@krypton.labs.overthewire.org -p 2231

Switch to correct directory
    
    cd /krypton/krypton2

The _README_ file tells us, we have again a Caeser enciphered text, but this time, we don't know the key. Then there is information about a binary that encrypts anything we are giving to it using the same key, the password was encrypted with.

The encrypted ciphertext within krypton2 is: _OMQEMDUEQMEK_

My initial approach was to slightly modify my solution from the previous challenge to *bruteforce* the caeser cipher (as there are only 26 keys). Indeed, coding the [solution](bruteforceCaeserCipher.py) yields only one solution that has semantic sense to it. The rotation key must be 12.

    OMQEMDUEQMEK - key: 0
    NLPDLCTDPLDJ - key: 1
    MKOCKBSCOKCI - key: 2
    LJNBJARBNJBH - key: 3
    KIMAIZQAMIAG - key: 4
    JHLZHYPZLHZF - key: 5
    IGKYGXOYKGYE - key: 6
    HFJXFWNXJFXD - key: 7
    GEIWEVMWIEWC - key: 8
    FDHVDULVHDVB - key: 9
    ECGUCTKUGCUA - key: 10
    DBFTBSJTFBTZ - key: 11
    CAESARISEASY - key: 12
    BZDRZQHRDZRX - key: 13
    AYCQYPGQCYQW - key: 14
    ZXBPXOFPBXPV - key: 15
    YWAOWNEOAWOU - key: 16
    XVZNVMDNZVNT - key: 17
    WUYMULCMYUMS - key: 18
    VTXLTKBLXTLR - key: 19
    USWKSJAKWSKQ - key: 20
    TRVJRIZJVRJP - key: 21
    SQUIQHYIUQIO - key: 22
    RPTHPGXHTPHN - key: 23
    QOSGOFWGSOGM - key: 24
    PNRFNEVFRNFL - key: 25

However, this solution is sloppy, as it relies on the solution to have semantic sense (often, CTF flags do not). So let's  do it the proper way too.

If the binary encrypts arbitrary text with the key used to encipher the password, we can easily leak the key. Just create a file only containing the letter 'A' in it - after encryption you can derive the key by counting the distance of plaintext letter vs. cipertext letter in the alphabet. 

Let's do it (following instructions from the README):

    mkdir /tmp/testarea1
    cd /tmp/testarea1
    ln -s /krypton/krypton2/keyfile.dat
    chmod 777 .
    echo "A" > plaintext.txt
    /krypton/krypton2/encrypt plaintext.txt
    cat ciphertext

    > M

M comes 12 positions after the A within the alphabet, so we have confirmation that our rotation key is indeed 12. Now we can decrypt the Challenge _OMQEMDUEQMEK_ using [our decrypting script from the previous level](../Krypton1/decryptCaeserCipher.py) or use the _tr_ command again. 

<details>
  <summary>Solution</summary>
  Password: CAESARISEASY
</details>
    