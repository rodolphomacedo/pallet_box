import numpy as np
from essentials.manager import Pallet, Box, Grid, BoxSize
from control.inspection import has_intersection_among_pallet_box
#from control.inspection import has_intersection_between_boxs
from control.inspection import has_any_intersection
from control.printer import printHtmlFile, printBoxs
from fractions import gcd


# Measured in millimeters
pallet = Pallet(1000, 1200)
boxsize = BoxSize(300,250)
grid = Grid(pallet, boxsize)

print 'Palete x0: ', pallet.x0()
print 'Palete x1: ', pallet.x1()
print 'Palete x2: ', pallet.x2()
print 'Palete x3: ', pallet.x3()

print '*******************  Dados do Palete  **********************'
print 'Comprimento do Palete: ', pallet.L
print 'Largura do Palete: ', pallet.W
print 'Eficiencia do layout: %3.0f%%' %(np.float(grid.getMdc())/min(boxsize.getDimX(), boxsize.getDimY())*100)
print '\n*******************  Dados do Grid  **********************'
print 'Grade em L: ', grid.getGridL()
print '\n'
print 'Garde em W: ', grid.getGridW()


boxs = list()
for k in range(1500):
    box = Box(boxsize, grid)
    if not has_intersection_among_pallet_box(pallet, box):
        if not has_any_intersection(box, boxs):
            boxs.append(box)

printBoxs(boxs, onlyQuantity=True)     
printHtmlFile(pallet, boxsize, boxs)
