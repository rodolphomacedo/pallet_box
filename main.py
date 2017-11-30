from essentials.manager import Pallet, Grid, BoxSize, insertBoxs
from control.printer import printHtmlFile, printBoxs, printlayoutEfficiency
from essentials.optimizer import efficiency, rank, deleteRandomBoxs
from fractions import gcd
import inputs
import numpy as np

# Loading the inputs data 
gridx = inputs.BOX_WIDTH
gridy = inputs.BOX_LENGTH
palX =  inputs.PALLET_WIDTH + inputs.LOOSEN
palY =  inputs.PALLET_LENGTH + inputs.LOOSEN

# Loading the initial parameters 
temp_initial  = inputs.TEMPERATURE_INITIAL 
decay_initial = inputs.DECAY_INITIAL
steps_initial = inputs.STEPS_INITIAL

#False:= Num of boxs or True:= Filled area
percentualEffi = inputs.MODEL_EFFICIENCY


# Aux count
aux_count = 100.0 / temp_initial

def arruma(L, W, l, w):
    mdc = gcd(l,w)
    La = int(L/mdc)
    Wa = int(W/mdc)
    print "La: ", La*mdc
    print "Wa: ", Wa*mdc
    return [La*mdc, Wa*mdc]

if inputs.STANDARDIZE:
    a ,b = arruma(palX, palY, gridx, gridy)
    pallet = Pallet(a, b)
else:
    pallet = Pallet(palX, palY)

boxsize = BoxSize(gridx, gridy)

grid = Grid(pallet, boxsize)

print 'MDC: ', grid.getMdc()


for i in range(inputs.ROUNDS):
    boxs = list()
    
    while len(boxs) == 0:
        boxs = insertBoxs(pallet, boxsize, grid, qtd=1)

    efficiencyBox = efficiency(pallet, boxsize, boxs)
    print 'Quantidade na rodada inicial: ', len(boxs) 
    rankingList = list()

    # ------------ Parameters ---------------
    temp = temp_initial
    decay = decay_initial
    steps = steps_initial
   
    newBoxs = list()
    bestBoxs = boxs
       
    while (temp >= decay): # Simulated Annealing
        evolution = 100.00-temp*aux_count
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
            print 'Eficiencia antiga: ', len(bestBoxs)
            bestBoxs = boxs
            print 'Eficiencia Nova: ', len(bestBoxs)
        print 'Passada: ', i,
        print '\tMax Numero de caixas: ', len(bestBoxs),
        print '\tProbabilidade: %1.3f' %p,
        printHtmlFile(pallet, boxsize,bestBoxs, progressBar=evolution)
        if len(bestBoxs) == inputs.BREAKINGBESTBOXS:
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
