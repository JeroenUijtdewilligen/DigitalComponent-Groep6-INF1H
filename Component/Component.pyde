import Menu, RepeatHulp

def setup():
    #setting up some values
    global font, scene
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
        
def mousePressed():
    global scene
    if scene == "Menu":
        scene = Menu.mousePressed()
    if scene == "RepeatHulp":
        RepeatHulp.mousePressed()
