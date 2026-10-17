# Level 09


``` bash
$ ls -la
total 24
dr-x------ 1 level09 level09  140 Mar  5  2016 .
d--x--x--x 1 root    users    340 Aug 30  2015 ..
-r-x------ 1 level09 level09  220 Apr  3  2012 .bash_logout
-r-x------ 1 level09 level09 3518 Aug 30  2015 .bashrc
-r-x------ 1 level09 level09  675 Apr  3  2012 .profile
-rwsr-sr-x 1 flag09  level09 7640 Mar  5  2016 level09
----r--r-- 1 flag09  level09   26 Mar  5  2016 token

$ ./level09 
You need to provied only one arg.

$ ./level09 token 
tpmhr

$ cat token 
f4kmm6p|=�p�n��DB�Du{��

$ ./level09 test
tfuw
```

``` c
#include <unistd.h>

int	main(int ac, char *arg[])
{
	int	i = 0;
	char	c = 0;
	while (arg[1][i]) {
		c = arg[1][i] - i;
		write(1, &c, 1);
		i++;
	}
	write(1, "\n", 1);
	return 0;
}
```

``` bash
$ su flag09
Password: 
Don't forget to launch getflag !
$ getflag
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
```