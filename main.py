import numpy as np
from essentials.manager import Pallet, Box, Grid, BoxSize
from control.inspection import has_intersection_among_pallet_box
#from control.inspection import has_intersection_between_boxs
from control.inspection import has_any_intersection
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



print '\n*******************  Gerador de Caixa  **********************'
boxs = list()

# Insert first box in pallet
#boxs.append(Box(boxsize, grid))

for k in range(1500):
    box = Box(boxsize, grid)
    if not has_intersection_among_pallet_box(pallet, box):
        if not has_any_intersection(box, boxs):
            boxs.append(box)



colors = ['red', 'green', 'yellow', 'blue', 'purple', 'magenta', 'aqua','CornflowerBlue','Cyan', 'DarkBlue ', 'DarkCyan', 'DeepPink ', 'Olive' ]
#colors = ['red','green','yellow','blue','aqua','CornflowerBlue','Cyan','Olive' ]

bodyBox = list()

i = 0
for box in boxs:
    i = i + 1
    print '\n+========> Caixa ',i,' <=============+'
    #print '| \t', box
    #print 'Comprimento da caixa: ',box.dim_x()
    #print 'Largura da Caixa: ', box.dim_y()
    #print 'Posicao da caixa: \n', box.pos
    print '|  Orientacao:', box.orientation
    print '|  Ponto x0: ', box.x0()
    print '|  Ponto x1: ', box.x1()
    print '|  Ponto x2: ', box.x2()
    print '|  Ponto x3: ', box.x3()
     
    if box.orientation == 1:
        bodyBox.append("<rect x='%s' y='%s' width='%s' height='%s' fill='%s' />" %(box.x0()[0], box.x0()[1], boxsize.getDimX(), boxsize.getDimY(), np.random.choice(colors)))
    else:
        bodyBox.append("<rect x='%s' y='%s' width='%s' height='%s' fill='%s' />" %(box.x0()[0], box.x0()[1], boxsize.getDimY(), boxsize.getDimX(), np.random.choice(colors)))
        
        

head = """
<!DOCTYPE html>
<meta charset="utf-8">

<head>
    <script src="//d3js.org/d3.v3.min.js"></script>
</head>

<body>
<h2>Dados da Paletizacao</h2>


<svg width="2000" height="2000">
<rect x="0" y="0" width="%d" height="%d" fill="Black" />
""" %(pallet.x2()[0], pallet.x2()[1])


footer = """ 
</svg>

</body>
</html>

"""




arquivo = open('paletes.html', 'w')

arquivo.write(head)
for bb in bodyBox:
    arquivo.write(bb)
arquivo.write(footer)

arquivo.close()



