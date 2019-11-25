import SpelSpelen
def setup():
    global achtergrond, x, y, font, imgboek, scene
    achtergrond = loadImage("Achtergrond.png")
    imgboek = loadImage("Book.png")
    font = createFont("couture.otf", 144)

    x = 0
    y = 0
    scene = "Menu"
    
def draw():
    frameRate(60)
    global achtergrond, x, y, font, scene
    
    #sliding Background
    image(achtergrond, x, y)
    x -= 1
    if x == -1280:
        x = 0 
    
    #tekst Bitflip
    textAlign(LEFT)
    textFont(font)
    fill(0)
    strokeWeight(3)
    stroke(0)
    text("BitFlip!", 50, 200)
    
    fill(255)
    strokeWeight(5)
    stroke(0)
    if 110 < mouseX < 360 and 250 < mouseY < 350:
        stroke(150)
    rect(110, 250, 250, 100)
    
    fill(255)
    strokeWeight(5)
    stroke(0)
    if 110 < mouseX < 360 and 400 < mouseY < 500:
        stroke(150)
    rect(110, 400, 250, 100)
    
    fill(255)
    strokeWeight(5)
    stroke(0)
    if 110 < mouseX < 360 and 550 < mouseY < 650:
        stroke(150)
        image(imgboek, 400, 500)
    rect(110, 550, 250, 100)
    
    fill(0)
    textFont(font, 22)
    textAlign(CENTER)
    text("Spel Starten", 235, 310)
    text("Repeat Hulp", 235, 460)
    text("Handleiding", 235, 610)
    
def mousePressed():
    global scene
    if 110 < mouseX < 360 and 250 < mouseY < 350:
        scene = "SpelSpelen"
        SpelSpelen.setup()
        return scene
    elif 110 < mouseX < 360 and 400 < mouseY < 500:
        scene = "RepeatHulp"
        return scene
    elif 110 < mouseX < 360 and 550 < mouseY < 650:
        scene = "Handleiding"
        return scene
    else:
        return scene
