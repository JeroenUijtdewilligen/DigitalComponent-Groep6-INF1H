#alle libarys worden ingeladen
import time
import timer 
import random
import functions as f
from pprint import pprint
import json
import Handleiding

add_library('minim')
from ddf.minim import Minim


def setup():

    global start, event,event_times,time,pause, i, j, bit,font,p1,p2,p3,p4,scene,obj,square_size, Watgoed, HelpHelp , minim, thema

    
    # fetch settings
    with open('settings.json', 'r') as file:
        data=file.read()
    obj = json.loads(data)
  
    thema = loadImage("data/ThemaSTANDAARD.png")
    minim = Minim(this)
    Watgoed = minim.loadFile("WatGoed.mp3")
    HelpHelp = minim.loadFile("HelpHelp.mp3")
    

    p1 = loadImage("spelspelen/p1.png")
    p2 = loadImage("spelspelen/p2.png")
    p3 = loadImage("spelspelen/p3.png")
    p4 = loadImage("spelspelen/p4.png")
    start = timer.start_time()
    font = createFont("Arial", 32)
    
    frameRate(1)
    strokeWeight(5)
    #timer word gestart
    i = 250
    j = 150
    square_size = 50 
    bit = [] 
    pause = False
    #de tijden waar op de event gehouden worden word geladen.
    event_times = f.events(obj['amount_of_events'], obj['minimal_timer'], obj['max_timer'], obj['sleep']) #amount of events u want + #min wachttijd voor event
    scene = "SpelSpelen"
    
def draw():
    global start, event,event_times,time,pause, i, j, bit,font,p1,p2,p3,p4,scene,obj,square_size, thema
    textFont(font)
    background(230)
    fill(230)
    strokeWeight(5)
    stroke(0)
    
    image(thema, 0, 100)
    
    square(210, 380, 40)
    square(480, 110, 40)
    square(750, 380, 40)
    square(480, 650, 40)
    
    image(p2, 210, 380, 40, 40)
    image(p3, 480, 110, 40, 40)
    image(p4, 750, 380, 40, 40)
    image(p1, 480, 650, 40, 40)

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
    if bit:
        for coords in bit:
          g = coords.split("-")
          fill(int(g[2]),int(g[3]),int(g[4]))
          stroke(0)
          square(int(g[0]), int(g[1]), 50)
    check_time()        
    
    
    #Help/ Tutorial box
    if 1160 < mouseX < 1260 and 40 < mouseY < 90:

        stroke(150)
    fill(255)
    rect(1160, 40, 100, 50)
    fill(0)
    textSize(40)
    text('Help', 1211, 79)
    stroke(0)
            
def keyPressed():
    global start, event,event_times,time,pause, i, j, bit
    #check if de timer op pauze moet zo ja gaat hij op pauze
    if scene == 'menu':
        time.sleep(60)
        
def check_time():
    global HelpHelp
    if time in event_times:
        fill(0)
        Watgoed.rewind()
        Watgoed.play()
        text('Bitflip!!', 60, 70)
        #het event word aangeroepen
        bit.append(f.randn(obj))        
    
def mousePressed():
    global scene, Watgoed
    if 1210 < mouseX < 1260 and 650 < mouseY < 700:
        scene = "Menu"
        return scene
    
    #Tutorial
    if 1160 < mouseX < 1260 and 40 < mouseY < 90:
        HelpHelp.rewind()
        HelpHelp.play()
        scene = "Handleiding" 
        Handleiding.setup()
        page = 1
        frameRate(60)
        return scene
    
    else:
        scene = "SpelSpelen"
        return scene
