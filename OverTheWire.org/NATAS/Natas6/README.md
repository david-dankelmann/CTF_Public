# Natas Level 6

Access data:

    username: natas6
    password: fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR

Connect to the service using basic HTTP auth by replacing the credentials in the link:
    
    http://*USERNAME*:*FLAG*@*USERNAME*.natas.labs.overthewire.org/

We are given a form field and the source code of the validation:

```php
    <?

    include "includes/secret.inc";

        if(array_key_exists("submit", $_POST)) {
            if($secret == $_POST['secret']) {
            print "Access granted. The password for natas7 is <censored>";
        } else {
            print "Wrong secret";
        }
      }
    ?>
```

Well, a file is included. We should check if we can [access it](http://natas6.natas.labs.overthewire.org/includes/secret.inc).

```php
    <?
    $secret = "FOEIUWGHFEEUHOFUOIU";
    ?>
```

Entering the secret in the form field reveals our next flag.

<details>
  <summary>Solution</summary>
  Flag: jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr
</details>