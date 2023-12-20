## list directory
ls <br>
## find troll inside troll
cat troll_<filename> <br>

## delete troll
rm troll_<filename> <br>

## list current directory
pwd <br>

## find hidden troll
ls -al <br>

## show command history
history <br>

## show env
printenv <br>

## head into workshop
cd workshop <br>

## find the troll in one of these files 
grep -ir troll <br>

## run present engine
chmod +x present_engine
./present_engine <br>

## rename blown_fuse0 to fuse0
cd /home/elf/workshop/electrical <br>
mv blown_fuse0 fuse0 <br>

## make a sybolic link
ln -s fuse0 fuse1 <br>

## copy fuse1 to fuse2
cp fuse1 fuse2 <br>

## Add TROLL_REPELLENT into file fuse2
echo "TROLL_REPELLENT" >> fuse2 <br>

## find the troll in /opt/troll_den
cd /opt/troll_den <br>
find . -type f -iname "*troll*" <br>

## find file that is owned by user troll
find . -user troll <br>

## find a file that is greater than 108 kb and less than 110 kb
find . -size +108k -size -110k <br>

## list the running processes to find another troll
ps <br>

## Show only listening ports
netstat -ltnp <br>

## Interact with service listening on port 54321
curl http://localhost:54321 <br>

## kill process
kill 6208 <br>


