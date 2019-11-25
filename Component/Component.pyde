import Menu, RepeatHulp, SpelSpelen, functions, temp,time

def setup():
    #setting up some values
    global scene,start
    size(1280, 720)

    scene = "Menu"
    RepeatHulp.setup()
    Menu.setup()
    
def draw():
    global scene
    if scene == "Menu":
        Menu.draw()
    if scene == "RepeatHulp":
        RepeatHulp.draw()
    if scene == "SpelSpelen":
        SpelSpelen.draw()    
def mousePressed():
    global scene
    if scene == "Menu":
        scene = Menu.mousePressed()
    if scene == "RepeatHulp":
        scene = RepeatHulp.mousePressed()
    if scene == "SpelSpelen":
        scene = SpelSpelen.mousePressed()
