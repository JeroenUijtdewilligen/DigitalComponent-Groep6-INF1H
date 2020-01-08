#Alle nodige bestanden worden ingeladen.
import Main_setup as gl

def setup():
    global tab, begin, eind, sleep, amount
    
    tab = "Controls"
    amount = int(gl.obj['amount_of_events'])
    begin = int(gl.obj['minimal_timer'] // 60)
    eind = int(gl.obj['max_timer'] // 60)
    sleep = int(gl.obj['sleep'] // 60)

def draw():
    global tab
    background(230)
    textFont(gl.font, 35)
    
    if tab == "Controls":
        fill(255); rect(-10, -12, 650, 70, 17)
        fill(230); rect(640, -12, 650, 70, 17)

        stroke(195)
        line(120, 235, 1160, 235); line(120, 300, 1160, 300)
        line(120, 465, 1160, 465); line(120, 530, 1160, 530)
        line(120, 595, 1160, 595)
        stroke(0)
             
        fill(0)
        
        textFont(gl.boldFont, 35); text('Algemeen', 200, 140); text('Tutorial', 180, 370)
        textFont(gl.font, 35)
        
        textSize(25); text('Terug naar het menu', 233, 220)
        text('Programma afsluiten', 233, 285)
        text('Volgende pagina', 215, 450)
        text('Vorige pagina', 199, 515)
        text('Terug naar pagina 1', 233, 580)
        
        text('Rechter Pijl of S', 1050, 450)
        text('Linker Pijl of A', 1058, 515)
        
        textSize(35); text('M', 1120, 220); text('1', 1128, 580)
        textSize(30); text('ESC', 1108, 285) 
        
        
    if tab == "Extras":
        fill(230); rect(-10, -12, 650, 70, 17)
        fill(255); rect(640, -12, 650, 70, 17)
        #SpelSpelenSettings
        
        fill(0); text("Spelinstellingen", 320, 100)
        #save button
        fill(0,255,0); rect(510, 100, 100, 50);fill(0); text("Save", 560, 138)
        
        #Divider
        line(640, 0, 640, 720)
        #ThemaSettings
        fill(0); text("Themainstellingen", 960, 100)
        
        stroke(0)
        fill(255)
        
        if isMouseWithinSpace(700, 130, 250, 50):
            stroke(150)
        fill(255); rect(700, 130, 250, 50)
        if gl.obj['active_theme'] == "standaard":
            fill(0, 255, 0); rect(700, 130, 250, 50)
        fill(0); text("Standaard", 825, 168)
        stroke(0)
        fill(255)
        if isMouseWithinSpace(960, 130, 250, 50):
            stroke(150)
        fill(255); rect(960, 130, 250, 50)
        if gl.obj['active_theme'] == "random":
            fill(0, 255, 0); rect(960, 130, 250, 50)
        fill(0); text("Random", 1085, 168)
        stroke(0)
        if isMouseWithinSpace(700, 195, 250, 50):
            stroke(150)
        fill(255); rect(700, 195, 250, 50)
        if gl.obj['active_theme'] == "bc":
            fill(0, 255, 0); rect(700, 195, 250, 50)
        fill(0); text("Big Chungus", 825, 233)
        stroke(0)
        if isMouseWithinSpace(960, 195, 250, 50):
            stroke(150)
        fill(255); rect(960, 195, 250, 50)
        if gl.obj['active_theme'] == "bonzi":
            fill(0, 255, 0); rect(960, 195, 250, 50)
        fill(0); text("Bonzi Buddy", 1085, 233)
        stroke(0)
        if isMouseWithinSpace(700, 260, 250, 50):
            stroke(150)
        fill(255); rect(700, 260, 250, 50)
        if gl.obj['active_theme'] == "cm":
            fill(0, 255, 0); rect(700, 260, 250, 50)
        fill(0); text("Meiland", 825, 298)
        stroke(0)
        if isMouseWithinSpace(960, 260, 250, 50):
            stroke(150)
        fill(255); rect(960, 260, 250, 50)
        if gl.obj['active_theme'] == "fvd":
            fill(0, 255, 0); rect(960, 260, 250, 50)
        fill(0); text("FVD", 1085, 298)
        stroke(0)
        if isMouseWithinSpace(700, 325, 250, 50):
            stroke(150)
        fill(255); rect(700, 325, 250, 50)
        if gl.obj['active_theme'] == "kanye":
            fill(0, 255, 0); rect(700, 325, 250, 50)
        fill(0); text("Kanye", 825, 363)
        stroke(0)
        if isMouseWithinSpace(960, 325, 250, 50):
            stroke(150)
        fill(255); rect(960, 325, 250, 50)
        if gl.obj['active_theme'] == "kerst":
            fill(0, 255, 0); rect(960, 325, 250, 50)
        fill(0); text("Kerst", 1085, 363)
        stroke(0)
        if isMouseWithinSpace(700, 390, 250, 50):
            stroke(150)
        fill(255); rect(700, 390, 250, 50)
        if gl.obj['active_theme'] == "mario":
            fill(0, 255, 0); rect(700, 390, 250, 50)
        fill(0); text("Super Mario", 825, 428)
        stroke(0)
        if isMouseWithinSpace(960, 390, 250, 50):
            stroke(150)
        fill(255); rect(960, 390, 250, 50)
        if gl.obj['active_theme'] == "mc":
            fill(0, 255, 0); rect(960, 390, 250, 50)
        fill(0); text("Minecraft", 1085, 428)
        stroke(0)
        if isMouseWithinSpace(700, 455, 250, 50):
            stroke(150)
        fill(255); rect(700, 455, 250, 50)
        if gl.obj['active_theme'] == "siege":
            fill(0, 255, 0); rect(700, 455, 250, 50)
        fill(0); text("Rainbow 6 S", 825, 493)
        stroke(0)
        if isMouseWithinSpace(960, 455, 250, 50):
            stroke(150)
        fill(255); rect(960, 455, 250, 50)
        if gl.obj['active_theme'] == "thanos":
            fill(0, 255, 0); rect(960, 455, 250, 50)
        fill(0); text("Thanos", 1085, 493)
        stroke(0)
        if isMouseWithinSpace(700, 520, 250, 50):
            stroke(150)
        fill(255); rect(700, 520, 250, 50)
        if gl.obj['active_theme'] == "wilco":
            fill(0, 255, 0); rect(700, 520, 250, 50)
        fill(0); text("Wilco", 825, 558)
        stroke(0)
        if isMouseWithinSpace(960, 520, 250, 50):
            stroke(150)
        fill(255); rect(960, 520, 250, 50)
        if gl.obj['active_theme'] == "youngdaggerdack":
            fill(0, 255, 0); rect(960, 520, 250, 50)
        fill(0); text("Young Dagger", 1085, 558)
        stroke(0)
        if isMouseWithinSpace(700, 585, 250, 50):
            stroke(150)
        fill(255); rect(700, 585, 250, 50)
        if gl.obj['active_theme'] == "zelda":
            fill(0, 255, 0); rect(700, 585, 250, 50)
        fill(0); text("Zelda", 825, 623)
        stroke(0)
        if isMouseWithinSpace(960, 585, 250, 50):
            stroke(150)
        fill(255); rect(960, 585, 250, 50)
        if gl.obj['active_theme'] == "honden":
            fill(0, 255, 0); rect(960, 585, 250, 50)
        fill(0); text("Shiba", 1085, 623)
        stroke(0)    
        
        
        font = createFont("Arial", 40)
        textFont(font)
        text('Aantal bitflips:', 170, 225) 
        fill(255, 0, 0); rect(420, 190, 50, 50)
        fill(0)
        text(str(amount), 510 , 230) 
        fill(0, 255, 0); rect(550, 190, 50, 50)
        
        # + 140 on the y 
        fill(0)
        text('Begin tijd:       ', 170, 365) 
        fill(255, 0, 0); rect(420, 330, 50, 50)
        fill(0)
        text(str(begin), 510 , 370) 
        fill(0, 255, 0); rect(550, 330, 50, 50)
        
        fill(0)
        text('Eind tijd:         ', 170, 505) 
        fill(255, 0, 0); rect(420, 470, 50, 50)
        fill(0)
        text(str(eind), 510 , 510) 
        fill(0, 255, 0); rect(550, 470, 50, 50)
        
        
        fill(0)
        text('   Tijd tussen event:', 170, 645) 
        fill(255, 0, 0); rect(420, 610, 50, 50)
        fill(0)
        text(str(sleep), 510 , 650) 
        fill(0, 255, 0); rect(550, 610, 50, 50)
               
        
        
        
        
        
    fill(0)
    textFont(gl.font, 35)
    text('Controls', 320, 40)
    text('Extras', 960, 40)
    
    noFill()
    if 1210 < mouseX < 1260 and 650 < mouseY < 700:
        stroke(150)
    fill(255)
    rect(1210, 650, 50, 50)
    textFont(gl.font); textSize(40)
    fill(0)
    text('M', 1236 , 691)
    stroke(0)

def isMouseWithinSpace(x, y, w, h):
    if x < mouseX < x + w and y < mouseY < y + h:
        return True
    else:
        return False    
    
def mousePressed():
    global tab, begin, eind, sleep, amount, theme
    theme = ''
    if isMouseWithinSpace(0, 0, 650, 70) and tab == "Extras":
        tab = "Controls"
    
    if isMouseWithinSpace(641, 0, 650, 70) and tab == "Controls":
        tab = "Extras"

    if isMouseWithinSpace(1210, 650, 50, 50):
        gl.scene = "Menu"
        tab = "Controls"
        return gl.scene

    if isMouseWithinSpace(700, 130, 250, 50):
        #standaard
        change_theme('standaard')
        
    if isMouseWithinSpace(960, 130, 250, 50):
        #random
        change_theme('rand')
        
    if isMouseWithinSpace(700, 195, 250, 50):
        #big chungus
        change_theme('bc')
        
    if isMouseWithinSpace(960, 195, 250, 50):
        #bonzibuddy
        change_theme('bonzi')
        
    if isMouseWithinSpace(700, 260, 250, 50):
        #meiland
        change_theme('cm')
        
    if isMouseWithinSpace(960, 260, 250, 50):
        #fvd
        change_theme('fvd')
        
    if isMouseWithinSpace(700, 325, 250, 50):
        #kanye
        change_theme('kanye')
        
    if isMouseWithinSpace(960, 325, 250, 50):
        #kerst
        change_theme('kerst')

    if isMouseWithinSpace(700, 390, 250, 50):
        #super mario
        change_theme('mario')
        
    if isMouseWithinSpace(960, 390, 250, 50):
        #minecraft
        change_theme('mc')
        
    if isMouseWithinSpace(700, 455, 250, 50):
        #rainbow 6 siege
        change_theme('siege')
        
    if isMouseWithinSpace(960, 455, 250, 50):
        #thanos
        change_theme('thanos')
        
    if isMouseWithinSpace(960, 520, 250, 50):
        #xxxtentacion 
        change_theme('youngdaggerdack')    
        
    if isMouseWithinSpace(700, 520, 250, 50):
        #wilco
        change_theme('wilco')
        
    if isMouseWithinSpace(700, 585, 250, 50):
        #zelda
        change_theme('zelda')
        
    if isMouseWithinSpace(960, 585, 250, 50):
        #shiba
        change_theme('honden')
        
    #amount of events + && - 
    if isMouseWithinSpace(420, 190, 50, 50):
        amount -= 1
        if amount == 0:
            amount += 1
    if isMouseWithinSpace(550, 190, 50, 50):
        amount += 1
        
    #start tijd + && -    
    if isMouseWithinSpace(420, 330, 50, 50):
        begin -= 1
        if begin == 0:
            begin += 1
    if isMouseWithinSpace(550, 330, 50, 50):
        begin += 1
        
    #eind tijd + && -      
    if isMouseWithinSpace(420, 470, 50, 50):
        eind -= 1
        if eind == 0:
            eind += 1
    if isMouseWithinSpace(550, 470, 50, 50):
        eind += 1

    #tijd tussen events + && -       
    if isMouseWithinSpace(420, 610, 50, 50):
        sleep -=1
        if sleep == 0:
            sleep += 1
    if isMouseWithinSpace(550, 610, 50, 50):
        sleep += 1
        
    if isMouseWithinSpace(510, 100, 100, 50):
         #Hier worden  de settings omgezet naar seconden en opgeslagen in settings.json 
         gl.obj['amount_of_events'] = amount
         gl.obj['minimal_timer'] = begin * 60
         gl.obj['max_timer'] = eind * 60
         gl.obj['sleep'] = sleep * 60
         with open('settings.json', 'w') as f:
            gl.json.dump(gl.obj, f, ensure_ascii=False, indent=4)
                                    
    else:
        return gl.scene

#Deze functie checked welke key is ingedrukt en veranderd de scene waar nodig
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
            
#Deze functie scrijft de settings naar een .json bestand
def write_json(theme):
    gl.obj['active_theme'] = theme
    with open('settings.json', 'w') as f:
        gl.json.dump(gl.obj, f, ensure_ascii=False, indent=4)
    
#Deze functie varanderd het thema
def change_theme(theme):
    
    if theme == 'rand':
        
        k = gl.themas.keys()
        k.sort()
        theme = gl.random.choice(k)
    
    gl.thema = loadImage("data/Thema" + gl.themas[theme][0] + ".png")
    gl.bitflip_sound = gl.minim.loadFile("SoundEffects/" + gl.themas[theme][1] + ".mp3")
    gl.help_sound = gl.minim.loadFile("SoundEffects/" + gl.themas[theme][2] + ".mp3")
    write_json(theme)     
