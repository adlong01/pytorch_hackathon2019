<?php
 // $data=  exec('python C:\Ampps\www\cgi-bin\hello.py');

// /Applications/AMPPS/python/bin/python 

 $data=  exec('python \Applications\Ampps\www\monkeySearch\hello.py');
  echo "File Contain " .  $data;
 ?>