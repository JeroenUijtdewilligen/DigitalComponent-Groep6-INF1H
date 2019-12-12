

import Menu, RepeatHulp, SpelSpelen, functions,time, Handleiding

def setup():
    #setting up some values
    global scene,start
    size(1280, 720)
    
    #setting up the scenes
    scene = "Menu"
    RepeatHulp.setup()
    Menu.setup()
    Handleiding.setup()

def draw():
    global scene
    #determines which scene should be active
    if scene == "Menu":
        Menu.draw()
    elif scene == "RepeatHulp":
        RepeatHulp.draw()
    elif scene == "SpelSpelen":
        SpelSpelen.draw()   
    elif scene == "Handleiding":
        Handleiding.draw() 
        
def mousePressed():
    global scene
    #determines which mousepressed should be active
    if scene == "Menu":
        scene = Menu.mousePressed()
    elif scene == "RepeatHulp":
        scene = RepeatHulp.mousePressed()
    elif scene == "SpelSpelen":
        scene = SpelSpelen.mousePressed()
    elif scene == "Handleiding":
        scene = Handleiding.mousePressed()
