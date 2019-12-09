import time
import random
import json

def draw(i, j):
    while j < 700:
     while i < 1000:
      fill(255)
      stroke(0)
      square(i, j, 50)
      i += 50    
     j += 50
    
def randn(obj):
    x = []
    y = []
    x = [250, 300, 350, 400, 450, 500, 550, 600, 650, 700]
    y = [150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
    b = str(random.choice(x))
    c = str(random.choice(y))
    bit = b + "-" + c + "-" + random.choice(obj['colors'])
    return bit  

def events(times, minimal, maximum, wait):
    e=[5,10]
    while times >= 0:
        e.append(int(random.randrange(minimal,maximum, wait)))
        times -= 1
    return e    

def timer(start):
    #de timer functie die de tijd van nu vergelijkt het de start tijd het verschil hier tussen is de timer 
    end = time.time()
    return end - start

def time_convert(sec):
  #functie die de tijd convert naar leesbaare text
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
              
  return "Time Lapsed = " + str(hours) + ":" + str(mins) + ":" + str(sec)

    
