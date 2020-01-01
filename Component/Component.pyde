import Menu, RepeatHulp, SpelSpelen, functions,time, Handleiding
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
