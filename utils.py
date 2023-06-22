import numpy as np


def euclidian_distance(x1,y1,x2,y2):
    return np.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
