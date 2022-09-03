<?php

function xor_encrypt($in) {
    $key = 'KNHL';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function forgeCookie($d) {
    return base64_encode(xor_encrypt(json_encode($d)));
}

#Optional: Verify the key is correct
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
$defaultcookie = "MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY=";
echo "Verify key correctness with intercepted Plain/Ciphertext pair: " . ($defaultcookie == forgeCookie($defaultdata) ? "True" : "False") . "\n";

#Forge the challenge cookie
$challenge = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
echo "Forged Cookie: " . forgeCookie($challenge) . "\n";

?>