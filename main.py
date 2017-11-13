from essentials.manager import Pallet, Grid, BoxSize, insertBoxs
from control.printer import printHtmlFile, printBoxs, printlayoutEfficiency
from essentials.optimizer import efficiency, deleteRandomBoxs, rank
from fractions import gcd
import numpy as np

# Measured in millimeters
#palletMeasure = (1000, 1200)
#pallet = Pallet(1000/gcd(400, 200), 1200/gcd(400,200))
gridx = 200
gridy = 150

palX = 1000
palY = 1200

def arruma(L, W, l, w):
    mdc = gcd(l,w)
    La = int(L/mdc)
    Wa = int(W/mdc)
    return [La*mdc, Wa*mdc]

a ,b = arruma(palX, palY, gridx, gridy)

pallet = Pallet(a, b)
boxsize = BoxSize(gridx, gridy)

grid = Grid(pallet, boxsize)

print grid.getMdc()

rankingList = list()

# insert box in pallet
#boxs = insertBoxs(pallet, boxsize, grid)

#printBoxs(boxs, onlyQuantity=True)     
#deleteRandomBoxs(boxs, 50)
#printBoxs(boxs, onlyQuantity=True)     

for i in range(10):
    boxs = insertBoxs(pallet, boxsize, grid)
    efficiencyBox = efficiency(pallet, boxsize, boxs)
    rankingList = rank(pallet, boxsize, boxs, rankingList)
    efficiencyBox = 0
    newsBoxs = ''
    efficiencyNewsBox = 0

    for j in range(1000):
        decay = ((1000.0) - j)/(1000.0)
        #decay = 1.00/(j+1)

        randDestroy = np.random.rand() * decay 
        if randDestroy <= 0.10:
            randDestroy = 0.25
        
        newsBoxs = deleteRandomBoxs(boxs, percentual=randDestroy)
       
        if np.random.rand() > 0.5:
            newsBoxs = insertBoxs(pallet, boxsize, grid, listBox=boxs)
        else:
            newsBoxs = insertBoxs(pallet, boxsize, grid)
        
        efficiencyNewsBox = efficiency(pallet, boxsize, newsBoxs)
    
        if efficiencyNewsBox >= efficiencyBox:
            boxs = newsBoxs
            efficiencyBox = efficiencyNewsBox
        
        elif decay < np.random.rand():
            boxs = newsBoxs
            efficiencyBox = efficiencyNewsBox
        
    rankingList = rank(pallet, boxsize, boxs, rankingList)
    #print 'Melhor Configuracao: ',len(rankingList[0][1]),' caixas com' ,rankingList[0][0] ,'% \t|\t',
    #print 'Configuracao atual: ',len(newsBoxs),' caixas com- Eficiencia atual: ', efficiencyBox, '%'

    print 'Melhor Configuracao: ',len(rankingList[0][1]),' caixas \t|\t',
    print 'Configuracao atual: ',len(newsBoxs),' caixas'



# Print datas 
#print 'Eficiencia da Paletizacao: ',efficiency(pallet, boxsize, boxs)
#printlayoutEfficiency(boxsize, grid)



# Generate html layout file
printHtmlFile(pallet, boxsize,rankingList[0][1])
print 'Acesse: file:///home/rodolpho/Projects/pallet_box/paletes.html'
