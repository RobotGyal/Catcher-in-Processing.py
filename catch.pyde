
def setup():
    size(720,480)
    strokeWeight(2)
    ellipseMode(RADIUS)
    
    
    
    
def draw():
    background(0, 153, 204)
    robo = Robot(100, 100)
    robo.drawRobot(270, 460, 260, 95)
