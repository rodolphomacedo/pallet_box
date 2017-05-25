from essentials.manager import Box
from essentials.manager import Pallet
from control.inspection import has_intersection_among_pallet_box
from control.inspection import has_intersection_between_boxs

# Objects
p = Pallet(100, 120)
b1 = Box(50, 50, 10, 10, 1)
b2 = Box(50, 50, 80, 80, 1)
b3 = Box(50, 50, 40, 40, 1)

b5 = Box(100, 120, 30, 30, 1)
b6 = Box(100, 120, 80, 75, 2)
b7 = Box(100, 120, 130, 150, 2)


def test_intersection_pallet():
    assert has_intersection_among_pallet_box(p, b2) == True


def test_intersection_box():
    assert has_intersection_between_boxs(b1, b3) == True


def test_no_intersection_box():
    assert has_intersection_between_boxs(b1, b2) == False


def test_orientation_box():
    assert (b5.x == b6.y and b5.y == b6.x) == True


def test_no_intersection_box_unlike_orientation():
    assert has_intersection_between_boxs(b5, b7) == False


def test_intersection_box_unlike_orientation():
    assert has_intersection_between_boxs(b5, b6) == True
