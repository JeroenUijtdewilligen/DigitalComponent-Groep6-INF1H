import SpelSpelen, RepeatHulp
import Main_setup as gl

def setup():
    global page
    page = 1
    
def isMouseWithinSpace(x, y, w, h):
    if x < mouseX < x + w and y < mouseY < y + h:
        return True
    else:
        return False
    
def keyPressed():
    global page
    if key == CODED:
        if keyCode == LEFT and page > 1:
            page -= 1
            return scene
        if keyCode == RIGHT and page < 9:
            page += 1
            return scene
        else:
            return scene
    if key == 'd' and page < 9:
        page += 1
        return scene
    if key == 'a' and page > 1:
        page -= 1
        return scene
    if key == '1':
        page = 1
        return scene
    else:
        return scene

def mousePressed():
    global page
    if isMouseWithinSpace(670, 640, 60, 60) and page < 9:
        page += 1
    if isMouseWithinSpace(550, 640, 60, 60) and page > 1:
        page -= 1
    if isMouseWithinSpace(280, 300, 200, 100) and page == 1:
        page = 2
    if isMouseWithinSpace(800, 300, 200, 100) and page == 1:
        page = 7
    if isMouseWithinSpace(20, 650, 50, 50):
        page = 1
    if isMouseWithinSpace(1160, 40, 100, 72) and page >= 2 and page < 7:
        scene = "SpelSpelen"
        SpelSpelen.setup()
        return scene
    if isMouseWithinSpace(1150, 40, 117, 72) and page >= 7 and page < 10:
        scene = "RepeatHulp"
        return scene
    if isMouseWithinSpace(1210, 650, 50, 50):
        scene = "Menu"
        return scene
    else:
        scene = "Handleiding"
        return scene
            
