
def setup():
    
    global repeat1, repeat2, repeat3, font, output, scene
    font = createFont("couture.otf", 32)
    #variables
    repeat3 = 0
    repeat2 = 0
    repeat1 = 0
    output = 0
    scene = "RepeatHulp"
def draw():
    
    global repeat1, repeat2, repeat3, font, output
    
    #formule
    output = 1 + repeat1 + (repeat2 * repeat1) + (repeat3 * (repeat2 * repeat1))
    
    #nice graphic stuff
    background(240)
    strokeWeight(5)
    line(0, 600, 1280, 600)
    line(0, 525, 1280, 525)
    
    #text
    fill(0)
    textFont(font)
    text(repeat3, 100, 575)
    text(repeat2, 300, 575)
    text(repeat1, 500, 575)
    text("1", 700, 575)
    text(output, 900, 575)
    
    #green boxes
    fill(0, 255, 0)
    rect(40, 630, 60, 60)
    rect(240, 630, 60, 60)
    rect(440, 630, 60, 60)
   
    #red boxes
    fill(255, 0, 0)
    rect(110, 630, 60, 60)
    rect(310, 630, 60, 60)
    rect(510, 630, 60, 60)
    
    #back box
    noFill()
    rect(1210, 650, 50, 50)
    
def mousePressed():
    
    global repeat1, repeat2, repeat3, scene
    
    #interactivity for green boxes
    #greenbox1
    if 40 < mouseX < 100 and 630 < mouseY < 690:
        repeat3 += 1
        if repeat3 > 3:
            repeat3 = 0
   
    #greenbox2
    if 240 < mouseX < 300 and 630 < mouseY < 690:
        repeat2 += 1
        if repeat2 > 3:
            repeat2 = 0
    
    #greenbox3
    if 440 < mouseX < 500 and 630 < mouseY < 690:
        repeat1 += 1
        if repeat1 > 3:
            repeat1 = 0
    
    #interactivity for red boxes
    #redbox1
    if 110 < mouseX < 170 and 630 < mouseY < 690:
        repeat3 -= 1
        if repeat3 < 0:
            repeat3 = 3
    
    #redbox2
    if 310 < mouseX < 370 and 630 < mouseY < 690:
        repeat2 -= 1
        if repeat2 < 0:
            repeat2 = 3
   
    #redbox3
    if 510 < mouseX < 570 and 630 < mouseY < 690:
        repeat1 -= 1
        if repeat1 < 0:
            repeat1 = 3    
    
    if 1210 < mouseX < 1260 and 650 < mouseY < 700:
        scene = "Menu"
        return scene
    else:
        return scene
    
