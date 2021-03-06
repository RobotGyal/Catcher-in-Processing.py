moveX = 200

def setup():
    global bg
    size(780, 800)
    strokeWeight(2)
    ellipseMode(RADIUS)
    bg = loadImage("space.jpg")
    bg.resize(width, height)


def keyPressed():
    global moveX
    if (keyCode == LEFT):
        moveX -= 5
    elif (keyCode == RIGHT):
        moveX += 5
    else:
        moveX = width / 2


def draw():
    global bg
    global moveX
    background(bg)
    # background(125)
    robo = Robot()
    robo.drawRobot(moveX, height, 50, 40)
    star = Star(100, 100)
    stroke(0, 123, 236)
    star.drawStar(50)
    star.fall()


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


class Star(object):

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def drawStar(self, size):
        self.size = size

        beginShape()
        vertex(self.xpos, self.ypos)
        vertex(self.xpos + self.size, self.ypos)
        vertex(self.xpos, self.ypos + self.size / 2)
        vertex(self.xpos + self.size / 2, self.ypos - self.size / 2)
        vertex(self.xpos + self.size, self.ypos + self.size / 2)
        vertex(self.xpos, self.ypos)
        endShape()

    def fall(self):
        self.ypos += 10
