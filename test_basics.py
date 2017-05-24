from essentials.manager import Box
from essentials.manager import Pallet
from control.inspection import has_intersection_pallet
from control.inspection import has_intersection_boxs

# Objects
p = Pallet(100, 120)
b1 = Box(50, 50, 10, 10, 1)
b2 = Box(50, 50, 80, 80, 1)
b3 = Box(50, 50, 40, 40, 1)


def test_intersection_pallet():
    assert has_intersection_pallet(p, b2) == True


def test_intersection_box():
    assert has_intersection_boxs(b1, b3) == True


def test_no_intersection_box():
    assert has_intersection_boxs(b1, b2) == False
