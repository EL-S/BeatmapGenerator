from random import randint

width = 1920
height = 1080
notes = []

class Note:
    def __init__(self):
        self.x = randint(0,width)
        self.y = 0
    def pos(self):
        return (self.x,self.y)

for i in range(100):
    notes.append(Note())

for i in notes:
    print(i.pos())

print(len(notes))

