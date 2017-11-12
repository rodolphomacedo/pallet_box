import numpy as np
from fractions import gcd
from control.inspection import has_intersection_among_pallet_box
from control.inspection import has_any_intersection



class Pallet(object):

    def __init__(self, L, W):
        self.L = np.int(L)
        self.W = np.int(W)

    def L(self):
        return self.L

    def W(self):
        return self.W

    def x0(self):
        return np.array([0, 0])

    def x1(self):
        return np.array([0, self.L])

    def x2(self):
        return np.array([self.W, self.L])

    def x3(self):
        return np.array([self.W, 0])

    def pos(self):
        return np.array([[0, 0], [0, self.L], [self.L, self.W], [0, self.W]])


class BoxSize(object):
    def __init__(self, x, y):
        self.dimX = np.int(x)
        self.dimY = np.int(y)
    
    def getDimX(self):
        return self.dimX

    def getDimY(self):
        return self.dimY


class Grid(object):
    
    def __init__(self, pallet, boxsize):
        self.palletL = pallet.L
        self.palletW = pallet.W
        self.mdcPallet = gcd(pallet.L, pallet.W)
        self.mdcBoxSize  = gcd(boxsize.getDimX(),boxsize.getDimY())
        self.mdc = gcd(self.mdcPallet, self.mdcBoxSize)

    def getMdc(self):
        return self.mdc

    def getGridL(self):
        self.gridL = np.arange(0, self.palletL, self.getMdc())
        return self.gridL

    def getGridW(self):
        self.gridW = np.arange(0, self.palletW, self.getMdc())
        return self.gridW
   
    def getLengthGridW(self):
        self.lengthGridW = np.size(np.arange(0, self.palletW, self.getMdc()))
        return self.lengthGridW

    def getLengthGridL(self):
        self.lengthGridL = np.size(np.arange(0, self.palletL, self.getMdc()))
        return self.lengthGridL





class Box(object):

    def __init__(self, boxsize, grid, orientation=-1):
        
        dim_x = boxsize.getDimX()
        dim_y = boxsize.getDimY()
        
        randL = np.random.randint(0,grid.getLengthGridL())
        randW = np.random.randint(0,grid.getLengthGridW())

        self.l0 = grid.getGridL()[randL]
        self.w0 = grid.getGridW()[randW]

        self.dimX = np.int(dim_x)
        self.dimY = np.int(dim_y)
       
        # Defining the box orientation
        if (orientation != -1):
            self.orientation = np.int(orientation)
        else:
            self.orientation = np.random.randint(0,2)


        if (np.equal(self.orientation, 1)):
            self.x = np.float(dim_x)
            self.y = np.float(dim_y)
        else:
            self.y = np.float(dim_x)
            self.x = np.float(dim_y)

        self.pos = np.array([
                        [self.l0, self.w0],
                        [np.sum([self.l0, self.x]), self.l0],
                        [np.sum([self.l0, self.x]), np.sum([self.w0, self.y])],
                        [self.l0, np.sum([self.w0, self.y])]
                    ])

    def __str__(self):
        return '[%s,%s,%s]' %(self.l0, self.w0, self.orientation)

    def dim_x(self):
        return self.dimX

    def dim_y(self):
        return self.dimY

    def orientation(self):
        return self.orientation
        
    def l(self):
        return self.l0

    def w(self):
        return self.w0

    def pos(self):
        return self.pos[[0]]

    def x0(self):
        return self.pos[0]

    def x1(self):
        return self.pos[1]

    def x2(self):
        return self.pos[2]

    def x3(self):
        return self.pos[3]


def insertBoxs(pallet, boxsize, grid):
    boxs = list()
    for k in range(1500):
        box = Box(boxsize, grid)
        if not has_intersection_among_pallet_box(pallet, box):
            if not has_any_intersection(box, boxs):
                boxs.append(box)
    return boxs
                                        













