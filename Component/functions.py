#Alle nodige bestanden worden ingeladen.
import time
import random
import json

#deze functie tekend het bordspel                
def draw(i, j, s):
    for row in range(i, 700 + s, s):
     for column in range(j, 600 + s, s):
         strokeWeight(3)
         fill(220,220,220)
         stroke(0)
         square(row, column, s)

#deze functie maakt de events aan                  
def events(times, minimal, maximum, wait):
    #test tijden voor bitflips 
    e=[]
    while times >= 0:
        e.append(int(random.randrange(minimal,maximum, wait)))
        times -= 1
    return e    

#de timer functie die de tijd van nu vergelijkt het de start tijd het verschil hier tussen is de timer 
def timer(start):
    end = time.time()
    return end - start

#functie die de tijd convert naar leesbaare text
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  
  if mins < 10:
     mins = "0" + str(mins)
  if hours < 10:
     hours = "0" + str(hours) 
  if sec < 10:
     sec = "0" + str(sec)                                                                 
                                      
  return "Tijd verstreken: " + str(hours) + ":" + str(mins) + ":" + str(sec)

#als het tijd is voor een event worden deze aangemaakt en aan de reeks toegevoed
def create_event(obj, events):
    
    x = [250, 300, 350, 400, 450, 500, 550, 600, 650, 700]
    y = [150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
    b = str(random.choice(x))
    c = str(random.choice(y))
    bit = b + "-" + c + "-" 
    if events:     
        for o in events:
            g = o.split("-")
            f = g[0] + "-" + g[1] + "-"
            if f == bit:
                create_event(obj, events)
    return bit + random.choice(obj['colors'])    
      

    
