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