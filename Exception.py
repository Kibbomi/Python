
try:
    a = 10/0
except:
    print("a : Error!")
finally:
    print("a : finally")




try:
    b = 10/0
except Exception as e:
    print("b Error!")
    print(e)
finally:
    print("b : finally")




class MyError(Exception):
    def __str__(this):
        return "Error!"

class Point:
    def __init__(this, x, y):
        this.x = x
        this.y = y
    
    def Print(this):
        print(f"Point ({this.x}, {this.y})")
        if this.x > 10 :
            raise MyError


p1 = Point(100,0)
try :
    p1.Print()
except MyError as e :
    print(e)

