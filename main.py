from essentials.manager import Pallet, Grid, BoxSize, insertBoxs
from control.printer import printHtmlFile, printBoxs, printlayoutEfficiency
from essentials.optimizer import efficiency, rank, deleteRandomBoxs
from fractions import gcd
import numpy as np

# Measured in millimeters

# Medidas Finni - 26 caixas
#gridx = 240
#gridy = 180
#palX = 1000
#palY = 1200

# Hello world - 15 caixas
#gridx = 400
#gridy = 200
#palX = 1000
#palY = 1200

# Ricieri - 21 caixas
#gridx = 345
#gridy = 160
#palX = 1000
#palY = 1200

# Ricieri - 21 caixas
gridx = 40
gridy = 90
palX = 500
palY = 390


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

#False:= Num of boxs or True:= Filled area
percentualEffi = True


for i in range(1):
    boxs = list()
    
    while len(boxs) == 0:
        boxs = insertBoxs(pallet, boxsize, grid, qtd=1)

    efficiencyBox = efficiency(pallet, boxsize, boxs)
    print 'Quantidade na rodada inicial: ', len(boxs) 
    rankingList = list()

    # ------------ Parameters ---------------
    temp = 20.0
    decay = 0.005
    steps = 50
   
    newBoxs = list()
    bestBoxs = boxs
       
    while (temp >= decay): # Simulated Annealing
        evolution = 100-temp*5.0
        print '\t\t\t\tEvolucao: %2.0f %%' %(evolution)
        efficiencyNewsBox = efficiency(pallet, boxsize, newBoxs, percentual=percentualEffi)
        
        for step in range(steps):
            newBoxs = insertBoxs(pallet, boxsize, grid, qtd=50, listBox=newBoxs)

            if efficiency(pallet, boxsize, newBoxs, percentual=percentualEffi) > efficiencyNewsBox: 
                break
            if step % 15 == 0: # Delete boxs
                newBoxs = deleteRandomBoxs(newBoxs, qtd=1)
        
        efficiencyNewsBox = efficiency(pallet, boxsize, newBoxs, percentual=percentualEffi)
        
        p = min(1,np.exp((efficiencyNewsBox-efficiencyBox)/temp))
        
        #print '\n--------------------------------------------------'    
        #print 'probabilidade: \t', p 

        if efficiencyNewsBox >= efficiencyBox or np.random.rand() < p:
            boxs = newBoxs
            efficiencyBox = efficiency(pallet, boxsize, boxs, percentual=percentualEffi)
            #print 'Probabilidade: ', p
            #print 'Num caixas: ', len(boxs)
        temp = temp - decay
    
        if len(boxs) > len(bestBoxs):
            print 'Trocouuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'
            print 'Eficiencia antiga: ', len(bestBoxs)
            bestBoxs = boxs
            print 'Eficiencia Nova: ', len(bestBoxs)
        print 'Passada: ', i,
        print '\tMax Numero de caixas: ', len(bestBoxs),
        print '\tProbabilidade: %1.3f' %p,
        printHtmlFile(pallet, boxsize,bestBoxs, progressBar=evolution)
        if len(bestBoxs) == 53:
            break
        
        #print 'Max quantidade de caixas: ', len(bestBoxs)
        #printHtmlFile(pallet, boxsize, bestBoxs)
        #print 'Temperatura: \t',temp
        #print 'Eficiencia: \t', efficiencyBox

# Generate html layout file
#rankingFinal = rankingList[0]
print 'Final -> ',
print ' Total de caixas no palete: ', len(bestBoxs)
printHtmlFile(pallet, boxsize,bestBoxs, 100)
print '\n\nAcesse no browser: file:///home/rodolpho/Projects/pallet_box/paletes.html'
