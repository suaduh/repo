import turtle, random

SCALE = 32 #Controls how many pixels wide each grid square is

class Game:
    '''
Purpose: Represents a Tetris game using turtle.py. Represented by 200 grids.
Instance variables: self.occupied: a list of lists that checks whether a grid square
is occupied by another square. Initialized to False for all grid squares.
self.active: represents the active Block object that the player is currently controlling
Methods: gameloop(): checks if movement is valid, and if it is the block object moves downward every 300 milliseconds.
If the movement isn't valid, it changes that square coordinate to True, which means it's occupied. 
It then creates a new Block object.
         move_left(): moves the Block left by binding the move_left method to the left key. Uses the Block method move() and changes the x coordinate by -1. 
         Also uses the Block method valid() and checks whether the movement is valid.
         move_right(): moves the Block right by binding the move_right method to the right key. Uses the Block method move() and changes the x coordinate by 1. 
         Also uses the Block method valid() and checks whether the movement is valid.
'''

    def __init__(self):
        self.occupied=[]
        for i in range(20):
            self.occupied.append([False,False,False,False,False,False,False,False,False,False])
        #Setup window size based on SCALE value.
        turtle.setup(SCALE*12+20, SCALE*22+20)

        #Bottom left corner of screen is (-1.5,-1.5)
        #Top right corner is (10.5, 20.5)
        turtle.setworldcoordinates(-1.5, -1.5, 10.5, 20.5)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)
        turtle.tracer(0, 0)

        #Draw rectangular play area, height 20, width 10
        turtle.bgcolor('black')
        turtle.pencolor('white')
        turtle.penup()
        turtle.setpos(-0.525, -0.525)
        turtle.pendown()
        for i in range(2):
            turtle.forward(10.05)
            turtle.left(90)
            turtle.forward(20.05)
            turtle.left(90)
        self.active=Block()
        #These three lines must always be at the BOTTOM of __init__
        turtle.ontimer(self.gameloop, 300)
        turtle.onkeypress(self.move_left, 'Left')
        turtle.onkeypress(self.move_right, 'Right')
        turtle.update()
        turtle.listen()
        turtle.mainloop()
    def gameloop(self):
        if self.active.valid(0,-1,self.occupied)==True:
            self.active.move(0,-1)
            turtle.update()
            turtle.ontimer(self.gameloop, 300)
        else:
            for i in self.active.squares:
                self.occupied[i.ycor()][i.xcor()]=True
            self.active=Block()
            turtle.ontimer(self.gameloop, 300)
    def move_left(self):
        if self.active.valid(-1,0,self.occupied)==True:
            self.active.move(-1, 0)
            turtle.update()
        else:
            []
    def move_right(self):
        if self.active.valid(1,0,self.occupied)==True:
            self.active.move(1,0)
            turtle.update()
        else:
            []
class Square(turtle.Turtle):
    '''
Purpose: represents a Square object made using the Turtle class.
Instance variables: self.x: current x-coordinate, self.y current y-coordinate, color: chosen color of the Square
Changes the Squaare's shape to square, and it's size to SCALE/20. Also set it's speed to 0, and fillcolor with self.color.
We then set pencolor to gray, and then move the Squaare object to (self.x,self.y)
Methods: Doesn't have any methods.
'''

    def __init__(self, x, y, color):
        turtle.Turtle.__init__(self)
        self.x=x
        self.y=y
        self.color=color
        self.shape('square')
        self.shapesize(SCALE/20)
        self.speed(0)
        self.fillcolor(self.color)
        self.pencolor('gray')
        self.penup()
        self.goto(self.x,self.y)
class Block:
    '''
Purpose: represents a Block object made up of Square objects.
Instance variables: self.squares: Initialized to an empty list. Represents a list of the four Square objects that make up this particular block.
Chooses a random tetrinome ands appends the chosen Square objects to self.squares.
Methods: move(): iterates through self.squares and uses turtle.goto to move the Block objects xcord and ycord by dx and dy.
         valid(): similar to the move method, and uses dx and dy. those represent tnteger values representing the chosen change in x or y coordinates
         instead of moving the Square objects, it checks whether the new location would be in-bounds. returns False if the new xcord is <0 or >9, or if the new ycord<0
         otherwise, returns True.

'''
    def __init__(self):
       self.squares=[]
       lst=[1,2,3,4,5,6,7]
       if random.choice(lst)==1:
           self.squares.append(Square(3, 18, 'cyan'))
           self.squares.append(Square(4, 18, 'cyan'))
           self.squares.append(Square(5, 18, 'cyan'))
           self.squares.append(Square(6, 18, 'cyan'))
       elif random.choice(lst)==2:
           self.squares.append(Square(4, 19, 'blue'))
           self.squares.append(Square(4, 18, 'blue'))
           self.squares.append(Square(5, 18, 'blue'))
           self.squares.append(Square(6, 18, 'blue'))
       elif random.choice(lst)==3:
           self.squares.append(Square(6, 19, 'orange'))
           self.squares.append(Square(4, 18, 'orange'))
           self.squares.append(Square(5, 18, 'orange'))
           self.squares.append(Square(6, 18, 'orange'))
       elif random.choice(lst)==4:
           self.squares.append(Square(6, 19, 'yellow'))
           self.squares.append(Square(5, 19, 'yellow'))
           self.squares.append(Square(5, 18, 'yellow'))
           self.squares.append(Square(6, 18, 'yellow'))
       elif random.choice(lst)==5:
           self.squares.append(Square(5, 18, 'lightgreen'))
           self.squares.append(Square(6, 18, 'lightgreen'))
           self.squares.append(Square(6, 19, 'lightgreen'))
           self.squares.append(Square(7, 19, 'lightgreen'))
       elif random.choice(lst)==6:
           self.squares.append(Square(5, 18, 'purple'))
           self.squares.append(Square(6, 19, 'purple'))
           self.squares.append(Square(6, 18, 'purple'))
           self.squares.append(Square(7, 18, 'purple'))
       else:
           self.squares.append(Square(5, 18, 'red'))
           self.squares.append(Square(6, 18, 'red'))
           self.squares.append(Square(5, 19, 'red'))
           self.squares.append(Square(4, 19, 'red'))
    def move(self,dx,dy):
       for i in self.squares:
           xcord=dx+i.xcor()
           ycord=dy+i.ycor()
           i.goto(xcord,ycord)
    def valid(self, dx, dy, occupied):
        for i in self.squares:
           xcord=dx+i.xcor()
           ycord=dy+i.ycor()
           if xcord<0 or xcord>9 or ycord<0:
               return False
           elif occupied[i.ycor()+dy][i.xcor()+dx]==True:
               return False
        return True
if __name__ == '__main__':
    Game() 