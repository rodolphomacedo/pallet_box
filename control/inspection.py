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
    elif(box1.orientation == 1):
        has_intersection_x = True
        has_intersection_y = True

        if(box1.l0 < box2.l0):
            if(box1.x1[0] <= box2.x0[0]):
                has_intersection_x = False

        if(box1.w0 < box2.w0):
            if(box1.x2[1] <= box2.x0[1]):
                has_intersection_y = False


