import numpy as np
from essentials.manager import Pallet, Box


pallet = Pallet(1000, 1200)
print pallet.L
print pallet.W
print pallet.pos()[2]

print np.inner(pallet.pos()[2], pallet.pos()[1])

box = Box(100.41, 150.30, 10, 15, 1)
print box.w()
print box.pos
print box.x0()
print box.x2()
print box.x3()
