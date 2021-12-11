import numpy as np

def part2():
    data = open('input.txt').readlines()
    octos = []
    for line in data:
        row = []
        for c in line.strip():
            row.append(int(c))
        octos.append(row)
    octos = np.array(octos)
    print(octos)
    numflashes = 0
    
    for step in range(1000):
        stepped = octos + 1

        if step < 10:
            print(octos)
            print(step)
        flashed = set()
        done = False
        while not done:
            willflash = stepped > 9
            done = True
            for y in range(10):
                for x in range(10):
                    if willflash[x,y] and (x,y) not in flashed:
                        stepped[max(x-1,0):min(x+2,10),max(y-1,0):min(y+2,10)] += 1
                        numflashes += 1
                        flashed.add((x,y))
                        done = False
        for (x,y) in flashed:
            stepped[x,y] = 0
        octos = stepped
        if len(flashed) == 100:
            print(step+1)
            return
    print(numflashes)
    return octos
    pass

FLASH = 10


def day11():
    data = open('input.txt').readlines()
    octos = []
    for line in data:
        row = []
        for c in line.strip():
            row.append(int(c))
        octos.append(row)
    octos = np.array(octos)
    print(octos)
    numflashes = 0
    
    for step in range(100):
        stepped = octos + 1

        if step < 10:
            print(octos)
            print(step)
        flashed = set()
        done = False
        while not done:
            willflash = stepped > 9
            done = True
            for y in range(10):
                for x in range(10):
                    if willflash[x,y] and (x,y) not in flashed:
                        stepped[max(x-1,0):min(x+2,10),max(y-1,0):min(y+2,10)] += 1
                        numflashes += 1
                        flashed.add((x,y))
                        done = False
        for (x,y) in flashed:
            stepped[x,y] = 0
        octos = stepped
    print(numflashes)
    return octos


if __name__ == '__main__':
    #octos = day11()
    part2()
