#include "palindrome.h"
/**
 * is_palindrome - if a number is a palindrome
 *
 * @n: number
 *
 * Return: 1: palindrome or 0: not a palindrome
 */
int is_palindrome(unsigned long n)
{
	int ct1 = 0, ct2 = 0;
	unsigned long array[1024];
	unsigned long new_n = n;

	while (new_n != 0)
	{
		array[ct1++] = new_n % 10;
		new_n = new_n / 10;
	}

	ct1--;
	for ( ; ct1 > ct2; ct1--, ct2++)
	{
		if (array[ct1] != array[ct2])
			return (0);
	}

	return (1);
}
