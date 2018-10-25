
class Bird:
    def __init__(self,type=None,color=None):
        pass
    def canFly(self):
        pass

class Parrot(Bird):
    def __init__(self):
        pass
    def canFly(self):
        print("yes can fly")


class Pangvinue(Bird):
    def __init__(self):
        pass
    def canFly(self):
        print("yes can't fly")


def isFly(bird):
    bird.canFly()

p=Pangvinue()
p1=Parrot()

isFly(p)
isFly(p1)

def add(x,y):
	return x+y
