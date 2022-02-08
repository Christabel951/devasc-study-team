# Given a radius value, print the circumference of a circle.
# Formula for a circumference is c = pi * 2* radius

class Circle:

    def __init__(self, radius):
        self.radius = radius
    
    def circumference(self):
        pi = 3.14
        circumferenceValue = pi * self.radius * 2
        return circumferenceValue

    def printCircumference(self):
        myCircumference = self.circumference()
        print("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))

#1st Object:
circle_1 = Circle(2)
# - now use object to access methods inherited by object from class Circle
circle_1.printCircumference()

circle_2 = Circle(5)
circle_2.printCircumference()

circle_3 = Circle(7)
circle_3.printCircumference()