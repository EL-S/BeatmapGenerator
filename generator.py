from random import randint

width = 1920
height = 1080
notes = []

class Note:
    prev_x_value = randint(0,width)
    spacing = round(width/5)
    def __init__(self):
        lower = Note.prev_x_value-Note.spacing
        upper = Note.prev_x_value+Note.spacing
        if lower < 0:
            lower = 0
        if upper > width:
            upper = width
        self.x = randint(lower,upper)
        self.y = 0
        Note.prev_x_value = self.x
    def pos(self):
        return (self.x,self.y)

for i in range(100):
    notes.append(Note())

x = 0
for i in notes:
    print(i.pos(),abs(i.pos()[0]-x))
    x = i.pos()[0]

print(len(notes))

