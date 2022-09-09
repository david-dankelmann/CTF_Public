# Natas Level 14

Access data:

    username: natas14
    password: qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP

Connect to the service using basic HTTP auth by replacing the credentials in the link:
    
    http://*USERNAME*:*FLAG*@*USERNAME*.natas.labs.overthewire.org/

We got ourselves a Login form. Looking at the source code you can see, that the user input is used without escaping in the SQL query. Therefore, SQL injection is possible. 

We can force the password check to always be true using these values:

    Username: natas15
    Password: " OR "1"="1


<details>
  <summary>Solution</summary>
  Flag: TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB
</details>