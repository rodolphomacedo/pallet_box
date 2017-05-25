import numpy as np


def has_intersection_among_pallet_box(pallet, box):
    return np.logical_not(np.all(pallet.x2() >= box.x2()))


def has_intersection_between_boxs(box1, box2):

    has_intersection_x = True
    has_intersection_y = True

    # Testing axis x
    if(box1.l0 < box2.l0):
        if(box1.x1()[0] <= box2.x0()[0]):
            has_intersection_x = False

    else:
        if(box2.x1()[0] <= box1.x0()[0]):
            has_intersection_x = False

    # Testing axis y
    if(box1.w0 < box2.w0):
        if(box1.x2()[1] <= box2.x0()[1]):
            has_intersection_y = False

    else:
        if(box2.x2()[1] <= box1.x0()[1]):
            has_intersection_y = False

    return has_intersection_x and has_intersection_y
