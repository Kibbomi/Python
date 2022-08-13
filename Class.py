
from turtle import hideturtle


class Point :
    # C# C++ 처럼 overloading 할 수 없음..
    '''
    def __init__(this) :
        this.x = 0
        this.y = 0
    '''
    def __init__(this, x =0 , y = 0):
        print("constructor of Point")
        this.x = x
        this.y = y
    
    
    def Print(this):
        print("Point: (%d, %d)" %(this.x, this.y))

    name = "POINT"


class Circle(Point):
    def __init__(this, x, y, r):
        print("Constructor of Circle")
        super().__init__(x,y) # run constructor of super class(Point)
        this.r = r
    
    # overriding #
    def Print(this):
        print(f"Point({this.x},{this.y}), radius : {this.r}")

    name = "CIRCLE"




p2 = Point(10,10)
p2.Print()
print('\n')

c1 = Circle(1,2,3)
c1.Print()
