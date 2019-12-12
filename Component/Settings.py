def setup():
    global font, tab, scene
    font = loadFont("ArialMT-48.vlw")
    
    tab = "Controls"
    scene = "Settings"
    
def isMouseWithinSpace(x, y, w, h):
    if x < mouseX < x + w and y < mouseY < y + h:
        return True
    else:
        return False    
    
def mousePressed():
    global tab, scene
    if isMouseWithinSpace(0, 0, 650, 70) and tab == "Extras":
        tab = "Controls"
    
    if isMouseWithinSpace(641, 0, 650, 70) and tab == "Controls":
        tab = "Extras"

    if isMouseWithinSpace(1210, 650, 50, 50):
        scene = "Menu"
        return scene
    else:
        return scene

        
def draw():
    global tab
    background(230)
    textFont(font, 35)
    
    if tab == "Controls":
        fill(255); rect(-10, -12, 650, 70, 17)
        fill(230); rect(640, -12, 650, 70, 17)
        fill(0); text('Algemeen \n Terug naar het menu = M', 650, 200)
        text('Tutorial \n Terug naar de eerste pagina = 1 \n  Volgende pagina = Rechter Pijl \n Vorige pagina = Linker Pijl', 650, 400)
    if tab == "Extras":
        fill(230); rect(-10, -12, 650, 70, 17)
        fill(255); rect(640, -12, 650, 70, 17)
    fill(0)

    text('Controls', 320, 40)
    text('Extras', 960, 40)
    
    noFill()
    if 1210 < mouseX < 1260 and 650 < mouseY < 700:
        stroke(150)
    rect(1210, 650, 50, 50)
    textFont(font); textSize(40)
    fill(0)
    text('M', 1236 , 691)
    stroke(0)
