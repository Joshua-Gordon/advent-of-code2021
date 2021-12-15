
import numpy as np

def construct(data):
    size = 100
    whole_thing = np.zeros((len(data)*5,len(data)*5))
    first_tile = np.array(data)
    for x in range(5):
        for y in range(5):
            if x == 0 and y == 0:
                whole_thing[x*size:(x+1)*size,y*size:(y+1)*size] = first_tile
            elif x == 0:
                prev_tile = whole_thing[0:size,(y-1)*size:y*size]
                new_tile = (prev_tile+1)
                new_tile = np.where(new_tile>9,1,new_tile)
                whole_thing[x*size:(x+1)*size,y*size:(y+1)*size] = new_tile
            else:
                prev_tile = whole_thing[(x-1)*size:x*size,y*size:(y+1)*size]
                new_tile = (prev_tile+1)
                new_tile = np.where(new_tile>9,1,new_tile)
                whole_thing[x*size:(x+1)*size,y*size:(y+1)*size] = new_tile
    return whole_thing





def part2():
    data = [[int(c) for c in l.strip()] for l in open('input.txt').readlines()]
    data = construct(data)

    start = (0,0)
    queue = [start]

    dists = {(0,0):0}
    prevs = {}

    while len(queue) > 0:
        queue = sorted(queue,key=lambda v: dists.get(v,9999999))
        n = queue.pop(0)

        neighbs = nexts(len(data),n)
        for neighb in neighbs:
            newdist = dists[n] + data[neighb[0]][neighb[1]]
            if neighb not in dists or newdist < dists[neighb]:
                dists[neighb] = newdist
                prevs [neighb] = n
                queue.append(neighb)
    print(dists)
    print(data)
    print(dists[(499,499)])


def nexts(size,loc):
    x,y = loc
    neighbs = []
    if x > 1:
        neighbs.append((x-1,y))
    if x < size-1:
        neighbs.append((x+1,y))
    if y > 1:
        neighbs.append((x,y-1))
    if y < size-1:
        neighbs.append((x,y+1))
    return neighbs

def day15():
    data = [[int(c) for c in l.strip()] for l in open('input.txt').readlines()]
    start = (0,0)
    queue = [start]

    dists = {(0,0):0}
    prevs = {}

    while len(queue) > 0:
        queue = sorted(queue,key=lambda v: dists.get(v,9999999))
        n = queue.pop(0)

        neighbs = nexts(len(data),n)
        for neighb in neighbs:
            newdist = dists[n] + data[neighb[0]][neighb[1]]
            if neighb not in dists or newdist < dists[neighb]:
                dists[neighb] = newdist
                prevs [neighb] = n
                queue.append(neighb)
    print(dists)


if __name__ == '__main__':
    day15()
    part2()
