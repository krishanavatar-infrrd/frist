class Employee:

    x=0
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal

    def __init__(self):
        self.name=0
        self.age=0
        self.sal=0

    def __del__(self):

        print("destroye")





x=input("something:")

