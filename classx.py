# Class X is being imported by pkg.py as an example how to create a package in Python 
# you need to add __init__.py in the directory where the codes that you want to pack are stored

class GrandPa():
    def grandPaFunc(self, msg):
        print (f"I am a {msg} at Grandpa's home")

class Parent(GrandPa):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def parentFunc(self):
        print (f"I am a {self.msg} at Parent's home")

class GrandSon(Parent):
    def sonFunc(self, msg):
        print (f"I am a {msg} at GrandSon's home")
