#alle libarys worden ingeladen
import Main_setup as gl
import functions as f
import time
import Handleiding

def setup():

    global i, j,font,square_size,start
    font = createFont("Arial", 32)
    textFont(font)
    strokeWeight(5)
    i = 250
    j = 150
    square_size = 50
    
def draw():
    frameRate(1)
    global i, j,font,square_size,start, thema,c_time
    
    textFont(gl.font)
    background(230)
    fill(230)
    strokeWeight(5)
    stroke(0)
    
    image(gl.thema, 0, 100)
    
    square(210, 380, 40)
    square(480, 110, 40)
    square(750, 380, 40)
    square(480, 650, 40)
    
    image(gl.p2, 210, 380, 40, 40)
    image(gl.p3, 480, 110, 40, 40)
    image(gl.p4, 750, 380, 40, 40)
    image(gl.p1, 480, 650, 40, 40)

    #er word gekeken of de timer op pause staat zo nee blijft de timer door lopen zo ja word de timer op 0 gezet (pauze)
    c_time = int(f.timer(gl.start)) - int(gl.rest)
    fill(0)
    text(str(f.time_convert(c_time)), 500, 70)
    strokeWeight(5)
    line(0, 100, 1280, 100)
    noFill()
    if 1210 < mouseX < 1260 and 650 < mouseY < 700:
        stroke(150)
    fill(255)
    rect(1210, 650, 50, 50)
    stroke(0)
    fill(0)
    textSize(40)
    text('M', 1236 , 691)
    noFill()
    textSize(32)
    f.draw(i, j, square_size)

    textFont(font)
    textAlign(CENTER)
    #er word gekeken of er tijd is voor een event         
    if gl.bit:
        for coords in gl.bit:
          g = coords.split("-")
          fill(int(g[2]),int(g[3]),int(g[4]))
          stroke(0)
          square(int(g[0]), int(g[1]), 50)
    check_time()        
    
    gl.obj["siege"][0]
    #Help/ Tutorial box
    if 1160 < mouseX < 1260 and 40 < mouseY < 90:
        stroke(150)
    fill(255)
    rect(1160, 25, 100, 50)
    fill(0)
    textSize(40)
    text('Help', 1211, 64)
    stroke(0)
        
def check_time():
    global c_time
    if c_time in gl.event_times:
        fill(0)
        gl.bitflip_sound.rewind()
        gl.bitflip_sound.play()
        text('Bitflip!!', 60, 70)
        #het event word aangeroepen
        gl.bit.append(f.create_event(gl.obj, gl.bit))  
    
    
def mousePressed():
    global scene
    if 1210 < mouseX < 1260 and 650 < mouseY < 700:
        gl.time_snapshot = time.time()
        scene = "Menu"
        return scene
    
    #Tutorial
    if 1160 < mouseX < 1260 and 40 < mouseY < 90:
        gl.help_sound.rewind()
        gl.help_sound.play()
        gl.time_snapshot = time.time()
        scene = "Handleiding"
        Handleiding.draw()
        page = 0
        frameRate(60)
        return scene
    
    else:
        scene = "SpelSpelen"
        return scene
