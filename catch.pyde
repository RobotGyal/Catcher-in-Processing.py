def setup():
    size(780, 800)
    strokeWeight(2)
    ellipseMode(RADIUS)
    bg = loadImage("space.jpg")
    bg.resize(width, height)
    background(bg)




def draw():
    # background(125)
    robo = Robot()
    robo.drawRobot(width/2, height, 50, 40)


class Robot(object):
    # def __init__(self, tempX, tempY):
    #     self.xpos = tempX
    #     self.ypos = tempY
    #     self.angle = random(0, TWO_PI)

    def drawRobot(self, x, y, bodyHeight, neckHeight):
        radius = 45
        ny = y - bodyHeight - neckHeight - radius

        # NECK
        stroke(255)
        line(x + 2, y - bodyHeight, x + 2, ny)
        line(x + 12, y - bodyHeight, x + 12, ny)
        line(x + 22, y - bodyHeight, x + 22, ny)

        # ANTENNAE
        line(x + 12, ny, x - 18, ny - 43)
        line(x + 12, ny, x + 42, ny - 99)
        line(x + 12, ny, x + 78, ny + 15)

        # BODY
        noStroke()
        fill(255, 204, 0)
        ellipse(x, y - 33, 33, 33)
        fill(125)
        rect(x - 45, y - bodyHeight, 90, bodyHeight - 33)
        fill(255, 204, 0)
        rect(x - 45, y - bodyHeight + 17, 90, 6)

        # HEAD
        fill(125)
        ellipse(x + 12, ny, radius, radius)
        fill(255)
        ellipse(x + 24, ny - 6, 14, 14)
        fill(0)
        ellipse(x + 24, ny - 6, 3, 3)
