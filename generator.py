import pygame
import datetime
from pygame.locals import *
from random import randint

screen_width = 1920
game_width = (screen_width/3)*2
gamearea_offset = (screen_width-game_width)/2
width = 1920
height = 1080
height_spacing = 150
notes = []
to_be_deleted = []
catcher_width = 200
center = round(width/2)
catcher_height = height-height_spacing
catcher_x, catcher_y = center, catcher_height
combo = 0
note_diameter = 100
time_ms = 0
offset_ms = 0
nps = 10
timing = 1000/(nps*2)
running = True
ar = 9
note_speed = round(ar*0.55)
fps = 1000
time_until_bottom = 600 #ms
pixels_to_bottom = (height+(note_diameter/2))-height_spacing
pixels_a_ms = pixels_to_bottom/time_until_bottom
ms_a_frame = 1000/fps
pixels_a_frame = (pixels_a_ms)
clock = pygame.time.Clock()
caught = 0
total = 0
score = 0
base_score = 1000

white = (255, 255, 255)
black = (0, 0, 0)


screen = pygame.display.set_mode((width,height), pygame.FULLSCREEN)
pygame.init()
pygame.font.init()
gamefont = pygame.font.SysFont('Comic Sans MS', 130)
gamefont2 = pygame.font.SysFont('Comic Sans MS', 50)
gamefont3 = pygame.font.SysFont('Comic Sans MS', 80)

class Note:
    prev_x_value = randint(gamearea_offset+(note_diameter/2),game_width+gamearea_offset-(note_diameter/2))
    spacing = round(width/5)
    def __init__(self, time_real, time_relative):
        lower = Note.prev_x_value-Note.spacing
        upper = Note.prev_x_value+Note.spacing
        if lower < (gamearea_offset+(note_diameter/2)):
            lower = gamearea_offset+(note_diameter/2)
        if upper > (game_width+gamearea_offset-(note_diameter/2)):
            upper = game_width+gamearea_offset-(note_diameter/2)
        self.x = randint(lower,upper)
        self.y = 0-round(note_diameter/2)
        self.time_real = time_real
        self.time_relative = time_relative
        Note.prev_x_value = self.x
    def pos(self):
        return (self.x,self.y)
    def update_pos(self):
        self.y += 1*round(pixels_a_frame*time_factor)
        return (self.x,self.y)
    def note_time(self):
        return (self.time_real,self.time_relative)

amount = 0
x = 0
def create_note(time_ms, relative_time):
    #print(datetime.datetime.now())
    global x, amount
    notes.append(Note(time_ms, relative_time))
    #print(notes[amount].pos(),abs(notes[amount].pos()[0]-x))
    x = notes[amount].pos()[0]
    amount += 1

def move_notes():
    global height, height_spacing, to_be_deleted
    screen.fill(black)
    for i in notes:
        #print(i.pos(),i.note_time())
        i.update_pos()
        note_x, note_height = i.pos()[0], i.pos()[1]
        pygame.draw.circle(screen, white, (note_x, note_height), round(note_diameter/2))
        if note_height >= (catcher_height):
            #print(i.pos())
            #print("yeet")
            check_collision(note_x, note_height, i)
    delete_old_notes(to_be_deleted)
        
def check_collision(note_x, note_height, note_object):
    global combo, catcher_x, catcher_width, note_diameter, notes, to_be_deleted, time_ms, total, caught, score, base_score
    if note_x <= (catcher_x+(catcher_width/2)) and note_x >= (catcher_x-(catcher_width/2)) and note_height >= (catcher_height) and (note_height <= (catcher_height+20)): #(time_ms == note_object.note_time()[0]):
        combo += 1 #caught the note
        caught += 1
        total += 1
        score += base_score
        base_score = round(base_score * 1.1)
        to_be_deleted.append(note_object)
    elif note_height > height+(note_diameter/2):
        #note offscreen, add to delete queue
        total += 1
        to_be_deleted.append(note_object)
    else:
        #missed the note but it is still on the screen
        #this calls continously
        #you can't get a combo or a higher score multipler if there is a missed note on screen
        base_score = 1000
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
    relative_time = (time_ms - offset_ms)
    if ((relative_time % timing*time_factor) == 0) and (relative_time >= 0):
        create_note(time_ms, relative_time)
        
def draw_screen():
    if move_boost:
        catcher_colour = (66,223,255)
    else:
        catcher_colour = white
    pygame.draw.rect(screen, catcher_colour, [catcher_x-(catcher_width/2),catcher_y,catcher_width,(height_spacing/2)])
    if combo > 0:
        combo_size = gamefont.size(str(combo))
        combo_surface = gamefont.render(str(combo), False, (white))
        screen.blit(combo_surface,(round(catcher_x-(combo_size[0]/2)),round((height/2)-(combo_size[1]/2))))
    accuracy_size = gamefont2.size(str("%.2f" % ((caught/total)*100))+"%")
    displacement = width - accuracy_size[0]-41 #41 is the width of the percentage sign
    accuracy_surface = gamefont2.render(str("%.2f" % ((caught/total)*100))+"%", False, (white))
    screen.blit(accuracy_surface,(round(displacement),round(height/15)))
    score_size = gamefont3.size(str(score))
    score_displacement = width - score_size[0]
    score_surface = gamefont3.render(str(score), False, (white))
    screen.blit(score_surface,(round(score_displacement),-(score_size[1]/8)))
    pygame.display.flip()
    
def move_catcher():
    global catcher_x
    speed = 1.5
    multiply_speed = 1
    if move_boost:
        #boost
        multiply_speed = 1.5
    if move_left and not move_right and (catcher_x >= gamearea_offset+(catcher_width/2)):
        #left
        catcher_x -= speed*multiply_speed*time_factor
    elif move_right and not move_left and (catcher_x <= game_width+gamearea_offset-(catcher_width/2)):
        #right
        catcher_x += speed*multiply_speed*time_factor

    
move_left = False
move_right = False
move_boost = False

while running:
    time_factor = clock.tick(fps)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LSHIFT:
                move_boost = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LSHIFT:
                move_boost = False
    move_catcher()   
    check_time()
    move_notes()
    draw_screen()
    time_ms += 1
pygame.quit()

#time between notes that is a percentage of the distance the note is from the next
#close notes are closer in time
#far notes are further in time
#potential leeway to make it less rhythming and repetitive
#potential preference for going one direction that has a small probablity of change based on location on screen

