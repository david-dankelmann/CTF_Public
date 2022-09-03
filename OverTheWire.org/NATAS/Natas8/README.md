# Natas Level 8

Access data:

    username: natas8
    password: a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB

Connect to the service using basic HTTP auth by replacing the credentials in the link:
    
    http://*USERNAME*:*FLAG*@*USERNAME*.natas.labs.overthewire.org/

Another form field. We are given the source code again:

```php
    <?
    $encodedSecret = "3d3d516343746d4d6d6c315669563362";

    function encodeSecret($secret) {
        return bin2hex(strrev(base64_encode($secret)));
    }

    if(array_key_exists("submit", $_POST)) {
        if(encodeSecret($_POST['secret']) == $encodedSecret) {
        print "Access granted. The password for natas9 is <censored>";
        } else {
        print "Wrong secret";
        }
    }
    ?>
```

Well, encoding is not encrypting or hashing. We can easily reverse it, just do the operations in the opposite order:

```php
    <?php

    $encodedSecret = "3d3d516343746d4d6d6c315669563362";

    function decodeSecret($secret){
        return base64_decode(strrev(hex2bin($secret)));
    }

    echo decodeSecret($encodedSecret);
    ?>
```

This yields the secret 'oubWYf2kBq' which leads to the flag.

<details>
  <summary>Solution</summary>
  Flag: Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd
</details>