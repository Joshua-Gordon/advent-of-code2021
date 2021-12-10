import numpy as np


def floodfill(array,point,basin=[]):
    done = False
    if len(basin) == 0:
        basin = np.zeros_like(array)
        done = True
    x,y = point
    print(x,y)
    if x >= 0 and x < len(array) and y >= 0 and y < len(array[0]) and basin[x,y] == 0 and array[x,y] != 9:
        basin[x,y] = 1
        print("flooding point ",x,y,"!")
        basin = floodfill(array,(x-1,y),basin)
        basin = floodfill(array,(x+1,y),basin)
        basin = floodfill(array,(x,y-1),basin)
        basin = floodfill(array,(x,y+1),basin)
    if done:
        print(basin)
        size = 0
        for x in range(1,len(array)-1):
            for y in range(1,len(array[0])-1):
                if basin[x,y] == 1:
                    size += 1
        return size
    else:
        return basin

    

def part2():
    data = open('input.txt').read()
    d2data = np.array([[int (c) for c in line] for line in data.split('\n') if len(line)>0])
    padded = np.pad(d2data,((1,1),(1,1)),'maximum')
    basins = []
    for x in range(1,len(padded)-1):
        for y in range(1,len(padded[0])-1):
            neighborhood = padded[x-1:x+2,y-1:y+2]
            if np.count_nonzero(np.less(neighborhood[1][1], neighborhood)) == 8:
                basins.append((x,y))
    #flood fill
    scores = []
    for b in basins:
        score = floodfill(padded,b)
        scores.append(score)
    scores = sorted(scores,reverse=True)
    print(scores)
    print(scores[0]*scores[1]*scores[2])
    

def day9():
    data = open('input.txt').read()
    d2data = np.array([[int (c) for c in line] for line in data.split('\n') if len(line)>0])
    padded = np.pad(d2data,((1,1),(1,1)),'maximum')
    total = 0
    for x in range(1,len(padded)-1):
        for y in range(1,len(padded[0])-1):
            print(x,y)
            neighborhood = padded[x-1:x+2,y-1:y+2]
            print(neighborhood)
            if np.count_nonzero(np.less(neighborhood[1][1], neighborhood)) == 8:
                print("Minimal!")
                total += neighborhood[1][1]+1
    print(total)


if __name__ == '__main__':
    #day9()
    part2()
