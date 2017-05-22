import numpy as np


class Pallet():

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


class Box():

    def __init__(self, dim_x, dim_y, l0, w0, orientation):
        self.l0 = np.int(l0)
        self.w0 = np.int(w0)
        self.x = np.float(dim_x)
        self.y = np.float(dim_y)
        self.orientation = np.int(orientation)
        self.pos = np.array([
                        [self.l0, self.w0],
                        [np.sum([self.l0, self.x]), self.l0],
                        [np.sum([self.l0, self.x]), np.sum([self.w0, self.y])],
                        [self.l0, np.sum([self.w0, self.y])]
                    ])

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
