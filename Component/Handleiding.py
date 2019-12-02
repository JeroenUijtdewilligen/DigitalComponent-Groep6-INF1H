
def setup():
    global nextPageArrow, returnArrow, page, font, scene, bitflip0, bitflip1, bitflip2, bitflipX, repeatHulp0, repeatHulp1, repeatHulp2
    
    nextPageArrow = loadImage("nextPageArrow.png")
    returnArrow = loadImage("returnArrow.png")
    bitflip0 = loadImage("Bitflip0.png")
    bitflip1 = loadImage("Bitflip1.png")
    bitflip2 = loadImage("Bitflip2.png")
    bitflipX = loadImage("BitflipX.png")
    repeatHulp0 = loadImage("repeatHulp0.png")
    repeatHulp1 = loadImage("repeatHulp1.png")
    repeatHulp2 = loadImage("repeatHulp2.png")
    font = loadFont("ArialMT-48.vlw")
    page = 1
    scene = "Handleiding"
    
def isMouseWithinSpace(x, y, w, h):
    if x < mouseX < x + w and y < mouseY < y + h:
        return True
    else:
        return False
    

def mousePressed():
    global page, scene

    if isMouseWithinSpace(670, 640, 60, 60) and page < 6:
        page += 1
    if isMouseWithinSpace(550, 640, 60, 60) and page > 1:
        page -= 1
    if isMouseWithinSpace(280, 300, 200, 100) and page == 1:
        page = 2
    if isMouseWithinSpace(800, 300, 200, 100) and page == 1:
        page = 4
    if isMouseWithinSpace(1210, 650, 50, 50):
        page = 1
    if isMouseWithinSpace(20, 650, 50, 50):
        scene = "Menu"
        return scene
    else:
        return scene


def draw():
    global nextPageArrow, returnArrow, page, font, logo, bitflip0, bitflip1, bitflip2, bitflipX, repeatHulp0, repeatHulp1, repeatHulp2
    stroke(0)
    background(240)
    
    textFont(font, 25)
    textAlign(CENTER)
    fill(0)
    text(page, width/ 2, 678)
    strokeWeight(5)
    line(0, 620, width, 622)
    noFill()
    
    textSize(40)
    text('M', 47 , 690)
    if isMouseWithinSpace(20, 650, 50, 50):
        stroke(150)
    rect(20, 650, 50, 50)
    stroke(0)

    if page == 1:
        fill(255)
        if isMouseWithinSpace(280, 300, 200, 100):
            stroke(150)
        rect(280, 300, 200, 100)
        stroke(0)
        if  isMouseWithinSpace(800, 300, 200, 100):
            stroke(150)
        rect(800, 300, 200, 100)
        fill(0)
        textSize(50)
        text('Bitflip', 380, 370)
        text('Tutorial Digitale Component', width/ 2, 120) 
        textSize(40)
        text('Repeat'+ '\n' + 'Hulp', 900, 340)
        
        image(nextPageArrow, 670, 640, 60, 60)
        
    elif page == 2:
        
        textSize(25)
        text('Situatie voor de eerste Bitflip', 250, 580)
        text('Situatie na de eerste Bitflip', 1050, 580)
        textSize(50)
        text('Bitflip', width/ 2, 100)
        image(bitflip0, 100, 250, 300, 300)
        image(bitflip1, 900, 250, 300, 300)
        
    elif page == 3:
        
        textSize(25)
        text('Situatie na de tweede Bitflip', 250, 580)
        text('Situatie na acht Bitflips', 1050, 580)
        image(bitflip2, 100, 250, 300, 300)
        image(bitflipX, 900, 250, 300, 300)
        textSize(50)
        text('Bitflip', width/ 2, 100)
        
    elif page == 4:
        
        textSize(40)
        text('Repeat Hulp', width/ 2, 100)
        textSize(20)
        text('Geeft de  waarde' + '\n' + 'van de Repeat kaart' + '\n' + 'aan op de 1e plek', 220, 225)
        text('Geeft de waarde' + '\n' + 'van de Repeat kaart' + '\n' + 'aan op de 2e plek', 430, 225)
        text('Geeft de waarde' + '\n' + 'van de Repeat kaart' + '\n' + 'aan op de 3e plek', 640, 225)
        text('Geeft de waarde' + '\n' + 'van de Draw kaart aan' + '\n' + 'die gespeeld is', 845, 225)
        text('Geeft het aantal' + '\n' + 'Blokjes aan die' + '\n' + 'geplaatst mogen worden', 1060, 225)
        image(repeatHulp0, 135, 285, 1000, 320)

    elif page == 5:
        textSize(20)
        text('Op de 1e plek' + '\n' 'is er een Repeat Kaart' + '\n' + 'met de waarde 2' , 220, 225)
        text('Op de 2e plek' + '\n' 'is er een Repeat Kaart' + '\n' + 'met de waarde 1' , 430, 225)
        text('Op de 3e plek' + '\n' + 'is er een Repeat Kaart' + '\n' + 'met de waarde 3' , 640, 225)
        text('De waarde van' + '\n' + 'de Draw kaart is' + '\n' 'altijd gelijk aan 1', 845, 225)
        text('Het aantal blokjes' + '\n' + 'dat geplaatst mag worden' + '\n' + 'is dus gelijk aan 13', 1060, 225)
        textSize(40)
        text('Voorbeeld 1', width/ 2, 100)
        image(repeatHulp1, 135, 285, 1000, 320)
        
    elif page == 6:
        textSize(20)
        text('Op de 1e plek' + '\n' 'is er een Repeat Kaart' + '\n' + 'met de waarde 1' , 220, 225)
        text('Op de 2e plek' + '\n' 'is er een Repeat Kaart' + '\n' + 'met de waarde 3' , 430, 225)
        text('Op de 3e plek' + '\n' + 'is er een Repeat Kaart' + '\n' + 'met de waarde 1' , 640, 225)
        text('De waarde van' + '\n' + 'de Draw kaart is' + '\n' 'altijd gelijk aan 1', 845, 225)
        text('Het aantal blokjes' + '\n' + 'dat geplaatst mag worden' + '\n' + 'is dus gelijk aan 8', 1060, 225)
        textSize(40)
        text('Voorbeeld 2', width/ 2, 100)
        image(repeatHulp2, 135, 285, 1000, 320)
        image(returnArrow, 550, 640, 60, 60)
        
    if page != 1:
        if isMouseWithinSpace(1210, 650, 50, 50):
            stroke(150)
        rect(1210, 650, 50, 50)
        textSize(40)
        text('1', 1236 , 690)
        
    if page != 1 and page != 6:
        image(returnArrow, 550, 640, 60, 60)
        image(nextPageArrow, 670, 640, 60, 60)

        
