from random import randint

width = 1920
height = 1080
height_spacing = 50
notes = []
to_be_deleted = []
catcher_width = 100
center = round(width/2)
catcher_height = height-height_spacing
catcher_x, catcher_y = center, catcher_height
combo = 0
note_diameter = 50
time_ms = 0
offset_ms = 0
timing = 100

class Note:
    prev_x_value = randint(0,width)
    spacing = round(width/5)
    def __init__(self, time_real, time_relative):
        lower = Note.prev_x_value-Note.spacing
        upper = Note.prev_x_value+Note.spacing
        if lower < 0:
            lower = 0
        if upper > width:
            upper = width
        self.x = randint(lower,upper)
        self.y = 0
        self.time_real = time_real
        self.time_relative = time_relative
        Note.prev_x_value = self.x
    def pos(self):
        return (self.x,self.y)
    def update_pos(self):
        self.y += 1
        return (self.x,self.y)
    def note_time(self):
        return (self.time_real,self.time_relative)

amount = 0
x = 0
def create_note(time_ms, relative_time):
    global x, amount
    notes.append(Note(time_ms, relative_time))
    #print(notes[amount].pos(),abs(notes[amount].pos()[0]-x))
    x = notes[amount].pos()[0]
    amount += 1

def move_notes():
    global height, height_spacing, to_be_deleted
    for i in notes:
        #print(i.pos(),i.note_time())
        i.update_pos()
        note_x, note_height = i.pos()[0], i.pos()[1]
        if note_height >= (catcher_height):
            #print(i.pos())
            #print("yeet")
            check_collision(note_x, note_height, i)
    delete_old_notes(to_be_deleted)
        
def check_collision(note_x, note_height, note_object):
    global combo, catcher_x, catcher_width, note_diameter, notes, to_be_deleted
    if note_x <= (catcher_x+(catcher_width/2)) and note_x >= (catcher_x-(catcher_width/2)) and note_height == (catcher_height):
        combo += 1
        print(combo, note_x, catcher_x, note_object.note_time())
        if combo > 1:
            print("combo:",combo)
    elif note_height > height+(note_diameter/2):
        #note offscreen, add to delete queue
        to_be_deleted.append(note_object)
    else:
        combo = 0
    #print("combo:",combo)
    
def delete_old_notes(delete_queue):
    global amount
    for i in delete_queue:
        try:
            notes.remove(i)
            amount -= 1
        except:
            pass
            #print("note isn't in notes list")

def check_time():
    global time_ms, offset_ms, timing
    relative_time = time_ms - offset_ms
    if ((relative_time % timing) == 0) and (relative_time >= 0):
        create_note(time_ms, relative_time)
    
while True:
    check_time()
    move_notes()
    time_ms += 1

#time between notes that is a percentage of the distance the note is from the next
#close notes are closer in time
#far notes are further in time
#potential leeway to make it less rhythming and repetitive
#potential preference for going one direction that has a small probablity of change based on location on screen

