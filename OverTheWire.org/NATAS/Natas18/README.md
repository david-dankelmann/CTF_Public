# Natas Level 18

Access data:

    username: natas18
    password: 8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq


This challenge seems to be about understanding the given source code, however the solution is simple if you know where to look for.

Eventually you'll notice, that you can change the place where the session is created (by sending an invalid (non-numerical) session ID but providing username+password via post). But that doesn't help because no matter what you are doing, admin is always set to zero. 

All the code is not really important for the solution and just distracts. The problem is with the session ID. 

```php
    function createID($user) {
        global $maxid; //constant of 640
        return rand(1, $maxid);
    }
```

It is super weak and capped at 640. We can easily brute-force this by trying to hijack all sessions between 1-640 until we found the admin account. 

You can either code a little script for this like before but i used Burp Intruder for this - creating a payload out of numbers (1-640) for the session ID. You can then observe the length of the server response - at some point you'll receive something slightly larger than the rest. This response contains our flag!

<details>
  <summary>Solution</summary>
  Flag: 8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s
</details>