def draw():
    global nextPageArrow, returnArrow, page, font, logo, bitflip0, bitflip1, bitflip2, bitflipX, repeatHulp0, repeatHulp1, repeatHulp2
    stroke(0)
    background(240)
    textFont(gl.font, 35)
    textAlign(CENTER)
    fill(255)
    tint(255)
    strokeWeight(5)
    rect(-10, 620, 1300, 720)

    noTint()
    fill(0)
    text(page, width/ 2, 680)
    noFill()
    
    #Return to Menu
    textSize(40)
    text('M', 1236 , 691)
    if isMouseWithinSpace(1210, 650, 50, 50):
        stroke(150)
    rect(1210, 650, 50, 50)
    stroke(0)
    
    textSize(30)
             
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
        
        textSize(55)
        text('Bitflip', 380, 370)
        text('Tutorial Digitale Component', width/ 2, 120) 
        textSize(40)
        text('Repeat \n Hulp', 900, 340)
        
        image(gl.nextPageArrow, 670, 640, 60, 60)
        
    elif page == 2:
        
        text('Situatie 1', 965, 190)
        text('Een Bitflip vindt om de \n X aantal (seconden/ minuten) plaats. \n\n In Situatie 1 heeft er \n nog geen Bitflip plaatsgevonden. \n\n'
             'Er hoeven in deze situatie \n geen blokjes geplaatsts te worden.', 360, 210)
        image(gl.bitflip0, 780, 200, 380, 380)
        
        
    elif page ==  3:
        
        text('Situatie 2', 965, 190)
        text('In Situatie 2 heeft er wel \n een Bitflip plaatsgevonden. \n\n In deze situatie is er \n een vakje geel gekleurd. \n\n' 
             'Dit gele vakje geeft aan dat \n er een geel blokje, \n op de aangegeven plek, \n op het bord geplaatst moet worden.', 360, 210)
        image(gl.bitflip1, 780, 200, 380, 380)
        
    elif page == 4:
        
        text('Situatie 3', 965, 190)
        text('In Situatie 3 heeft er \n een Bitflip plaatsgevonden. \n\n In deze situatie is er \n een vakje wit gekleurd. \n\n'
             'Dit witte vakje geeft aan dat er, \n op de aangegeven plek, \n op het bord een blokje moet worden verwijderd. \n', 360, 210)
        image(gl.bitflip2, 780, 200, 380, 380)
        
        
    elif page == 5:
        
        text('Situatie 4', 965, 190)
        text('In Situatie 4 hebben er \n acht Bitflips plaatsgevonden. \n\n In deze situatie zijn er twee groene, \n' 
             'twee rode en twee witte vakjes gekleurd, \n verder is er nog een geel en blauw vakje gekleurd. \n\n' 
             'Op de volgende pagina \n staan alle verschillende kleuren met \n de bijbehordende betekenissen beschreven.', 360, 210)
        image(gl.bitflipX, 780, 200, 380, 380)
        
    elif page == 6:
        
        textSize(23)
        text('Er moet een zwart blokje geplaatst worden.', 360, 218) 
        text('Dit heeft hetzelfde effect als de Dead Transistor kaart.', 411, 248)
        text('Er moet een blokje worden verwijderd.', 337, 363)
        text('Er moet een rood blokje geplaatst worden.', 359, 493)
        text('Er moet een geel blokje geplaatst worden.', 970, 232)
        text('Er moet een groen blokje geplaatst worden.', 979, 363)
        text('Er moet een blauw blokje geplaatst worden.', 979, 493)
        fill(0)               #Black
        rect(80, 200, 50, 50)
        fill(255)             #White
        rect(80, 330, 50, 50)
        fill(255, 0, 0)       #Red
        rect(80, 460, 50, 50)
        fill(255,242,0)       #Yellow
        rect(700, 200, 50, 50)
        fill(0, 255, 0)       #Green
        rect(700, 330, 50, 50)
        fill(0, 0, 255)       #Blue
        rect(700, 460, 50, 50)
    
        
    elif page == 7:
        
        textSize(20)
        text('Geeft de  waarde \n van de Repeat kaart \n aan op de 1e plek.', 220, 225)
        text('Geeft de waarde \n van de Repeat kaart \n aan op de 2e plek.', 430, 225)
        text('Geeft de waarde \n van de Repeat kaart \n aan op de 3e plek.', 640, 225)
        text('Geeft de waarde \n van de Draw kaart aan \n die gespeeld is.', 845, 225)
        text('Geeft het aantal \n Blokjes aan die \n geplaatst mogen worden.', 1060, 225)
        textSize(40)
        text('Repeat Hulp', width/ 2, 100)
        image(gl.repeatHulp0, 135, 285, 1000, 320)
        

    elif page == 8:
        
        textSize(20)
        text('Op de 1e plek \n is er een Repeat Kaart \n met de waarde 2.' , 220, 225)
        text('Op de 2e plek \n is er een Repeat Kaart \n met de waarde 1.' , 430, 225)
        text('Op de 3e plek \n is er een Repeat Kaart \n met de waarde 3.' , 640, 225)
        text('De waarde van \n de Draw kaart is \n altijd gelijk aan 1.', 845, 225)
        text('Het aantal blokjes \n dat geplaatst mag worden \n is dus gelijk aan 13.', 1060, 225)
        textSize(40)
        text('Voorbeeld 1', width/ 2, 100)
        image(gl.repeatHulp1, 135, 285, 1000, 320)
        
        
    elif page == 9:
        
        textSize(20)
        text('Op de 1e plek \n is er een Repeat Kaart \n met de waarde 1.' , 220, 225)
        text('Op de 2e plek \n is er een Repeat Kaart \n met de waarde 3.' , 430, 225)
        text('Op de 3e plek \n is er een Repeat Kaart \n met de waarde 1.' , 640, 225)
        text('De waarde van \n de Draw kaart is \n altijd gelijk aan 1.', 845, 225)
        text('Het aantal blokjes \n dat geplaatst mag worden \n is dus gelijk aan 8.', 1060, 225)
        textSize(40)
        text('Voorbeeld 2', width/ 2, 100)
        image(gl.repeatHulp2, 135, 285, 1000, 320)
        image(gl.returnArrow, 550, 640, 60, 60)
        
        
    if page != 1:
        #Return to page 1
        if isMouseWithinSpace(20, 650, 50, 50):
            stroke(150)
        noFill()
        rect(20, 650, 50, 50)
        textSize(20)
        fill(0)
        text('Pag \n 1 ', 47 , 672)
        
        if page >=2 and page < 7:
            textSize(55)
            text('Bitflip', width/ 2, 100)
            textSize(22)
            if isMouseWithinSpace(1160, 40, 100, 72):
                stroke(150)
            fill(255)
            rect(1160, 40, 100, 72)
            fill(0)
            text('  Spel \n Spelen', 1211, 72)
            stroke(0)
            
        if page >= 7 and page < 10:
            textSize(20)
            if isMouseWithinSpace(1150, 40, 117, 72):
                stroke(150)
            fill(255)
            rect(1150, 40, 117, 72)
            fill(0)
            text('  Naar \n Repeat Hulp', 1207, 72)
            stroke(0)
        
    if page != 1 and page != 9:

        image(gl.returnArrow, 550, 640, 60, 60)
        image(gl.nextPageArrow, 670, 640, 60, 60)
