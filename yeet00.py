import turtle

t = turtle.Pen()
t.speed(150)
size1 = 20
angle1 = 20
dire = 0
def color():
    color1 = str(input("""
                    what color do you want?
                    1 blue
                    2 green
                    3 yellow
                    4 red
                    5 black"""))
    
    if color1 == "1":
                t.pencolor("blue")
    elif color1 == "2":
                t.pencolor("green")
    elif color1 == "3":
                t.pencolor("yellow")
    elif color1 == "4":
                t.pencolor("red")
                    
    elif color1 == "5":
                t.pencolor("black")
                
    else:
        print("thats not an option...")
        color()

def position():
    x_p = int(input("what is the starting position's x coordinate?"))
    y_p = int(input("what is the starting position's y coordinate?"))
    t.pu()
    t.goto(x_p , y_p)
    t.pd()
def size():
    global size1
    size1 = int(input("how big should the shape be (in pixels) recomended:200"))

def left_spiral():
    global size1
    position()
    color()
    size()
    for x in range(size1):
        t.forward(x)
        t.left(91)

def right_spiral():
    global size1
    position()
    color()
    size()
    for x in range(size1):
        t.forward(x)
        t.right(89)

def angle():
    global angle1
    angle1 = int(input("what should the turn angle be for the spiral? (degrees)"))
                                                                                        
def direction ():
                 global dire
                 dire = str(input("what direction should the spriral go? 1 = right. 2 = left"))
                 
                            


def custom():
    global dire
    global size1
    global angle1           
    position()
    color()
    size()
    angle()
    direction()
    for x in range(size1):
            t.forward(x)
            if dire == "1":
                 t.right(angle1)
            elif dire == "2":
                 t.left(angle1)
            else:
                 print("you didnt pick right or left")
                 direction()

while True:
    inst = str(input("What do you want to draw? 1 left spiral. 2  right sprial 3 custom"))
    if inst == "1":
        left_spiral()
    elif inst == "2":
        right_spiral()
    elif inst == "3":
        custom()
