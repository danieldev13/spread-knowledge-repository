#include <stdio.h>
#include <stdlib.h>
#include "haversines.h"

int main(void) {
	printf("!!! Calculating haversines !!!\n");

	Position pos1, pos2;

	pos1.latitude = 45.477825;
	pos1.longitude = -75.692627;
	pos2.latitude = 39.136986;
	pos2.longitude = -121.607841;

	DistanceUnit unit = KILOMETERS;

	double result = distance(pos1, pos2, unit);

	printf("Distance between points is: %.2f %s.", result, (unit == KILOMETERS ? "kilometer(s)" : "mile(s)"));
	getchar();
	return EXIT_SUCCESS;
}
