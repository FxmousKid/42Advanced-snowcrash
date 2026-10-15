# Level 01

On va essayer les memes primitives que dans le level00 :

```bash
$ id
level01@SnowCrash:~$ id
uid=2001(level01) gid=2001(level01) groups=2001(level01),100(users)

$ pwd
/home/user/level01

$ ls -la
total 12
dr-x------ 1 level01 level01  100 Mar  5  2016 .
d--x--x--x 1 root    users    340 Aug 30  2015 ..
-r-x------ 1 level01 level01  220 Apr  3  2012 .bash_logout
-r-x------ 1 level01 level01 3518 Aug 30  2015 .bashrc
-r-x------ 1 level01 level01  675 Apr  3  2012 .profile

$ find / -user level01 2> /dev/null
(rien dinteressant)

$ find / -user flag01 2> /dev/null
(rien dinteressant)
```

rien d'interessant en gros, cela veut dire qu'on doit etre unpeu
créatif que ça...

Sur Linux, le dossier /etc ('êtsi') est un dossier spécial a la racine
du filesystem qui stock des infos sur le user et ses configurations,
notamment des info sensible sur les users d'une machine, dans 
`/etc/passwd`

```bash
$ cat /etc/passwd

...
flag00:x:3000:3000::/home/flag/flag00:/bin/bash
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
flag02:x:3002:3002::/home/flag/flag02:/bin/bash
...
```

wow. voila quelquechose ! on peut assez vite reconnaitre le fait 
que cette chaine de caractere n'est pas un flag, mais un hash,
donc on peux essayer dcode.fr, mais perso je n'ai pas eu de succés
avec ce hash, donc il faut déployer les grand moyens :

Welcome `John the Ripper` , un programme ultra connue pour 
déchiffré des mots de passe.

On peut dockerisé une machine Kali avec l'éxécutable deja installé
de `john` et en mettant le hash dans un fichier :

```bash
$ john --show < <(echo -n "42hDRfypTqqnw")
cdefg
```

et voila on refait la meme manipulation a la fin du level01 et 
on `getflag`, et voila !


