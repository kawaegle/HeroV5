when we spawn the instance of the chall the chall give us the basic credential

`ssh user@<instance> -p<port>` and the password is password123


`s -la /
total 84
drwxr-xr-x   1 root root 4096 May 14 13:11 .
drwxr-xr-x   1 root root 4096 May 14 13:11 ..
-rwxr-xr-x   1 root root    0 May 14 13:11 .dockerenv
drwxr-xr-x   1 root root 4096 May 12 11:43 bin
drwxr-xr-x   2 root root 4096 Apr  2 11:55 boot
drwxr-xr-x   5 root root  340 May 14 13:11 dev
drwxr-xr-x   1 root root 4096 May 14 13:11 etc
----------   1 user user   40 May 12 11:43 flag.txt
drwxr-xr-x   1 root root 4096 May 12 11:43 home
drwxr-xr-x   1 root root 4096 May 12 11:43 lib
`
we see that the flag.txt is owned by our user but there is no right mod.
let's try to chmod it as the challenge name.
`user@ff93b579540d158579ff3e86c9f6c4fc:~$ chmod +rwx /flag.txt
-bash: /bin/chmod: Permission denied`

so let see why 

`
user@ff93b579540d158579ff3e86c9f6c4fc:~$ ls -la /bin/chmod 
---------- 1 root root 64448 Sep 24  2020 /bin/chmod
`
so we can see that chmod is also rightless.

maybe we can use the kernel system call to get some right.
`
perl -e 'chmod 0755, "/flag.txt"'
`
and if we redo 
`user@ff93b579540d158579ff3e86c9f6c4fc:~$ cat /flag.txt
Hero{chmod_1337_would_have_been_easier}
`
 there is the flag.
