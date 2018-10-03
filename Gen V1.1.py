import random

def createFruit(offset, bpm, variance, length, gamemode, snapdivisor, column, mode=0):
    """
    Creates fruit bro

    offset - The time in ms where the first beat is put.

    bpm - The the amount of beats per minute.

    variance - The maximum distance between each note.

    length - The length from the first to the last beat in seconds.

    gamemode - standard, taiko, ctb, mania. (1, 2, 3, 4)

    snapdivisor - divide bpm into how many parts.

    column - keys in mania.

    mode - Use mode=1 if you want all notes to be the exact same distance apart(the varaince).
    """
    if gamemode == 4:
        counter = snapdivisor - 1
        column = column - 1
        prevx = -2
        doubleprevx = -2
        doublenewx = -2
        if snapdivisor == 0:
            snapdivisor = 1
        for i in range(int((length/60) * bpm * snapdivisor)):
            if mode == 0:
                newx = int(round((random.random() * column)))
                counter += 1
                if counter == snapdivisor:
                    doublenewx = int(round((random.random() * column)))
                if newx == prevx or newx == doublenewx or newx == doubleprevx:
                    while newx == prevx or newx == doublenewx or newx == doubleprevx:
                        newx = int(round((random.random() * column)))
                if doublenewx == prevx or doublenewx == newx:
                    while doublenewx == prevx or doublenewx == newx:
                        doublenewx = int(round((random.random() * column)))
                if counter == snapdivisor:
                    prevx = newx
                    doubleprevx = doublenewx
                    if newx == 0:
                        newx = 64
                    if newx == 1:
                        newx = 192
                    if newx == 2:
                        newx = 320
                    if newx == 3:
                        newx = 448
                    if doublenewx == 0:
                        doublenewx = 64
                    if doublenewx == 1:
                        doublenewx = 192
                    if doublenewx == 2:
                        doublenewx = 320
                    if doublenewx == 3:
                        doublenewx = 448
                    print(str(int(newx))+','+'192'+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',1,0,0:0:0:0:')
                    print(str(int(doublenewx))+','+'192'+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',1,0,0:0:0:0:')
                    counter = 0
                else:
                    """newx = prevx"""
                    prevx = newx
                    doubleprevx = -9
                    if newx == 0:
                        newx = 64
                    if newx == 1:
                        newx = 192
                    if newx == 2:
                        newx = 320
                    if newx == 3:
                        newx = 448
                    print(str(int(newx))+','+'192'+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',1,0,0:0:0:0:')
                        
            elif mode == 1:
                if bool(random.getrandbits(1)) == True:
                    newx = variance
                else:
                    newx = -1 * variance    
    if gamemode == 3:
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
            
            
createFruit(38,174.11,256,114.410,4,2,4)
    
