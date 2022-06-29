class Vehicle :
    def __init__(self,color,max_speed):
        self._color = color
        self.__max_speed = max_speed

    def __str__(self):
        return "this is vehicle class"

    def getMaxSpeed(self):
        return self.__max_speed

    def setMaxSpeed(self,max_speed):
        self.__max_speed = max_speed

    def print(self):
        print(f"color is {self._color}")



class Car(Vehicle):
    #class variable (outside the init function)
    #declare instance variable
    def __init__(self,max_speed,color,price,gears,is_convertible):
        super().__init__(color,max_speed)
        self.price = price
        self.gears = gears
        self.is_convertible = is_convertible
    
    def __str__(self):
        return ("This is car class")

    def print(self):
        super().print()
        print(f"gears is {self.gears}",f"Is car convertible: {self.is_convertible}")


    # def getspeed(self):
    #     return self.__speed
    
    # def getcolor(self):
    #     return self.__color

    # def setspeed(self,speed):
    #     self.__speed = speed

    # def setcolor(self,color):
    #     self.__color = color
    
    # def stop(self):
    #     print("car is Stoped")
    
    # def start(self):
    #     print("car is started")

    
honda = Car(40,"red",1000,7,True)

print(honda.print())