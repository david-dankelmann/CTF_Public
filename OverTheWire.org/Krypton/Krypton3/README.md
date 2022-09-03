# Krypton Level 3

    username: krypton3
    password: CAESARISEASY

Connect via SSH and enter password:

    ssh krypton3@krypton.labs.overthewire.org -p 2231

Switch to correct directory
    
    cd /krypton/krypton3

The _README_ file tells us that we have to deal yet again with a substitution cipher, although now we don't know which one. A quick test using our [previous bruteforce solution](bruteforceCaeserCipher.py) reveals that this is **no** caeser cipher (because for all possible keys, there is not a single plaintext with semantic sense to it).

We are given three more ciphertexts (in addition to the encrypted password). We also know, that the same plaintext letter is always replaced with the same letter from the cipher alphabet (monoalphabetic cipher).

One of the attacks possible to execute here is the frequence analysis (they actually used this to decipher the Enigma from the Nazis in WW2 which helped to win the war). 

The distribution of letters in languages is not uniform, some [occur more than others](https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html). 

We can reasonably guess the possible plaintext characters associated with their ciphertext partner as we have enough encrypted ciphertexts using the same key. We do so, until the guessed mapping reveals a semantic meaningful key, as some deviation has to be expected (some letters have nearly the same probability, so you can't say for sure, that the order is maintained)

I merged all four ciphertexts and created a script [frequenceAnalysis.py](frequenceAnalysis.py) to count the letters in a given ciphertext. After that, they are sorted by their occurence. From there you can try to map each enciphered letter to the most probable plaintext letter obtaining a possible key dictionary. Prepare for some trial and error :-)

Trying to decrypt the password yields this:

    Ciphertext:
    KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS
    Plaintext:
    BECCD ONERL ECEVE CGOPT MAIIB OTDSI WTPRE

Still, we can't read the plaintext. But looking especially at the first word _BECCD_ we can derive that the mapping of 'V' => 'C' is most likely wrong. Why? What word has two consecutive 'C's in it? Let's look at the most probable neighbours of the letter C in the [table](https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html): They are 'L' or 'U'. Let's swap out 'L' and 'C' within our guessed key mapping and see what happens:

    Ciphertext:
    KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS
    Plaintext:
    BELLD ONERC ELEVE LGOPT MAIIB OTDSI WTPRE

Wohoo! There is a pattern now! The decrypted plaintext starts with "BELLD ONE" which sounds like WELL DONE. Adjusting 'B' and 'W' in our key dictionary:

    Ciphertext:
    KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS
    Plaintext:
    WELLD ONERC ELEVE LGOPT MAIIW OTDSI BTPRE

More progress. We now see *WELLDONERCELEVEL* ... This sounds like *WELL DONE THE LEVEL* ... Let's swap 'R' with 'T' and 'C' with 'H'

    Ciphertext:
    KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS
    Plaintext:
    WELLD ONETH ELEVE LGOPR MAIIW ORDSI BRPTE

Hmm... Now it's tricky. But we have more ciphertexts to guess from, so let's search there for a sequencec that has a wrong letter in it. For example, in the decrypted file contents there is the sequence 'EDSTT OUOCC PNSUA' This looks wrong. It appears that 'C' is still wrong. Later, there is also the sequence 'H ARDLY BLACE' -> 'C' should be replaced with 'M'.

    Ciphertext:
    KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS
    Plaintext:
    WELLD ONETH ELEVE LGOPR CAIIW ORDSI BRPTE

Last word could be 'BRUTE'? Swap 'P' and 'U'

    Ciphertext:
    KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS
    Plaintext:
    WELLD ONETH ELEVE LGOUR CAIIW ORDSI BRUTE

There is the sequence "SONSP OULDH ARDLY BLAME" -> Swap 'P' and 'C'

    Ciphertext:
    KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS
    Plaintext:
    WELLD ONETH ELEVE LGOUR PAIIW ORDSI BRUTE

Now i see it. 'GOUR' will most likely mean 'FOUR'. Swap 'F' and 'G'

    Ciphertext:
    KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS
    Plaintext:
    WELLD ONETH ELEVE LFOUR PAIIW ORDSI BRUTE

Swap 'I' and 'S'

    Ciphertext:
    KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS
    Plaintext:
    WELLD ONETH ELEVE LFOUR PASSW ORDIS BRUTE

Got it! 

The final key dictionary looks like this:

    {'A': 'B',
    'B': 'O',
    'C': 'I',
    'D': 'H',
    'E': 'G',
    'F': 'K',
    'G': 'N',
    'H': 'Z',
    'I': 'V',
    'J': 'T',
    'K': 'W',
    'L': 'Y',
    'M': 'U',
    'N': 'R',
    'O': 'X',
    'P': 'Q',
    'Q': 'A',
    'R': 'J',
    'S': 'E',
    'T': 'M',
    'U': 'S',
    'V': 'L',
    'W': 'D',
    'X': 'F',
    'Y': 'P',
    'Z': 'C'}


<details>
  <summary>Solution</summary>
  Password: BRUTE
</details>
