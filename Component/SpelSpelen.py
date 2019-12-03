#alle libarys worden ingeladen
import time
import timer 
import random
import functions as f
import temp as t
from pprint import pprint

def setup():
    global start, event,event_times,time,pause, i, j, bit, font,p1,p2,p3,p4
    p1 = loadImage("spelspelen/p1.png")
    p2 = loadImage("spelspelen/p2.png")
    p3 = loadImage("spelspelen/p3.png")
    p4 = loadImage("spelspelen/p4.png")
    start = timer.start_time()
    font = createFont("Arial", 32)
    textFont(font)
    frameRate(1)
    global start, event,event_times,time,pause, i, j, bit, scene
    #timer word gestart
    i = 200
    j = 150
    bit = [] 
    pause = False
    #de tijden waar op de event gehouden worden word geladen.
    event_times = f.events(12, 60) #amount of events u want + #min wachttijd voor event
    scene = "SpelSpelen"
    
def draw():
    global start, event,event_times,time,pause, i, j, bit, font,p1,p2,p3,p4
    background(230)
    fill(230)
    stroke(0)
    square(900, 200, 80)
    image(p4, 845, 215, 40, 40)
    image(p3, 920, 150, 40, 40)
    image(p2, 990, 215, 40, 40)
    image(p1, 920, 290, 40, 40)

    #er word gekeken of de timer op pause staat zo nee blijft de timer door lopen zo ja word de timer op 0 gezet (pauze)
    if pause == False:
     time = int(f.timer(start))
    else:
     time = 0
     
    fill(0)
    text(str(f.time_convert(time)), 500, 70)
    strokeWeight(5)
    line(0, 100, 1280, 100)
    noFill()
    if 50 < mouseX < 100 and 620 < mouseY < 670:
        stroke(150)
    rect(50, 620, 50, 50)
    stroke(0)
    fill(0)
    textSize(40)
    text('M', 76 , 659)
    noFill()
    textSize(32)
    t.draw()      
    #f.draw(i, j)

    textFont(font)
    textAlign(CENTER)
    #er word gekeken of er tijd is voor een event            
    if bit:
        for coords in bit:
          g = coords.split("-")
          fill(int(g[2]),int(g[3]),int(g[4]))
          stroke(0)
          square(int(g[0]), int(g[1]), 50)
    check_time()                  
            
def keyPressed():
    global start, event,event_times,time,pause, i, j, bit
    #check if de timer op pauze moet zo ja gaat hij op pauze
    if key == 'p':
        pass
        #time.sleep(60)
        
def check_time():
    if time in event_times:
        fill(0)
        text('Bitflip!!', 60, 70)
        #het event word aangeroepen
        bit.append(f.randn())        
    
def mousePressed():
    global scene
    if 50 < mouseX < 100 and 620 < mouseY < 670:
        scene = "Menu"
        return scene
    else:
        return scene
