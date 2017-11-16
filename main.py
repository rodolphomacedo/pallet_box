from essentials.manager import Pallet, Grid, BoxSize, insertBoxs
from control.printer import printHtmlFile, printBoxs, printlayoutEfficiency
from essentials.optimizer import efficiency, rank, deleteRandomBoxs
from fractions import gcd
import numpy as np

# Measured in millimeters
gridx = 240
gridy = 180

#gridx = 400
#gridy = 200

palX = 1000
palY = 1200

def arruma(L, W, l, w):
    mdc = gcd(l,w)
    La = int(L/mdc)
    Wa = int(W/mdc)
    print "La: ", La*mdc
    print "Wa: ", Wa*mdc
    return [La*mdc, Wa*mdc]

a ,b = arruma(palX, palY, gridx, gridy)
#pallet = Pallet(a, b)

pallet = Pallet(palX, palY)

boxsize = BoxSize(gridx, gridy)

grid = Grid(pallet, boxsize)

print 'MDC: ', grid.getMdc()

rankingList = list()

boxs = list()

for i in range(1):
    while len(boxs) == 0:
        boxs = insertBoxs(pallet, boxsize, grid, qtd=1)

    efficiencyBox = efficiency(pallet, boxsize, boxs)
    print 'Quantidade na rodada inicial: ', len(boxs) 
    newBoxs = list()
    bestBoxs = boxs
    temp = 1000.0
    decay = 0.5
    steps = 50
    percentualEffi = False
    #for j in range(500):
    while (temp >= 1):

        efficiencyNewsBox = efficiency(pallet, boxsize, newBoxs, percentual=percentualEffi)
        for step in range(steps):
            newBoxs = insertBoxs(pallet, boxsize, grid, qtd=5, listBox=newBoxs)

            if efficiency(pallet, boxsize, newBoxs, percentual=percentualEffi) > efficiencyNewsBox: 
                break
            if step % 15 == 0:
                #newBoxs = deleteRandomBoxs(newBoxs, percentual=0.120*np.random.rand())
                newBoxs = deleteRandomBoxs(newBoxs, qtd=1)
        
        efficiencyNewsBox = efficiency(pallet, boxsize, newBoxs, percentual=percentualEffi)
       
        p = np.exp((efficiencyNewsBox-efficiencyBox)/temp)
        print '--------------------------------------------------'
        print 'probabilidade: \t', p 
        if efficiencyNewsBox > efficiencyBox or np.random.rand() < p:
            boxs = newBoxs
            efficiencyBox = efficiencyNewsBox

        
        temp = temp - decay
    
        if efficiency(pallet, boxsize, boxs, percentual=percentualEffi) > efficiency(pallet, boxsize, bestBoxs, percentual=percentualEffi):
            bestBox = boxs
            rankingList = rank(pallet, boxsize, boxs, rankingList)
        
            print 'Max quantidade de caixas: ', rankingList[0][0]
            printHtmlFile(pallet, boxsize, bestBox)
            print 'Temperatura: \t',temp
            print 'Eficiencia: \t', efficiency(pallet, boxsize, boxs, percentual=percentualEffi) 

# Generate html layout file
rankingFinal = rankingList[0]
print 'Final: ', rankingFinal
print '\nTotal de caixas no palete: ', rankingFinal[0]
printHtmlFile(pallet, boxsize,rankingFinal[1])
print '\n\nAcesse no browser: file:///home/rodolpho/Projects/pallet_box/paletes.html'
