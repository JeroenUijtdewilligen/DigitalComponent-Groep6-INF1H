import Main_setup as gl
def setup():
    global tab
    
    tab = "Controls"
    
def isMouseWithinSpace(x, y, w, h):
    if x < mouseX < x + w and y < mouseY < y + h:
        return True
    else:
        return False    
    
def mousePressed():
    global tab
    if isMouseWithinSpace(0, 0, 650, 70) and tab == "Extras":
        tab = "Controls"
    
    if isMouseWithinSpace(641, 0, 650, 70) and tab == "Controls":
        tab = "Extras"

    if isMouseWithinSpace(1210, 650, 50, 50):
        gl.scene = "Menu"
        return gl.scene
    else:
        return gl.scene

def draw():
    global tab
    background(230)
    textFont(gl.font, 35)
    
    if tab == "Controls":
        fill(255); rect(-10, -12, 650, 70, 17)
        fill(230); rect(640, -12, 650, 70, 17)
        fill(0); text('Algemeen \n\n Terug naar het menu = M', 650, 200)
        text('Tutorial \n\n Terug naar de eerste pagina = 1 \n  Volgende pagina = Rechter Pijl \n Vorige pagina = Linker Pijl', 650, 400)
    if tab == "Extras":
        fill(230); rect(-10, -12, 650, 70, 17)
        fill(255); rect(640, -12, 650, 70, 17)
        #SpelSpelenSettings
        
        fill(0); text("Spelinstellingen", 640, 100)
        
        #Divider
        line(0, 400, 1280, 400)
        #ThemaSettings
        fill(0); text("Themainstellingen", 640, 450)
        
    fill(0)

    text('Controls', 320, 40)
    text('Extras', 960, 40)
    
    noFill()
    if 1210 < mouseX < 1260 and 650 < mouseY < 700:
        stroke(150)
    rect(1210, 650, 50, 50)
    textFont(gl.font); textSize(40)
    fill(0)
    text('M', 1236 , 691)
    stroke(0)
