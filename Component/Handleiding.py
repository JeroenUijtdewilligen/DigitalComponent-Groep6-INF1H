
def setup():
    global nextPageArrow, returnArrow, page, font, logo, scene
    
    nextPageArrow = loadImage("nextPageArrow.png")
    returnArrow = loadImage("returnArrow.png")
    logo = loadImage("Logo.jpg")
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

    if isMouseWithinSpace(670, 640, 60, 60) and page < 3:
        page += 1
    if isMouseWithinSpace(550, 640, 60, 60) and page > 1:
        page -= 1
    if isMouseWithinSpace(20, 650, 50, 50):
        scene = "Menu"
    return scene
def draw():
    global nextPageArrow, returnArrow, page, font, logo

    background(255)
    
    textFont(font, 25)
    textAlign(CENTER)
    fill(0)
    text(page, width/ 2, 678)
    strokeWeight(5)
    line(0, 620, width, 622)
    noFill()
    rect(20, 650, 50, 50)
     
    if page == 1:

        image(nextPageArrow, 670, 640, 60, 60)
        image(logo, 0, 0, 1280, 619)
        
    elif page == 2:

        text('Inhoud Spel', width /2, 100)
        text('1 x Speelbord' + '\n' + '60 x Speelkaarten' + '\n' + '15 x Zwarte blokjes' \\
             + '\n' + '40 x Gele blokjes' + '\n' + '40 x Groene blokjes' \\
             + '\n' + '40 x Rode blokjes' + '\n' + '40 x Blauwe blokjes' \\
             + '\n' + '4 x Zakjes', width /2, 200)
        image(returnArrow, 550, 640, 60, 60)
        image(nextPageArrow, 670, 640, 60, 60)
        
        
    elif page == 3:
        image(returnArrow, 550, 640, 60, 60)


        
