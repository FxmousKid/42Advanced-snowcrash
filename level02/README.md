# Level 02

On refait les memes manip de bases, mais un seul résultat
m'attire : 

```bash
$ ls -la
total 24
dr-x------ 1 level02 level02  120 Mar  5  2016 .
d--x--x--x 1 root    users    340 Aug 30  2015 ..
-r-x------ 1 level02 level02  220 Apr  3  2012 .bash_logout
-r-x------ 1 level02 level02 3518 Aug 30  2015 .bashrc
-r-x------ 1 level02 level02  675 Apr  3  2012 .profile
----r--r-- 1 flag02  level02 8302 Aug 30  2015 level02.pcap
```

Un fichier `.pcap` ! je m'y connais un peu donc je sais que c'est 
un fichier de capture de packets réseaux (Packet CAPture).

Qui dit capture de packets, dit 'wireshark', le programme le plus
connu pour ca.

Ouvrons Wireshark (app GUI), et si clique sur on analyse le flux TCP :


On retrouve cette chaine de caractere :
`ft_wandr...NDRel.L0L`

Le 1ere instint quand on est pas sûre en CTF, est de directement
verifier, donc si on test directement cette string comme mot de passe
on remarque que sa ne passe pas, visuellement on remarque que les 
'.' sont 'bizzare', donc si on les passes sous ASCII, on voit 
que chaque point est en faite un ASCII 'DEL' (7f, 127), donc si
on applique le DEL on obtient : `ft_waNDReL0L`

Or il s'avere que c'est le code !
