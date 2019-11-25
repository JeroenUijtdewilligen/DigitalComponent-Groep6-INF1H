
import Menu, RepeatHulp, SpelSpelen, functions, temp,time, Handleiding

def setup():
    #setting up some values
    global scene,start
    size(1280, 720)

    scene = "Menu"
    RepeatHulp.setup()
    Menu.setup()
    Handleiding.setup()
def draw():
    global scene
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
    if scene == "Menu":
        scene = Menu.mousePressed()
    elif scene == "RepeatHulp":
        scene = RepeatHulp.mousePressed()
    elif scene == "SpelSpelen":
        scene = SpelSpelen.mousePressed()
    elif scene == "Handleiding":
        scene = Handleiding.mousePressed()

