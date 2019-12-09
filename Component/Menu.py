import SpelSpelen, RepeatHulp, Handleiding
def setup():
    global achtergrond, x, y, font, imgboek, scene, imgkaarten, imgrepeat, imglogo
    achtergrond = loadImage("menu/Achtergrond.png")
    imgboek = loadImage("menu/Book.png")
    imgkaarten = loadImage("menu/kaarten.png")
    imgrepeat = loadImage("menu/repeat.png")
    imglogo = loadImage("menu/logo.png")
    font = createFont("couture.otf", 144)

    x = 0
    y = -1280
    scene = "Menu"
    
def draw():
    frameRate(60)
    global achtergrond, x, y, font, scene
    
    #sliding Background
    image(achtergrond, x, 0)
    x -= 1
    if x == -1280:
        x = 0 
    image(imgkaarten, y, 0)
    y += 1
    if y == 0:
        y = -1280
    
    #tekst Bitflip
    stroke(0)
    fill(255)
    rect(25, 50, 580, 150)
    textAlign(LEFT)
    textFont(font)
    fill(0)
    strokeWeight(3)
    stroke(0)
    text("BitFlip!", 40, 175)
    
    fill(255)
    strokeWeight(5)
    stroke(0)
    if 110 < mouseX < 360 and 250 < mouseY < 350:
        stroke(150)
        image(imglogo, 675, 275, 480, 300)
    rect(110, 250, 250, 100)
    
    fill(255)
    strokeWeight(5)
    stroke(0)
    if 110 < mouseX < 360 and 400 < mouseY < 500:
        stroke(150)
        image(imgrepeat, 800, 250)
    rect(110, 400, 250, 100)
    
    fill(255)
    strokeWeight(5)
    stroke(0)
    if 110 < mouseX < 360 and 550 < mouseY < 650:
        stroke(150)
        image(imgboek, 750, 250, 400, 400)
    rect(110, 550, 250, 100)
    
    fill(0)
    textFont(font, 22)
    textAlign(CENTER)
    text("Spel Starten", 235, 310)
    text("Repeat Hulp", 235, 460)
    text("Tutorial", 235, 610)
    
def mousePressed():
    global scene
    if 110 < mouseX < 360 and 250 < mouseY < 350:
        scene = "SpelSpelen"
        SpelSpelen.setup()
        return scene
    elif 110 < mouseX < 360 and 400 < mouseY < 500:
        scene = "RepeatHulp"
        RepeatHulp.setup()
        return scene
    elif 110 < mouseX < 360 and 550 < mouseY < 650:
        scene = "Handleiding"
        Handleiding.setup()
        return scene
    else:
        scene = "Menu"
        return scene
