from ezgraphics import GraphicsWindow
win=GraphicsWindow()
canvas=win.canvas()

def scacchiera():
    """
    disegna la scacchiera con quadrati
    """
    x=0
    y=0
    canvas.setOutline("red")
    for _ in range(15):
        for _ in range (20):
            canvas.drawRectangle(x,y,20,20)
            x+=20
        x=0
        y+=20

def pulsanti():
    """
    disegna i pulsanti
    """
    x=0
    canvas.setOutline("black")
    for _ in range(4):
        canvas.drawRectangle(x,301,99.75,98)
        x+=99.75
    canvas.drawText(35,335,"Step")
    canvas.drawText(135,335,"Clear")
    canvas.drawText(235,335,"Glider")
    canvas.drawText(335,335,"Quit")

def matrice(l):
    """
    genera la matrice associata alla griglia di quadratini mettendoli tutti a zero cioè bianco
    """
    for i in range(15):
        l.append([])
        for _ in range(20):
            l[i].append(0)
    return l

def cambia_stato():
    """
    cambia lo stato della cella cliccata da nero a bianco e viceversa aggiornando la matrice associata
    """
    for i in range(15):
        for j in range (20):
            if 20*j<x<20*j+20 and 20*i<y<20*i+20:
                canvas.setColor("red")
                canvas.drawRectangle(j*20,i*20,20,20)
                if l[i][j]==0:
                    l[i][j]=1
                    canvas.setFill("black")
                    canvas.drawRectangle(j*20,i*20,20,20)
                elif l[i][j]==1:
                    l[i][j]=0
                    canvas.setFill("white")
                    canvas.drawRectangle(j*20,i*20,20,20)

def clear():
    """
    mette tutti i quadratini della griglia a bianco e tutti gli elementi della matrice a zero
    """
    for i in range(15):
        for j in range (20):
            l[i][j]=0

    for i in range(15):
        for j in range (20):
            canvas.setColor("red")
            canvas.drawRectangle(j*20,i*20,20,20)
            canvas.setFill("white")
            canvas.drawRectangle(j*20,i*20,20,20)

def nero(i,j):
    """
    colora la cella alla posizione i j di nero e ritorna il nuovo valore della matrice in i j
    """
    canvas.setColor("red")
    canvas.drawRectangle(j*20,i*20,20,20)
    canvas.setFill("black")
    canvas.drawRectangle(j*20,i*20,20,20)
    return 1

def bianco(i,j):
    """
    colora la cella alla posizione i j di bianco e ritorna il nuovo valore della matrice in i j
    """
    canvas.setColor("red")
    canvas.drawRectangle(j*20,i*20,20,20)
    canvas.setFill("white")
    canvas.drawRectangle(j*20,i*20,20,20)
    return 0

def glinder():
    """
    crea la figura glinder
    """
    for i in range(15):
        for j in range (20):
            if i==6 and j==8:
                l[i][j]=nero(i,j)
            if i==7 and j==9:
                l[i][j]=nero(i,j)
            if i==7 and j==10:
                l[i][j]=nero(i,j)
            if i==6 and j==10:
                l[i][j]=nero(i,j)
            if i==5 and j==10:
                l[i][j]=nero(i,j)

def adiacenti(i,j):
    """
    calcola quante celle vive ci sono adiacenti a quella i j passata per parametro
    facendo attenzione che la lista di liste non esca dal suo range
    """
    adiacenti=0
    if 0<j<19 and l[i][j-1]==1:
        adiacenti+=1
    if 0<j<19 and 0<i<14 and l[i+1][j-1]==1:
        adiacenti+=1
    if 0<i<14 and l[i+1][j]==1:
        adiacenti+=1
    if 0<j<19 and 0<i<14 and l[i+1][j+1]==1:
        adiacenti+=1
    if 0<j<19 and l[i][j+1]==1:
        adiacenti+=1
    if  0<i<14 and 0<j<19  and l[i-1][j+1]==1:
        adiacenti+=1
    if 0<i<14 and l[i-1][j]==1:
        adiacenti+=1
    if  0<i<14 and 0<j<19  and l[i-1][j-1]==1:
        adiacenti+=1
    return adiacenti

def regola1(i,j):
    """
    applica la regola 1
    """
    a=adiacenti(i,j)
    if a<2:
        m[i][j]=bianco(i,j)

def regola2(i,j):
    """
    applica la regola 2
    """
    a=adiacenti(i,j)
    if a==2 or a==3:
        m[i][j]=nero(i,j)

def regola3(i,j):
    """
    applica la regola 3
    """
    a=adiacenti(i,j)
    if a>3:
        m[i][j]=bianco(i,j)

def regola4(i,j):
    """
    applica la regola 4
    """
    a=adiacenti(i,j)
    if a==3:
        m[i][j]=nero(i,j)

def step():
    """
    applica le quattro regole
    """
    for i in range(15):
        for j in range (20):
            if l[i][j]==1:
                regola1(i,j)
                regola2(i,j)
                regola3(i,j)
            if l[i][j]==0:
                regola4(i,j)

def aggiorna_m():
    """
    aggiorna la matrice temporanea m che serve per applicare le regole di step
    """
    for i in range(15):
        for j in range (20):
            m[i][j]=l[i][j]

def aggiorna_l():
    """
    aggiorna la matrice l con la quale lavorano le altre funzioni
    """
    for i in range(15):
        for j in range (20):
            l[i][j]=m[i][j]

scacchiera()
pulsanti()
#matrice associata alla scacchiera
l=matrice([])
#matrice provvisoria per step
m=matrice([])

#corpo del gioco
fine=False
while not fine:
    x,y=win.getMouse()

    cambia_stato()

    #tasto step
    if 0<x<99 and 301<y<399:
        aggiorna_m()    
        step()
        aggiorna_l()

    #tasto clear
    if 99.75<x<199 and 301<y<399:   
        clear()

    #tasto glider
    if 199.75<x<299 and 301<y<399:  
        glinder()

    #tasto quit
    if 299.75<x<399 and 301<y<399:  
        fine=True

win.close()