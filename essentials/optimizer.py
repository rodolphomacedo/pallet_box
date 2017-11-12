import numpy as np

def efficiency(pallet, boxsize, boxs):
    palletArea = float(pallet.getArea())
    boxArea = float(boxsize.getArea())
    lenBoxs = len(boxs)
    return ((lenBoxs*boxArea)/palletArea)*100


