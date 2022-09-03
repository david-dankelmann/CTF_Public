# Natas Level 3

Access data:

    username: natas3
    password: G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q

Connect to the service using basic HTTP auth by replacing the credentials in the link:
    
    http://*USERNAME*:*FLAG*@*USERNAME*.natas.labs.overthewire.org/


We are only given a HTML comment: 

    No more information leaks!! Not even Google will find it this time...

Google is a search engine. It uses so called _crawlers_ to search the web. You actually tell these crawlers what to do by defining rules with a "robots.txt" that should be placed at the root directory of your website. Let's check it [out](http://natas3.natas.labs.overthewire.org/robots.txt). 

  User-agent: *
  Disallow: /s3cr3t/

There is a rule defined: disallow crawling the subfolder [/s3cr3t](http://natas3.natas.labs.overthewire.org/s3cr3t). We can find another users.txt here. 

<details>
  <summary>Solution</summary>
  Flag: tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm
</details>