import random

def createFruit(offset, bpm, variance, length, gamemode, snapdivisor, column, mode):
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
        prevprevx = -2
        doubleprevprevx = -1
        doublenewx = -2
        note = 0
        direction = 1
        if snapdivisor == 0:
            snapdivisor = 1
        for i in range(int((length/60) * bpm * snapdivisor)):
            if mode == 0:
                newx = int(round((random.random() * column)))
                newxkey = newx
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
                    newx = round((newx * (512 / (column + 1))) + (512 / (2 * (column + 1))))
                    doublenewx = round((doublenewx * (512 / (column + 1))) + (512 / (2 * (column + 1))))
                    print(str(int(newx))+','+'192'+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',1,0,0:0:0:0:')
                    print(str(int(doublenewx))+','+'192'+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',1,0,0:0:0:0:')
                    counter = 0
                else:
                    """newx = prevx"""
                    prevx = newx
                    doubleprevx = -9
                    newx = round((newx * (512 / (column + 1))) + (512 / (2 * (column + 1))))
                    print(str(int(newx))+','+'192'+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',1,0,0:0:0:0:')
                        
            elif mode == 1:
                if column > 1:
                    counter += 1
                    if note == 0:
                        newx = int(round((random.random() * column)))
                        if bool(random.getrandbits(1)) == True:
                            direction = 1
                        else:
                            direction = -1
                    if counter == snapdivisor:
                        doublenewx = int(round((random.random() * column)))
                    if note != 0:
                        if prevx >= column:
                            newx = int(round((random.random() * column)))  
                        elif prevx <= 0:
                            newx = int(round((random.random() * column)))
                        else:
                            if bool(random.getrandbits(1)) == True and bool(random.getrandbits(1)) == True:
                                direction = direction * -1
                                newx = prevx - direction
                            else:
                                newx = prevx - direction
                            
                    if doublenewx == prevx or doublenewx == newx or doublenewx == prevprevx:
                        while doublenewx == prevx or doublenewx == newx or doublenewx == prevprevx:
                            doublenewx = int(round((random.random() * column)))
                    if newx == doubleprevx or newx == prevx or newx == doublenewx or newx == prevprevx:
                                while newx == doubleprevx or newx == prevx or newx == doublenewx or newx == prevprevx:
                                    newx = int(round((random.random() * column)))
                    note += 1

                    if counter == snapdivisor:
                        prevx = newx
                        prevprevx = prevx
                        doubleprevx = doublenewx
                        doubleprevprevx = doubleprevx
                        newx = round((newx * (512 / (column + 1))) + (512 / (2 * (column + 1))))
                        doublenewx = round((doublenewx * (512 / (column + 1))) + (512 / (2 * (column + 1))))
                        print(str(int(newx))+','+'192'+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',1,0,0:0:0:0:')
                        print(str(int(doublenewx))+','+'192'+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',1,0,0:0:0:0:')
                        counter = 0
                    else:
                        """newx = prevx"""
                        prevx = newx
                        doubleprevx = -9
                        newx = round((newx * (512 / (column + 1))) + (512 / (2 * (column + 1))))
                        print(str(int(newx))+','+'192'+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',1,0,0:0:0:0:')
    if gamemode == 3:
        currentx = random.random() * 512
        counter = 3
        counter2 = 384
        counter3 = snapdivisor
        note = 0
        prevx = 0
        direction = 0
        for i in range(int((length/60) * bpm * snapdivisor)):
            if mode == 3:
                if counter3 == snapdivisor:
                    if note == 0:
                        newx = (random.random() * variance * 2) - variance
                    else:
                        if prevx < 128:
                            currentx = (random.random() * 348) + 164
                        elif prevx >= 128 and prevx < 256:
                            if bool(random.getrandbits(1)) == True:
                                currentx = (random.random() * 128) + 384
                            else:
                                currentx = (random.random() * 64) + 448
                        elif prevx >= 256 and prevx < 384:
                            if bool(random.getrandbits(1)) == True:
                                currentx = (random.random() * 64)
                            else:
                                currentx = (random.random() * 128)
                        elif prevx >= 384 and prevx < 512:
                            currentx = (random.random() * 348)
                    counter3 = 0
                else:
                    if direction != 0:
                        if abs(direction) < 10:
                            if direction > 0:
                                direction = 10
                            else:
                                direction = -10
                        currentx = prevx + direction + (random.random() * direction)
                        #newx = prevx + direction
                        if counter3 == (snapdivisor / 2):
                            if direction < 0:
                                direction = abs(direction)
                            else:
                                direction = direction * -1
                        if counter3 == snapdivisor - 1:
                            direction = 0
                    elif bool(random.getrandbits(1)) == True:
                        if (bpm * snapdivisor) <= 600:
                            direction = (random.random() * (variance / 2.5)) * -1
                        else:
                            direction = (random.random() * (variance / 5)) * -1
                        currentx = prevx + direction
                        #newx = prevx + direction
                    else:
                        if (bpm * snapdivisor) <= 600:
                            direction = (random.random() * (variance / 2.5))
                        else:
                            direction = random.random() * (variance / 5)
                        currentx = prevx + direction
                        #newx = prevx + direction
                    #newx = (random.random() * (variance / 10) * 2) - (variance / 10)

                if currentx <= 0:
                    direction = abs(direction)
                    currentx = 0 + abs(direction)
                    if currentx <= 0:
                        if (bpm * snapdivisor) <= 600:
                            currentx = (random.random() * (variance / 2.5))
                        else:
                            currentx = (random.random() * (variance / 5))
                elif currentx >= 512:
                    direction = direction * -1
                    currentx = 512 - abs(direction)
                    if currentx >= 512:
                        if (bpm * snapdivisor) <= 600:
                            currentx = 512 - (random.random() * (variance / 2.5))
                        else:
                            currentx = 512 - (random.random() * (variance / 5))
                prevx = currentx
                counter += 1
                note += 1
                counter3 += 1
                if counter == 4:
                    print(str(int(currentx))+','+str(counter2)+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',5,0,0:0:0:0:')
                    counter = 0
                    counter2 -= 48
                else:
                    print(str(int(currentx))+','+str(counter2)+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',1,0,0:0:0:0:')
                    counter2 -= 48
                if counter2 == -48:
                    counter2 = 384
            elif mode == 2:
                if counter3 == snapdivisor:
                    if note == 0:
                        newx = (random.random() * variance * 2) - variance
                    else:
                        if prevx < 128:
                            currentx = (random.random() * 348) + 164
                        elif prevx >= 128 and prevx < 256:
                            if bool(random.getrandbits(1)) == True:
                                currentx = (random.random() * 128) + 384
                            else:
                                currentx = (random.random() * 64) + 448
                        elif prevx >= 256 and prevx < 384:
                            if bool(random.getrandbits(1)) == True:
                                currentx = (random.random() * 64)
                            else:
                                currentx = (random.random() * 128)
                        elif prevx >= 384 and prevx < 512:
                            currentx = (random.random() * 348)
                    counter3 = 0
                else:
                    if direction != 0:
                        if abs(direction) < 10:
                            if direction > 0:
                                direction = 10
                            else:
                                direction = -10
                        currentx = prevx + direction + (random.random() * direction)
                        #newx = prevx + direction
                        if counter3 == snapdivisor / 2:
                            if direction < 0:
                                direction = abs(direction)
                            else:
                                direction = direction * -1
                        if counter3 == snapdivisor - 1:
                            direction = 0
                    elif bool(random.getrandbits(1)) == True:
                        direction = (random.random() * (variance / 10)) * -1
                        currentx = prevx + direction
                        #newx = prevx + direction
                    else:
                        direction = random.random() * (variance / 10)
                        currentx = prevx + direction
                        #newx = prevx + direction
                    #newx = (random.random() * (variance / 10) * 2) - (variance / 10)

                if currentx < 0:
                    direction = abs(direction)
                    currentx = 0
                elif currentx > 512:
                    direction = direction * -1
                    currentx = 512
                prevx = currentx
                counter += 1
                note += 1
                counter3 += 1
                if counter == 4:
                    print(str(int(currentx))+','+str(counter2)+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',5,0,0:0:0:0:')
                    counter = 0
                    counter2 -= 48
                else:
                    print(str(int(currentx))+','+str(counter2)+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',1,0,0:0:0:0:')
                    counter2 -= 48
                if counter2 == -48:
                    counter2 = 384
            else:
                if mode == 0:
                    newx = (random.random() * variance * 2) - variance
                elif mode == 1:
                    if bool(random.getrandbits(1)) == True:
                        newx = variance
                    else:
                        newx = -1 * variance
                if (abs(newx) / (60000 / bpm / snapdivisor)) <= 1 or (abs(newx) / (60000 / bpm / snapdivisor)) >= 1.35:
                    if (abs(newx) / (60000 / bpm / snapdivisor)) < 0.25:
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
                    if (abs(newx) / (60000 / bpm / snapdivisor)) <= 1 or (abs(newx) / (60000 / bpm / snapdivisor)) >= 1.35:
                        if (abs(newx) / (60000 / bpm / snapdivisor)) < 0.25:
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
                    print(str(int(currentx))+','+str(counter2)+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',5,0,0:0:0:0:')
                    counter = 0
                    counter2 -= 48
                elif counter == 1 or counter == 2 or counter == 3:
                    print(str(int(currentx))+','+str(counter2)+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',1,0,0:0:0:0:')
                    counter2 -= 48
                if counter2 == -48:
                    counter2 = 384
    if gamemode == 5:
        currentx = random.random() * 512
        counter = 3
        counter2 = 384
        counter3 = snapdivisor
        note = 0
        prevx = 0
        direction = 0
        for i in range(int((length/60) * bpm * snapdivisor)):
            if mode == 0:
                if counter3 == snapdivisor:
                    if note == 0:
                        newx = (random.random() * variance * 2) - variance
                    else:
                        if prevx < 128:
                            currentx = (random.random() * 348) + 164
                        elif prevx >= 128 and prevx < 256:
                            if bool(random.getrandbits(1)) == True:
                                currentx = (random.random() * 128) + 384
                            else:
                                currentx = (random.random() * 64) + 448
                        elif prevx >= 256 and prevx < 384:
                            if bool(random.getrandbits(1)) == True:
                                currentx = (random.random() * 64)
                            else:
                                currentx = (random.random() * 128)
                        elif prevx >= 384 and prevx < 512:
                            currentx = (random.random() * 348)
                    counter3 = 0
                else:
                    if direction != 0:
                        if abs(direction) < 10:
                            if direction > 0:
                                direction = 10
                            else:
                                direction = -10
                        currentx = prevx + direction + (random.random() * direction)
                        #newx = prevx + direction
                        if counter3 == (snapdivisor / 2):
                            if direction < 0:
                                direction = abs(direction)
                            else:
                                direction = direction * -1
                        if counter3 == snapdivisor - 1:
                            direction = 0
                    elif bool(random.getrandbits(1)) == True:
                        if (bpm * snapdivisor) <= 600:
                            direction = (random.random() * (variance / 2.5)) * -1
                        else:
                            direction = (random.random() * (variance / 5)) * -1
                        currentx = prevx + direction
                        #newx = prevx + direction
                    else:
                        if (bpm * snapdivisor) <= 600:
                            direction = (random.random() * (variance / 2.5))
                        else:
                            direction = random.random() * (variance / 5)
                        currentx = prevx + direction
                        #newx = prevx + direction
                    #newx = (random.random() * (variance / 10) * 2) - (variance / 10)

                if currentx <= 0:
                    direction = abs(direction)
                    currentx = 0 + abs(direction)
                    if currentx <= 0:
                        if (bpm * snapdivisor) <= 600:
                            currentx = (random.random() * (variance / 2.5))
                        else:
                            currentx = (random.random() * (variance / 5))
                elif currentx >= 512:
                    direction = direction * -1
                    currentx = 512 - abs(direction)
                    if currentx >= 512:
                        if (bpm * snapdivisor) <= 600:
                            currentx = 512 - (random.random() * (variance / 2.5))
                        else:
                            currentx = 512 - (random.random() * (variance / 5))
                prevx = currentx
                counter += 1
                note += 1
                counter3 += 1
                if counter == 4:
                    print(str(int(currentx))+','+str(counter2)+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',5,0,0:0:0:0:')
                    counter = 0
                    counter2 -= 48
                else:
                    print(str(int(currentx))+','+str(counter2)+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',1,0,0:0:0:0:')
                    counter2 -= 48
                if counter2 == -48:
                    counter2 = 384
            if mode == 2:
                if counter3 == snapdivisor:
                    if note == 0:
                        newx = (random.random() * variance * 2) - variance
                    else:
                        if prevx < 128:
                            currentx = (random.random() * 348) + 164
                        elif prevx >= 128 and prevx < 256:
                            if bool(random.getrandbits(1)) == True:
                                currentx = (random.random() * 128) + 384
                            else:
                                currentx = (random.random() * 64) + 448
                        elif prevx >= 256 and prevx < 384:
                            if bool(random.getrandbits(1)) == True:
                                currentx = (random.random() * 64)
                            else:
                                currentx = (random.random() * 128)
                        elif prevx >= 384 and prevx < 512:
                            currentx = (random.random() * 348)
                    counter3 = 0
                else:
                    if direction != 0:
                        if abs(direction) < 10:
                            if direction > 0:
                                direction = 10
                            else:
                                direction = -10
                        currentx = prevx + direction + (random.random() * direction)
                        #newx = prevx + direction
                        if counter3 == snapdivisor / 2:
                            if direction < 0:
                                direction = abs(direction)
                            else:
                                direction = direction * -1
                        if counter3 == snapdivisor - 1:
                            direction = 0
                    elif bool(random.getrandbits(1)) == True:
                        direction = (random.random() * (variance / 10)) * -1
                        currentx = prevx + direction
                        #newx = prevx + direction
                    else:
                        direction = random.random() * (variance / 10)
                        currentx = prevx + direction
                        #newx = prevx + direction
                    #newx = (random.random() * (variance / 10) * 2) - (variance / 10)

                if currentx < 0:
                    direction = abs(direction)
                    currentx = 0
                elif currentx > 512:
                    direction = direction * -1
                    currentx = 512
                prevx = currentx
                counter += 1
                note += 1
                counter3 += 1
                if counter == 4:
                    print(str(int(currentx))+','+str(counter2)+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',5,0,0:0:0:0:')
                    counter = 0
                    counter2 -= 48
                else:
                    print(str(int(currentx))+','+str(counter2)+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',1,0,0:0:0:0:')
                    counter2 -= 48
                if counter2 == -48:
                    counter2 = 384
            else:
                if mode == 3:
                    newx = (random.random() * variance * 2) - variance
                elif mode == 1:
                    if bool(random.getrandbits(1)) == True:
                        newx = variance
                    else:
                        newx = -1 * variance
                if (abs(newx) / (60000 / bpm / snapdivisor)) <= 1 or (abs(newx) / (60000 / bpm / snapdivisor)) >= 1.35:
                    if (abs(newx) / (60000 / bpm / snapdivisor)) < 0.25:
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
                    if (abs(newx) / (60000 / bpm / snapdivisor)) <= 1 or (abs(newx) / (60000 / bpm / snapdivisor)) >= 1.35:
                        if (abs(newx) / (60000 / bpm / snapdivisor)) < 0.25:
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
                    print(str(int(currentx))+','+str(counter2)+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',5,0,0:0:0:0:')
                    counter = 0
                    counter2 -= 48
                elif counter == 1 or counter == 2 or counter == 3:
                    print(str(int(currentx))+','+str(counter2)+','+str(int(offset + (i * (60000/bpm/snapdivisor))))+',1,0,0:0:0:0:')
                    counter2 -= 48
                if counter2 == -48:
                    counter2 = 384
            
            
createFruit(68,175,256,200.228,4,2,4,1)
#offset, bpm, variance, length, gamemode, snapdivisor, column, mode
#Gamemode 3 (CTB)
#   mode 0 = fun and random but possible
#   mode 1 = perfectly spaced, all hypers or all not hypers
#   mode 2 = hypers on beats, side to side
#   mode 3 = even better hypers and jumps on beats, random and rounded
#Gamemode 4 (Mania)
#   mode 0 = random, doubles on beat, no stacking/jackhammers
#   mode 1 = streams, doubles on beat, less repeating patterns (better with 5k +)(makes 4k more human like)
#Gamemode 5 (DTB)
#   mode 0 = double notes every beat, impossible to properly play, dodge only.
#   (bpm / x = 200) with x being an integer that is even, seems to work best, with a snapdivisor of 4 and variance of 256.
#   etc, createFruit(4785,200,256,225.3,5,4,5,0)
#   accidentally created it, don't look at code, don't set mode to anything else.
    
