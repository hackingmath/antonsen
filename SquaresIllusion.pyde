'''Cloning Roger Antonsen's optical illusion:
https://twitter.com/rantonse/status/864174050377166848
Peter Farrell
August 19, 2017'''

def setup():
    size(700,700)
    rectMode(CENTER)
    colorMode(HSB)
    
t = 0.0 #time
dt = 0.0005 #change in time
    
def draw():
    global t,dt
    background(200)
    #translate to center of screen
    translate(width/2,height/2)
    #save this location and orientation
    #pushMatrix()
    
    #four circles
    for j in range(4):
        num = 12*(j+1)
        for i in range(num):
            #save this location and orientation
            pushMatrix()
            #rotate a twelfth of the circle
            rotate(radians(360.0/num*i))
            #translate a certain radius
            translate(75*(j+1),0)
            #rotate the square a little
            rotate(((-1)**j)*0.25*sin(t))
            #put a square there
            if i%2 == 0:
                stroke(255)
            else: stroke(0)
            strokeWeight(3)
            fill(20*i/(j+1),300,300)
            rect(0,0,25,25)
            #Go back to the saved location
            popMatrix()
            #increment time
            t += dt
    #(after the loop) Go back to the saved location
    #popMatrix()