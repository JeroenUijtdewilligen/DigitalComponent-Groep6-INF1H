import Menu, RepeatHulp

def setup():
    #setting up some values
    global font, scene
    size(1280, 720)
    font = createFont("Couture", 32)
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
        if 110 < mouseX < 360 and 400 < mouseY < 500:
            scene = "RepeatHulp"
    if scene == "RepeatHulp":
        RepeatHulp.mousePressed()
