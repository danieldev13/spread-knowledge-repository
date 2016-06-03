/*
 ============================================================================
 Name        : eratosthenes.c
 Author      : Daniel Torres
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include "eratosthenes.h"

#define LIMIT 10000000

int * eratosthenes(int limit) {
	unsigned long long int i, c;
	int *primes, *numbers;

	numbers = malloc(sizeof(int)*LIMIT);

	for(i = 2; i < limit; i++) {
		numbers[i] = 1;
	}

	for(i = 2; i < limit; i++) {
		if (numbers[i]) {
			for(c = i; i * c < limit; c++) {
				numbers[i * c] = 0;
			}
		}
	}

	int a = 0;
	for(i = 2; i < limit; i++) {
		if(numbers[i]) {
			a++;
		}
	}

	primes = malloc(a);

	a = 0;
	for(i = 2; i < limit; i++) {
		if(numbers[i]) {
			primes[a] = i;
			a++;
		}
	}

	return primes;
}
