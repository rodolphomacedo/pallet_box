import numpy as np

def efficiency(pallet, boxsize, boxs, percentual=False):
    if percentual:
        palletArea = float(pallet.getArea())
        boxArea = float(boxsize.getArea())
        lenBoxs = len(boxs)
        return ((lenBoxs*boxArea)/palletArea)*100
    else:
        return len(boxs)

def deleteRandomBoxs(boxs, percentual=0.0):
    if percentual == 0.0:
        return boxs
    else:
        qtdDelete = int(len(boxs)*percentual)
        for _ in range(qtdDelete):
            if (len(boxs) != 0):
                boxs.pop(np.random.randint(len(boxs)))
            else:
                return boxs 
    return boxs


def rank(pallet, boxsize, boxs, rankingList):
    
    efficiencyBoxs = efficiency(pallet, boxsize, boxs)
    
    rankingList.append([efficiencyBoxs, boxs])
    return sorted(rankingList, key=lambda x: x[0], reverse=True)
