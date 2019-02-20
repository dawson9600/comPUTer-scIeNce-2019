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


def angle_2():
    global angle1
    sides = int(input("how many sides do you want?"))
    angle1 = int(360 / sides)


def angle():
    global angle1
    angle1 = int(input("what should the turn angle be for the spiral? (degrees)"))
                                                                                        
def direction ():
                 global dire
                 dire = str(input("what direction should the spriral go? 1 = right. 2 = left"))
                 

def reset():
    t.reset()
    print("the drawings have been removed")
    t.speed(150)

def choice():
                choice = str(input("""Do you want to select how many sides the shape has or do you wish to input a specific turning angle?
                                   1= Pick sides.
                                   2= Pick turn angle."""))
                if choice == "1":
                        angle_2()
                        
                elif choice == "2":
                        angle()
                else:
                        print("I dont understand...")
                        choice()
                
                
                


def custom_1():
    global dire
    global size1
    global angle1           
    position()
    color()
    size()
    choice()
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
    inst = str(input("""What do you want to draw? 
                           1= left spiral. 
                           2= right sprial. 
                           3= custom.
                           4= reset """))
    if inst == "1":
        left_spiral()
    elif inst == "2":
        right_spiral()
    elif inst == "3":
        custom_1()
    elif inst == "4":
        reset()
    else:
        print("I dont understand...")



