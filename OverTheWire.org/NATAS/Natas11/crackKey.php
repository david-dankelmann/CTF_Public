<?php
$cookie_encoded = "MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY="; //Known "Ciphertext"
$cookie_decoded = base64_decode($cookie_encoded); #Remove Base64 Encoding

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff"); 
$defaultdata = json_encode($defaultdata); //This is our known plaintext string

$key = "";
for($i=0; $i<strlen($defaultdata); $i++){
    $key .= $defaultdata[$i] ^ $cookie_decoded[$i]; //XOR Ciphertext + Plaintext reveals the used key (XOR basics)
}
echo "key: " . $key . "\n";

?>