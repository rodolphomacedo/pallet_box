import numpy as np


def has_intersection_pallet(pallet, box):
    return np.logical_not(np.all(pallet.x2() >= box.x2()))


def has_intersection_boxs(box1, box2):
    if (box1.orientation, box2.orientation):
        return np.logical_not(np.all(np.absolute(np.subtract(
            box1.pos, box2.pos)) >= np.array([[box1.x, box1.y],
                                              [box1.x, box1.y],
                                              [box1.x, box1.y],
                                              [box1.x, box1.y]])))
