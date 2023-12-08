Read HELP file first for clues <br>
Clue #1 - Hash type is Kerberos 6, etype 23, AS-REP which has id 18200 <br>
Clue #2 - must use limited resources <br>

hashcat -w 1 -u 1 --kernel-accel 1 --kernel-loops 1 hash.txt password_list.txt -m 18200 --force <br>
<br>
Read the top block. The answer is at the very end after the colon <br>
Ouput <br>
$krb5asrep$23$alabaster_snowball@XMAS.LOCAL:22865a2bceeaa73227ea4021879eda02$8f07417379e610e2dcb0621462fec3675bb5a850aba31837d541e50c622dc5faee60e48e019256e466d29b4d8c43cb <br>
f5bf7264b12c21737499cfcb73d95a903005a6ab6d9689ddd2772b908fc0d0aef43bb34db66af1dddb55b64937d3c7d7e93a91a7f303fef96e17d7f5479bae25c0183e74822ac652e92a56d0251bb5d975c2f2b63f4 <br>
458526824f2c3dc1f1fcbacb2f6e52022ba6e6b401660b43b5070409cac0cc6223a2bf1b4b415574d7132f2607e12075f7cd2f8674c33e40d8ed55628f1c3eb08dbb8845b0f3bae708784c805b9a3f4b78ddf6830ad <br>
0e9eafb07980d7f2e270d8dd1966:<THE ANSWER>
