class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y


   

    def eq(self , other):
        return self.x ==  other.x and self.y == other.y 

    def __eq__(self , other):
        return self.x ==  other.x and self.y == other.y 
    
    # def __add__(self , other):
    #     return Vector2D(self.x + other.x, self.y + other.y )

v1 = Vector2D(10,20)
v2 = Vector2D(10,20)
v3 = v1.eq(v2)
v4= v1==v2
print(v4)

