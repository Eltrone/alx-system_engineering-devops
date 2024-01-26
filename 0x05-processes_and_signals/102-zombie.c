#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
* infinite_while - Fonction qui tourne indéfiniment.
*
* Return: Toujours 0.
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
* main - Crée 5 processus zombies.
*
* Return: Toujours 0.
*/
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
		else if (pid == 0)
		{
			exit(0);
		}
		else
		{
			perror("fork");
			return (1);
		}
	}

	infinite_while();

	return (0);
}
