
# Mouse Inversion
# def draw():
#     x = mouseX
#     y = mouseY
#     ix = width - mouseX   # Inverse X
#     iy = height - mouseY   # Inverse Y
#     background(126)
#     fill(255, 150)
#     ellipse(x, height/2, y, y)
#     fill(0, 159)
#     ellipse(ix, height/2, iy, iy)


# Find speed by taking deltaX
# def draw():
#     frameRate(12)
#     println(pmouseX - mouseX)


# Drawing line based on speed
# def setup():
#     size(100, 100)
#     strokeWeight(8)

# def draw():
#     background(204)
#     line(mouseX, mouseY, pmouseX, pmouseY)


# Drawing blocks based on mouse position
# def setup():
#     size(100, 100)
#     noStroke()
#     fill(0)

# def draw():
#     background(204)
#     if (mouseX < 33):
#         rect(0, 0, 33, 100)   # Left
#     elif (mouseX < 66):
#         rect(33, 0, 33, 100)   # Middle
#     else:
#         rect(66, 0, 33, 100)   # Right


# Changing color based on position
# def setup():
#     size(100, 100)
#     noStroke()
#     fill(0)

# def draw():
#     background(204)
#     if ((mouseX > 40) and (mouseX < 80) and
#       (mouseY > 20) and (mouseY < 80)):
#         fill(255)
#     else:
#         fill(0)
#     rect(40, 20, 40, 60)

# Fills in a shape based on if mouse is clicka dn which mouse button is clicked
# def setup():
#     size(100, 100)

# def draw():
#     if (mousePressed == True):
#         if (mouseButton == LEFT):
#             fill(0)   # Black
#         elif (mouseButton == RIGHT):
#             fill(255)   # White
#     else:
#         fill(126)   # Gray

#     rect(25, 25, 50, 50)


# Changes based on any key press
# def setup():
#     size(100, 100)
#     strokeWeight(4)

# def draw():
#     background(204)
#     if (keyPressed):   # If the key is pressed,
#         line(20, 20, 80, 80)   # draw a line
#     else:   # Otherwise,
#         rect(40, 40, 20, 20)   # draw a rectangle


# reads and displays key pressed
# def setup():
#     size(100, 100)
#     textSize(60)

# def draw():
#     background(0)
#     text(key, 20, 75)   # Draw at coordinate (20,75)



# Reads key value and converts it to ASCII value, uses that to change angle
# angle = 0

# def setup():
#     size(100, 100)
#     fill(0)


# def draw():
#     global angle
#     background(204)
#     if (keyPressed):
#         if ((ord(key) >= 32) and (ord(key) <= 126)):
#             # If the key is alphanumeric, use its value as an angle
#             angle = (ord(key) - 32) * 3

#     arc(50, 50, 66, 66, 0, radians(angle))
 
    
       
# Coded keys
y = 35

def setup():
  size(100, 100)

def draw():
    global y
    background(204)
    line(10, 50, 90, 50)
    if (key == CODED):
        if (keyCode == UP):
            y = 20
        elif (keyCode == DOWN):
            y = 50
    else:
        y = 35
    rect(25, y, 50, 30)
