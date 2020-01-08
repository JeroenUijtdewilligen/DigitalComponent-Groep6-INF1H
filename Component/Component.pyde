#Alle nodige bestanden worden ingeladen.
import Menu, RepeatHulp, SpelSpelen, functions,time, Handleiding, Settings
import Main_setup as gl

#Alle setups worden ingeladen en de globale variable worden ingeladen.
def setup():
    gl.setup()
    size(1280, 720)
    RepeatHulp.setup()
    Menu.setup()
    Handleiding.setup()
    SpelSpelen.setup()
    Settings.setup()
    
#determines which scene should be active.    
def draw():
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
        
#determines which mousepressed should be active.
def mousePressed():

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
        
#Checked welke key is ingedrukt en switcht de scene waar nodig. 
def keyPressed():
    if (gl.scene == "RepeatHulp" or gl.scene == "SpelSpelen") and key == 'm':
        gl.scene = "Menu"
    if gl.scene == "Settings":
        gl.scene = Settings.keyPressed()
    if gl.scene == "Handleiding":
        gl.scene = Handleiding.keyPressed()
        
