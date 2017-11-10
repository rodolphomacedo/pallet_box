import numpy as np


def has_intersection_among_pallet_box(pallet, box):
    #print 'Palete: ',pallet.x2()
    #print 'Caixa: ',box.x2()
    # On Width - axis X
    test0x = pallet.x0()[0] <= box.x0()[0]
    test1x = pallet.x1()[0] <= box.x1()[0]
    test2x = pallet.x2()[0] >= box.x2()[0]
    test3x = pallet.x3()[0] >= box.x3()[0]
    
    #print '\n************* Nova Caixa *****************'
    #print '\n------'
    #print 'Palete x0: ', pallet.x0()[0], '   Box0: ',box.x0()[0],' Teste:', test0x
    #print 'Palete x1: ', pallet.x1()[0], '   Box1: ',box.x1()[0],' Teste:', test1x
    #print 'Palete x2: ', pallet.x2()[0], '   Box1: ',box.x2()[0],' Teste:', test2x
    #print 'Palete x3: ', pallet.x3()[0], '   Box1: ',box.x3()[0],' Teste:', test3x


    
    if not (test0x and test1x and test2x and test3x):
        return True
    #else:
        #print '============================================='
        #print 'Teste 0 -X: ',test0x
        #print 'Teste 1 -X: ',test1x
        #print 'Teste 2 -X: ',test2x
        #print 'Teste 3 -X: ',test3x


    # On Width - axis Y
    test0y = pallet.x0()[1] <= box.x0()[1]
    test1y = pallet.x1()[1] >= box.x1()[1]
    test2y = pallet.x2()[1] >= box.x2()[1]
    test3y = pallet.x3()[1] <= box.x3()[1]
    
    #print '\n------'
    #print 'Palete y0: ', pallet.x0()[1], '   Box0: ',box.x0()[1],' Teste:', test0y
    #print 'Palete y1: ', pallet.x1()[1], '   Box1: ',box.x1()[1],' Teste:', test1y
    #print 'Palete y2: ', pallet.x2()[1], '   Box1: ',box.x2()[1],' Teste:', test2y
    #print 'Palete y3: ', pallet.x3()[1], '   Box1: ',box.x3()[1],' Teste:', test3y


    if not (test0y and test1y and test2y and test3y):
        return True
    #else:
       # print 'Teste 0 -Y: ',test0y
        #print 'Teste 1 -Y: ',test1y
        #print 'Teste 2 -Y: ',test2y
        #print 'Teste 3 -Y: ',test3y
        #print '=============================================\n\n'


    return False

def has_intersection_between_boxs(box1, box2):

    has_intersection_x = True
    has_intersection_y = True

    # Testing axis x
    if(box1.l0 < box2.l0):
        if(box1.x1()[0] <= box2.x0()[0]):
            has_intersection_x = False

    else:
        if(box2.x1()[0] <= box1.x0()[0]):
            has_intersection_x = False

    # Testing axis y
    if(box1.w0 < box2.w0):
        if(box1.x2()[1] <= box2.x0()[1]):
            has_intersection_y = False

    else:
        if(box2.x2()[1] <= box1.x0()[1]):
            has_intersection_y = False

    return has_intersection_x and has_intersection_y

def has_any_intersection(box, boxList):
    
    has_intersection = False
    
    for boxItem in boxList:
        has_intersection = has_intersection_between_boxs(box, boxItem) 
        if has_intersection:
            return True

   # return False 
