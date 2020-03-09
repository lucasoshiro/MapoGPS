#!/usr/bin/env python3

from math import cos, sin, pi, sqrt
import numpy as np

def coord_to_meters(origin, dest):
    R = 6371000
    lat_len = 10001965.729

    deg2rad = lambda deg: deg/180 * pi
    mean_deg_len = lambda lat_a, lat_b: ((pi * R / 180) *
                                         (sin(deg2rad(lat_b)) - sin(deg2rad(lat_a))) /
                                         (lat_b - lat_a))
    
    delta = (origin[0] - dest[0], origin[1] - dest[1])

    return (delta[0] * lat_len,
            delta[1] * mean_deg_len(origin[0], dest[0]))

