<?
$cookie_encoded = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFzZ5aAw=";
$cookie_decoded = base64_decode($cookie_encoded);
print($cookie_decoded);

$challenge = array(
    "bgcolor" => "0xaaaaaa",
    "showpassword" => "yes"
);
print("\n\n\n");
print(json_encode("test"));
?>