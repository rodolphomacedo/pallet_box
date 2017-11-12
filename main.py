import numpy as np
from essentials.manager import Pallet, Box, Grid, BoxSize, insertBoxs
from control.printer import printHtmlFile, printBoxs, printlayoutEfficiency
from essentials.optimizer import efficiency
from fractions import gcd


# Measured in millimeters
pallet = Pallet(1000, 1200)
boxsize = BoxSize(300,250)
grid = Grid(pallet, boxsize)

boxs = insertBoxs(pallet, boxsize, grid)
printBoxs(boxs, onlyQuantity=True)     
printHtmlFile(pallet, boxsize, boxs)
print 'Eficiencia da Paletizacao: ',efficiency(pallet, boxsize, boxs)
printlayoutEfficiency(boxsize, grid)
