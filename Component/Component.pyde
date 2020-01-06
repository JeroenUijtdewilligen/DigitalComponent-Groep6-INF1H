import Menu, RepeatHulp, SpelSpelen, functions,time, Handleiding, Settings
import Main_setup as gl


def setup():
    gl.setup()
    #setting up some values
    size(1280, 720)
    #setting up the scenes
    RepeatHulp.setup()
    Menu.setup()
    Handleiding.setup()
    SpelSpelen.setup()
    Settings.setup()

def draw():
    #determines which scene should be active
    if gl.scene == "Menu":
        Menu.draw()
    elif gl.scene == "RepeatHulp":
        RepeatHulp.draw()
    elif gl.scene == "SpelSpelen":
        SpelSpelen.draw()   
    elif gl.scene == "Handleiding":
        Handleiding.draw() 
    elif gl.scene == "Settings":
        Settings.draw()
        
def mousePressed():

    #determines which mousepressed should be active
    if gl.scene == "Menu":
        gl.scene = Menu.mousePressed()
    elif gl.scene == "RepeatHulp":
        gl.scene = RepeatHulp.mousePressed()
    elif gl.scene == "SpelSpelen":
        gl.scene = SpelSpelen.mousePressed()
    elif gl.scene == "Handleiding":
        gl.scene = Handleiding.mousePressed()
    elif gl.scene == "Settings":
        gl.scene = Settings.mousePressed()
        
def keyPressed():
    if (gl.scene == "RepeatHulp" or gl.scene == "SpelSpelen") and key == 'm':
        gl.scene = "Menu"
    if gl.scene == "Settings":
        gl.scene = Settings.keyPressed()
    if gl.scene == "Handleiding":
        gl.scene = Handleiding.keyPressed()
        
