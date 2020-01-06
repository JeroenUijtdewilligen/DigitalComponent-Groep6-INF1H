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
        tab = "Controls"
        return gl.scene
    else:
        return gl.scene
    
def keyPressed():
    global tab
    if key == CODED:
        if keyCode == LEFT and tab == "Extras":
            tab = "Controls"
            return gl.scene
        if keyCode == RIGHT and tab == "Controls":
            tab = "Extras"
            return gl.scene
        else:
            return gl.scene
    if key == 'm':
        gl.scene = "Menu"
        tab = "Controls"
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

        stroke(195)
        line(120, 235, 1160, 235); line(120, 415, 1160, 415)
        line(120, 480, 1160, 480); line(120, 545, 1160, 545)
        stroke(0)
             
        fill(0)
        
        textFont(gl.boldFont, 35); text('Algemeen', 200, 140); text('Tutorial', 180, 320)
        textFont(gl.font, 35)
        
        textSize(25); text('Terug naar het menu', 233, 220)
        text('Volgende pagina', 215, 400)
        text('Vorige pagina', 199, 465)
        text('Terug naar pagina 1', 233, 530)
        
        text('Rechter Pijl of S', 1050, 400)
        text('Linker Pijl of A', 1058, 465)
        textSize(35); text('M', 1120, 220); text('1', 1128, 530)
        
        
        
        
    if tab == "Extras":
        fill(230); rect(-10, -12, 650, 70, 17)
        fill(255); rect(640, -12, 650, 70, 17)
        #SpelSpelenSettings
        
        fill(0); text("Spelintstellingen", 640, 100)
        
        #Divider
        line(0, 400, 1280, 400)
        #ThemaSettings
        fill(0); text("Themaintstellingen", 640, 450)
        
    fill(0)
    textFont(gl.font, 35)
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
