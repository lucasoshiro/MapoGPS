#!/usr/bin/env python3

from pointset import *
from coord    import *
from vcoord   import *

import numpy as np

training = [*stations, *museums]

origin = (-23.55039, -46.63395)  # Praça da Sé, km 0 of São Paulo
p_real_delta = [coord_to_meters(origin, p[1]) for p in training]
p_vcoord = [vcoord_from_mapo(*p[0]) for p in training]

r = np.insert(np.array(p_real_delta), 0, 1, 1) # Insert column of ones
v = np.array(p_vcoord)
w = np.linalg.inv(r.T.dot(r)).dot(r.T).dot(v) # Linear Regression

def mapo_from_coord(y, x):
    real_delta = coord_to_meters(origin, (y, x))
    r = np.array([[1, *real_delta]])
    v = r.dot(w)[0]

    return mapo_from_vcoord(*v)

# These next two functions were only used to find the error between the
# predicted and the real page and position of page of the points

def point_error(point):
    e = vcoord_from_mapo(*point[0])
    mapo = mapo_from_coord(*point[1])
    if mapo[0] is None: return False # Point outside the map range
    o = vcoord_from_mapo(*mapo)
    return np.linalg.norm(np.array(o) - np.array(e))

def squared_error(it):
    errors = (point_error(point) for point in it)
    return sum(error ** 2 for error in filter(None, errors)) / len(it)

if __name__ == '__main__':
    while True:
        try:
            c = map(float, input().split(','))
            print(*mapo_from_coord(*c))
        except EOFError:
            exit(0)
        except KeyboardInterrupt:
            exit(0)
        except:
            pass
