#Alle nodige bestanden worden ingeladen.
import time
import random
import json
import functions as f
from pprint import pprint

add_library('minim')
from ddf.minim import Minim

#alle benodigde variable worden global gezet
def setup():
    global time, random, json, pprint
    global scene,nextPageArrow,returnArrow,page,font,scene,bitflip0,bitflip1,bitflip2,bitflipX
    global repeatHulp0,repeatHulp1,repeatHulp2,menu_font,achtergrond,imgboek,imgkaarten,imgrepeat,imglogo,menu_font,img,obj,p1,p2,p3,p4,bit,event_times,elapsed,time_snapshot,start,imgSettings,boldFont
    global thema, minim, bitflip_sound, help_sound,start,rest,file,themas

    
    tab = "Controls"
    nextPageArrow = loadImage("nextPageArrow.png")
    returnArrow = loadImage("returnArrow.png")
    logo = loadImage("Logo.jpg")
    nextPageArrow = loadImage("handleiding/nextPageArrow.png")
    returnArrow = loadImage("handleiding/returnArrow.png")
    bitflip0 = loadImage("handleiding/Bitflip0.png")
    bitflip1 = loadImage("handleiding/Bitflip1.png")
    bitflip2 = loadImage("handleiding/Bitflip2.png")
    bitflipX = loadImage("handleiding/BitflipX.png")
    repeatHulp0 = loadImage("handleiding/repeatHulp0.png")
    repeatHulp1 = loadImage("handleiding/repeatHulp1.png")
    repeatHulp2 = loadImage("handleiding/repeatHulp2.png")
    font = loadFont("ArialMT-48.vlw")
    boldFont = loadFont("Arial-BoldMT-48.vlw")

#Menu global varaibles

    achtergrond = loadImage("menu/Achtergrond.png")
    imgboek = loadImage("menu/Book.png")
    imgkaarten = loadImage("menu/kaarten.png")
    imgrepeat = loadImage("menu/repeat.png")
    imglogo = loadImage("menu/logo.png")
    imgSettings = loadImage('menu/Settings.png')
    menu_font = createFont("couture.otf", 144)
    
#repeathulp global variables

    img = loadImage("Achtergrondrepeat.png")
    
#spelspelen global variables

#settings.json && themas.json worden ingeladen     
    with open('settings.json', 'r') as a, open('themas.json', 'r') as b:
        c = a.read()
        d = b.read()
        obj = json.loads(c)
        themas = json.loads(d) 
        
    p1 = loadImage("spelspelen/p1.png")
    p2 = loadImage("spelspelen/p2.png")
    p3 = loadImage("spelspelen/p3.png")
    p4 = loadImage("spelspelen/p4.png")
    
    #de settings uit settings.json worden ingeladen 
    event_times = f.events(obj['amount_of_events'], obj['minimal_timer'], obj['max_timer'], obj['sleep']) #amount of events u want + #min wachttijd voor event
    bit = []
    start = 0                
    elapsed = 0
    rest = 0
    time_snapshot = 0
    start = 0
    #Het benodigde thema word uit themas.json gehaald
    thema = loadImage("data/Thema" + themas[obj['active_theme']][0] + ".png")
    minim = Minim(this)
    bitflip_sound = minim.loadFile("SoundEffects/" + themas[obj['active_theme']][1] + ".mp3")
    help_sound = minim.loadFile("SoundEffects/" + themas[obj['active_theme']][2] + ".mp3")
    
#main global variables        
    scene = "Menu"
    
