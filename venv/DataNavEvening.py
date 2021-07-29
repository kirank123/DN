import logging
import time

print("Data Navigator Evening processes")

class DataNavigator:
    def __init__(self, age, name = "Krishnan"):
        self.name = name
        self.age = age

    def myfun(abc, house):
        abc.house = house
        pin = 685581
        print("My name is " + abc.name)
        print("House is " + abc.house)
        print("Pin is", pin)
    x = 5
    print("Data Navigator process in class")

class student(DataNavigator):
    def __init__(self, floc, lloc, age, name):
        super().__init__(age, name)
        self.floc = floc
        self.lloc = lloc


    def details(self):
        print("Firsr location is", self.floc, "Last location is", self.lloc)
        print("Age:", self.age, "Name:", self.name)


D1 = DataNavigator(29)
print(D1.age)
print(D1.name)
D1.age = 25
print("New age is " + str(D1.age))
D1.myfun("mallisseril")
S1 = student("Bangalore", "Kochi", 21, "kkkkk")
S1.details()
print(S1.floc)
print(S1.name)

