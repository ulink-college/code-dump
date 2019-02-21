import three as t

class calculator():
    def __init__(self , dimention , shape):
        self.dimention = dimention
        self.shape = shape
        if dimention == int(3):
            shape = input("what shape you want to choose within cone , sphere , prism or pyramid: ")
            if shape == "cone":
                t.cone()
        elif dimention == int(2):
            shape = input("what shape you want to choose within triangle,rectangle,square or ciecle?: ")
    
        
            
    def two_dimentional(self , shape):
        if shape == str("triangle"):
            print("ok")
calculator(3,1)