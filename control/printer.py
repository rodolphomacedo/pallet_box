from numpy import random, float64

def printHtml(pallet, boxsize, boxs, progressBar=None):
    
    html = ''

    header = """ 
    <!DOCTYPE html>
    <head> 
        <meta http-equiv="refresh" content="1;URL=file:///home/rodolpho/Projects/pallet_box/paletes.html">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>
    <script src="//d3js.org/d3.v3.min.js"></script>
    </head>

    <body>
    <nav class="navbar navbar-light bg-faded">
        <a class="navbar-brand" href="#">
            <img src="brand.jpg" width="30" height="30" alt="">
            <b>AM-Tech</b>
        </a>
    </nav>
    <div class="container">
    <div class="jumbotron">
        <h1 class="display-2">Pallet Desing</h1>
        <h5><i>Optimization System</i></h5>
    </div>

    """
    if progressBar is not None:
        progressbar = '<b>Optimization Progress</b>: '+ str(int(progressBar))+'% <br/> <div class="progress"> <div class="progress-bar" role="progressbar" style="width:' + str(progressBar) + '%;" aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"></div>  </div>' 
        header = header + progressbar


    header = header + """
    <br /><hr />
    <div class="row">
    <div class="col-md-4">
    <h3>Dashboard:</h3>
    <p><b>Palet size</b>: %s  <i>vs</i>  %s</p>
    <p><b>Box size</b>: %s <i>vs</i> %s</p>
    <hr />
    <p><b>Boxs on the pallet currently</b>: <i>%s</i></p>
    <hr />
    </div>

    <div class="col-md-8">
    <svg align="center" width="1200" height="1200" >
    """%(pallet.L, pallet.W, boxsize.getDimX(), boxsize.getDimY(), len(boxs))


    pallet = """
    <!-- Insert layout pallet -->
    <rect x="0" y="0" width='%d' height='%d' fill="DimGray" rx="10" ry="10" style="stroke: black; stroke-width:5; opacity:1.0" />

    """%(pallet.W +2, pallet.L+2)
    
    footer = """  
    </svg> 
     </div>
     </div>
     </div>
     </body> 
     </html> 
      
      """ 
    #colors = ['red', 'green', 'yellow', 'blue', 'purple', 'magenta', 'aqua','CornflowerBlue','Cyan', 'DarkBlue ', 'DarkCyan', 'DeepPink ', 'Olive' ]
    colors = ['Gainsboro' ]
    bodyBoxs = list()

    for box in boxs:
        if box.orientation == 1:
            bodyBoxs.append("""<rect x='%s' y='%s' width='%s' height='%s' fill='%s' rx="5" ry="5" style="stroke: black; stroke-width:2; opacity:0.95" />
                    """ %(box.x0()[0]+2, box.x0()[1]+1, boxsize.getDimX(), boxsize.getDimY(), random.choice(colors)))
        else:
            bodyBoxs.append("""<rect x='%s' y='%s' width='%s' height='%s' fill='%s' rx="5" ry="5" style="stroke: black; stroke-width:2; opacity:0.95" />
                    """ %(box.x0()[0]+2, box.x0()[1]+1, boxsize.getDimY(), boxsize.getDimX(), random.choice(colors)))
                                            
    html = header + pallet
    for bodyBox in bodyBoxs:
        html = html + bodyBox
    html = html + footer

    return html
              
def printHtmlFile(pallet, boxsize, boxs, progressBar=None):
    htmlBody = printHtml(pallet, boxsize, boxs, progressBar=progressBar)
    
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

def printlayoutEfficiency(boxsize, grid):
    mdc = float64(grid.getMdc())
    minSuport = min(boxsize.getDimX(), boxsize.getDimY())
    print 'Eficiencia do layout: %3.0f%%' %((mdc*100.0) / minSuport)


