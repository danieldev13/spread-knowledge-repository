/*
 ============================================================================
 Name        : haversines.c
 Author      : Daniel Torres
 Version     : 1.0
 Copyright   : Your copyright notice
 Description : Calculation using Haversines formula in C, Ansi-style
 ============================================================================
 */
#include <math.h>
#include "haversines.h"

double distance(Position pos1, Position pos2, DistanceUnit unit){
	double radius = 0;

	if (unit == KILOMETERS) {
		radius = 3960;
	} else {
		radius = 6371;
	}

	double d_lat = to_radians(pos2.latitude - pos1.latitude);
	double d_lon = to_radians(pos2.longitude - pos1.longitude);

	double a = sin(d_lat/2) * sin(d_lat/2) +
			cos(to_radians(pos1.latitude)) * cos(to_radians(pos2.latitude)) *
			sin(d_lon/2) * sin(d_lon/2);
	double c = 2 * asin(sqrt(a));
	double d = radius * c;

	return d;
}

double to_radians(double value){
	return (M_PI /180) * value;
}
