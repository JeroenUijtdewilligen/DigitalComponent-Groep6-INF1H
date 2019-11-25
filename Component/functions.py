import time
import random

def draw(i, j):
    while j < 700:
     while i < 1000:
      fill(255)
      stroke(0)
      square(i, j, 50)
      i += 50    
     j += 50
    
def randn():
    x = []
    y = []
    x = [250, 300, 350, 400, 450, 500, 550, 600, 650, 700]
    y = [150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
    b = str(random.choice(x))
    c = str(random.choice(y))
    colors = ["255-0-0", "0-255-0", "0-0-255", "0-0-0", "255-255-0", "255-255-255"]
    bit = b + "-" + c + "-" + random.choice(colors)
    return bit  

def events(times, min):

    e = [5, 10, 15, 20 ,40, 50, 60, 678]
    # e=[]
    # while times >= 0:
    #     e.append(int(random(min,600)))
    #     times -= 1
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

    
