class Car:
    def __init__(self,model,color,mileage):
        self.model = model
        self.color = color
        self.mileage = mileage

    """def __str__(self):
        return f"The {self.model} car is {self.color} color and has {self.mileage} mileage"
    """
car1 = Car('buggatti','red', 1000)
car2 = Car('porche','blue', 2000)

for Car in (car1,car2):
    print(f"The {Car.model}'s {Car.color} car has {Car.mileage}, miles")

"""
print(car1)
print(car2)
"""
