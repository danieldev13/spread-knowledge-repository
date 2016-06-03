#include <stdio.h>
#include <stdlib.h>

#include "eratosthenes.h"

int main(void) {
	int number = 100;
	int *result;

	result = eratosthenes(number);

	int c = 0;
	while (1) {
		if (result[c] < 2 || result[c] > number) {
			break;
		}

		printf("Prime number is %d\n", result[c]);
		c++;
	}

	return EXIT_SUCCESS;
}
