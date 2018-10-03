import random

def createFruit(offset, bpm, variance, length, mode=0):
    """
    Creates fruit bro

    offset - The time in ms where the first beat is put.

    bpm - The the amount of beats per minute.

    variance - The maximum distance between each note.

    length - The length from the first to the last beat in seconds.

    mode - Use mode=1 if you want all notes to be the exact same distance apart(the varaince).
    """
    currentx = random.random() * 512
    counter = 3
    counter2 = 384
    prevx = 0
    for i in range(int((length/60) * bpm)):
        if mode == 0:
            newx = (random.random() * variance * 2) - variance
        elif mode == 1:
            if bool(random.getrandbits(1)) == True:
                newx = variance
            else:
                newx = -1 * variance
        if (abs(newx) / (60000 / bpm)) <= 1 or (abs(newx) / (60000 / bpm)) >= 1.35:
            if (abs(newx) / (60000 / bpm)) < 0.25:
                if currentx - (newx*4) > 0 and currentx - (newx*4) < 512:
                    currentx -= newx*4
                else:
                    currentx += newx    
            if currentx - newx > 0 and currentx - newx < 512:
                currentx -= newx
            else:
                currentx += newx
        else:
            if mode == 0:
                newx = (random.random() * variance * 2) - variance
            elif mode == 1:
                if bool(random.getrandbits(1)) == True:
                    newx = variance
                else:
                    newx = -1 * variance
            if (abs(newx) / (60000 / bpm)) <= 1 or (abs(newx) / (60000 / bpm)) >= 1.35:
                if (abs(newx) / (60000 / bpm)) < 0.25:
                    if currentx - (newx*4) > 0 and currentx - (newx*4) < 512:
                        currentx -= newx*4
                    else:
                        currentx += newx 
                if currentx - newx > 0 and currentx - newx < 512:
                    currentx -= newx
                else:
                    currentx += newx
            else:
                currentx = prevprevx

        prevprevx = prevx
        prevx = currentx
        counter += 1
        if counter == 4:
            print(str(int(currentx))+','+str(counter2)+','+str(int(offset + (i * (60000/bpm))))+',5,0,0:0:0:0:')
            counter = 0
            counter2 -= 48
        else:
            print(str(int(currentx))+','+str(counter2)+','+str(int(offset + (i * (60000/bpm))))+',1,0,0:0:0:0:')
            counter2 -= 48
        if counter2 == -48:
            counter2 = 384
        
        
createFruit(2310,340,256,107)
    
