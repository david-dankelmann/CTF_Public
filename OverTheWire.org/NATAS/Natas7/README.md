# Natas Level 7

Access data:

    username: natas7
    password: jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr

Connect to the service using basic HTTP auth by replacing the credentials in the link:
    
    http://*USERNAME*:*FLAG*@*USERNAME*.natas.labs.overthewire.org/

We are given two links to a subpage each that are not thrilling, just displaying text. However, another HTML comment gives us a hint:

    hint: password for webuser natas8 is in /etc/natas_webpass/natas8

Could it be that the implementation just dumps out text files at the path from the GET-Parameter 'page'? Let's [try it](http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8).

Lol, who does this? Flag obtained.


<details>
  <summary>Solution</summary>
  Flag: a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB
</details>