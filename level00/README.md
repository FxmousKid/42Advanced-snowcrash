Le premier niveau est toujours le plus dûr. 

On a pas trop idée de ou l'on veut aller au début, donc on a certaines techniques,
certains vecteurs d'attaque qu'on peut utiliser afin de trouver les premieres pistes
a exploiter.

Typiquement on parle de choses comme :

```bash
# Lister les fichiers
find / -name "*flag00*" 2> /dev/null

# qui suis-je
id
```

Or dans ce niveau là, la subtilité est de chercher les fichiers de certains user,
Generalement une approche comme cella n'est que le début de la piste, mais dans ce
cas c'est plus simple :

```bash
level00@SnowCrash:~$ find / -user flag00 2> /dev/null
/usr/sbin/john
/rofs/usr/sbin/john

```

Boom trouvé 2 fichiers, maintenant voyons ce qu'il contiennent :

```bash
level00@SnowCrash:~$ cat /usr/sbin/john
cdiiddwpgswtgt
level00@SnowCrash:~$ cat /rofs/usr/sbin/john
cdiiddwpgswtgt
```

on peut assumé que c'est le flag mais chiffré, et pour déchiffré
on peut essayer certains classiques, dont le chiffrement césar.

Il éxiste beaucoup de sites qui permettent le déchiffrement 
d'un hash a travers plein d'algo differents, notamment le site code
donc en le passant dedans, on remarque que le résultat avec le
chiffrement de césar est le plus pértinent, et si on essaye :

```bash
su flag00
password: nottoohardhere
getflag
```

On obtient le flag !
