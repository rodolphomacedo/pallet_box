from numpy import random 

def printHtml(pallet, boxsize, boxs):
    
    html = ''

    header = """ 
    <!DOCTYPE html>
    <meta charset="utf-8">

    <body>
    <script src="//d3js.org/d3.v3.min.js"></script>
    <svg width="2000" height="2000">

    """
    pallet = """
    <!-- Insert layout pallet -->
    <rect x="0" y="0" width='%d' height='%d' fill="black" />

    """%(pallet.W, pallet.L)
    
    footer = """  
    </svg> 
     
     </body> 
     </html> 
      
      """ 
    colors = ['red', 'green', 'yellow', 'blue', 'purple', 'magenta', 'aqua','CornflowerBlue','Cyan', 'DarkBlue ', 'DarkCyan', 'DeepPink ', 'Olive' ]
    bodyBoxs = list()

    for box in boxs:
        if box.orientation == 1:
            bodyBoxs.append("""<rect x='%s' y='%s' width='%s' height='%s' fill='%s' />
                    """ %(box.x0()[0], box.x0()[1], boxsize.getDimX(), boxsize.getDimY(), random.choice(colors)))
        else:
            bodyBoxs.append("""<rect x='%s' y='%s' width='%s' height='%s' fill='%s' />
                    """ %(box.x0()[0], box.x0()[1], boxsize.getDimY(), boxsize.getDimX(), random.choice(colors)))
                                            
               

    html = header + pallet
    for bodyBox in bodyBoxs:
        html = html + bodyBox
    html = html + footer

    return html
              
def printHtmlFile(pallet, boxsize, boxs):
    htmlBody = printHtml(pallet, boxsize, boxs)
    
    htmlFile = open('paletes.html', 'w')
    htmlFile.write(htmlBody)
    htmlFile.close



def printBoxs(boxs, onlyQuantity=False):
    i = 0
    if not onlyQuantity:
        for box in boxs:
            i = i + 1
            print '\n+========> Caixa ',i,' <=============+'
            print '|  Orientacao:', box.orientation
            print '|  Ponto x0: ', box.x0()
            print '|  Ponto x1: ', box.x1()
            print '|  Ponto x2: ', box.x2()
            print '|  Ponto x3: ', box.x3()
    else:
        print 'Quantidade de caixas: ', len(boxs)

