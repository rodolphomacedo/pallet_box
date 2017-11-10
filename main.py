import numpy as np
from essentials.manager import Pallet, Box, Grid, BoxSize
from fractions import gcd

pallet = Pallet(800, 900)
boxsize = BoxSize(40,20)
grid = Grid(pallet, boxsize)

print '*******************  Dados do Palete  **********************'
print 'Comprimento do Palete: ', pallet.L
print 'Largura do Palete: ', pallet.W

print '\n*******************  Dados do Grid  **********************'
print 'Grade em L: ', grid.getGridL()
print '\n'
print 'Garde em W: ', grid.getGridW()

print '\n*******************  Dados da Caixa  **********************'
for k in range(10):
    box = Box(boxsize, grid, 1)
    print '\n+========> Caixa ',k+1,'<=============+'
    #print 'Comprimento da caixa: ',box.dim_x()
    #print 'Largura da Caixa: ', box.dim_y()
    #print 'Posicao da caixa: \n', box.pos
    print '|  Ponto x0: ', box.x0()
    print '|  Ponto x1: ', box.x1()
    print '|  Ponto x2: ', box.x2()
    print '|  Ponto x3: ', box.x3()

