# Natas Level 2

Access data:

    username: natas2
    password: h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7

Connect to the service using basic HTTP auth by replacing the credentials in the link:
    
    http://*USERNAME*:*FLAG*@*USERNAME*.natas.labs.overthewire.org/

The page tells us, there is nothing on it but looking at the source code we see an embedded image: files/pixel.png

Let's check the files folder out: http://natas2.natas.labs.overthewire.org/files

Oh there is a [users.txt](http://natas2.natas.labs.overthewire.org/files/users.txt)! It holds our next flag:

<details>
  <summary>Solution</summary>
  Flag: G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q
</details>