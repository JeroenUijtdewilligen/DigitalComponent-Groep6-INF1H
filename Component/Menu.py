import SpelSpelen, RepeatHulp, Handleiding, Settings
import Main_setup as gl

def setup():
    global x, y
    
    #these are the variables for the location of the moving background
    x = 0
    y = -1280
    
def draw():
    frameRate(60)
    global achtergrond, x, y, font, scene, imgSettings
    
    #sliding Background

    image(gl.achtergrond, x, 0)
    x -= 1
    if x == -1280:
        x = 0 
    image(gl.imgkaarten, y, 0)
    y += 1
    if y == 0:
        y = -1280
    
    #tekst Bitflip
    stroke(0)
    fill(255)
    rect(25, 50, 580, 150)
    textAlign(LEFT)
    textFont(gl.menu_font)
    fill(0)
    strokeWeight(3)
    stroke(0)
    text("BitFlip!", 40, 175)
    
    #buttons
    fill(255)
    strokeWeight(5)
    stroke(0)
    if 110 < mouseX < 360 and 250 < mouseY < 350:
        stroke(150)
        image(gl.imglogo, 675, 275, 480, 300)
    rect(110, 250, 250, 100)
    
    fill(255)
    strokeWeight(5)
    stroke(0)
    if 110 < mouseX < 360 and 400 < mouseY < 500:
        stroke(150)
        image(gl.imgrepeat, 800, 250)
    rect(110, 400, 250, 100)
    
    fill(255)
    strokeWeight(5)
    stroke(0)
    if 110 < mouseX < 360 and 550 < mouseY < 650:
        stroke(150)
        image(gl.imgboek, 750, 250, 400, 400)
    rect(110, 550, 250, 100)
    
    image(gl.imgSettings, 1080, 50, 150, 150)
    
    #text inside buttons
    fill(0)
    textFont(gl.menu_font, 22)
    textAlign(CENTER)
    text("Spel Starten", 235, 310)
    text("Repeat Hulp", 235, 460)
    text("Tutorial", 235, 610)
    
def mousePressed():
    global scene
    #scene selection
    if 110 < mouseX < 360 and 250 < mouseY < 350:
        scene = "SpelSpelen"
        SpelSpelen.draw()
        return scene
    elif 110 < mouseX < 360 and 400 < mouseY < 500:
        scene = "RepeatHulp"
        RepeatHulp.draw()
        return scene
    elif 110 < mouseX < 360 and 550 < mouseY < 650:
        scene = "Handleiding"
        Handleiding.draw()
        return scene
    elif 1080 < mouseX < 1230 and 50 < mouseY < 200:
        scene = "Settings"
        Settings.draw()
        return scene
    else:
        scene = "Menu"
        return scene
