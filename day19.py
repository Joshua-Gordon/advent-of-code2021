import numpy as np
from numpy import rot90

def l1(a,b):
    s = 0
    for i in range(len(a)):
        s += abs(a[i]-b[i])
    return s

def neg(a):
    return (-a[0],-a[1],-a[2])

def offset(a,b):
    #returns a new b that is offset by a
    return (b[0]-a[0],b[1]-a[1],b[2]-a[2])

rotx = np.array([[1,0,0],
                 [0,0,-1],
                 [0,1,0]])
roty = np.array([[0,0,1],
                 [0,1,0],
                 [-1,0,0]])
rotz = np.array([[0,-1,0],
                 [1,0,0],
                 [0,0,1]])


def cloudrot24(cloud):
    def cloudrot90(cloud,turns,axismat):
        newcloud = cloud[:]
        for i in range(turns):
            newcloud=list(map(lambda v: np.matmul(axismat,v), newcloud))
        return newcloud
    def cloudrot4(cloud,axismat):
        for i in range(4):
            yield cloudrot90(cloud,i,axismat)
    #start with x rotations, including identity
    yield from cloudrot4(cloud,rotx)
    #flip y
    yflip = cloudrot90(cloud,2,roty)
    yield from cloudrot4(yflip,rotx)
    #other y orientations
    yleft = cloudrot90(cloud,1,roty)
    yield from cloudrot4(yleft,rotz)
    yright = cloudrot90(cloud,3,roty)
    yield from cloudrot4(yright,rotz)
    #now the z
    zturn = cloudrot90(cloud,1,rotz)
    yield from cloudrot4(zturn,roty)
    zother = cloudrot90(cloud,3,rotz)
    yield from cloudrot4(zother,roty)


class Scanner():

    def __init__(self,num,beacons,pos=(0,0,0)):
        self.num = num
        self.beacons = beacons
        self.pos = pos


    def adjust_position(self,d):
        #make a new scanner
        newbeacons = []
        for b in self.beacons:
            newbeacons.append(offset(d,b))
        return Scanner(self.num,newbeacons,d)

    def compare(self,other):
        def count_matches(a1,a2):
            a1 = [(l[0],l[1],l[2]) for l in a1]
            a2 = [(l[0],l[1],l[2]) for l in a2]
            return len(set(a1).intersection(set(a2)))

        #try all offsets, and for each one try all rotations
        for rot in cloudrot24(other.beacons):
            rotbeacs = [(l[0],l[1],l[2]) for l in rot]
            rotscanner = Scanner(other.num,rotbeacs)
            for i in range(len(self.beacons)):
                for j in range(len(rotbeacs)):
                    direction = offset(self.beacons[i],rotbeacs[j])
                    offscan = rotscanner.adjust_position(direction)
                    n = count_matches(self.beacons,offscan.beacons)
                    if n >= 12:
                        return True, offscan
        return False, None


def part2():
    datalines = [l.strip() for l in open('input.txt').readlines()]
    scans = []
    while len(datalines) > 0:
        scans.append(parsescanner(datalines))
    print(scans)
    for s in scans:
        print(s.num)
    solved_scanners = set([scans.pop(0)])
    while len(scans) > 0:
        solvednums = [str(s.num) for s in solved_scanners]
        unsolvednums = [str(s.num) for s in scans]
        print("SOLVED:",' '.join(solvednums))
        print("TO SOLVE:",' '.join(unsolvednums))
        added = False
        nextscan = scans.pop(0)
        newsolved = set()
        for solved in solved_scanners:
            worked,new = solved.compare(nextscan)
            if worked:
                print("Solved scanner",nextscan.num)
                newsolved.add(new)
                toremove = None
                for s in scans:
                    if s.num == nextscan.num:
                        toremove = s
                if toremove is not None:
                    scans.remove(toremove)
                break
            else:
                print("Can't solve",nextscan.num,"moving on")
                if not added:
                    scans.append(nextscan)
                    added = True
        print('wrapping around')
        solved_scanners.update(newsolved)
    beacons = set()
    for s in solved_scanners:
        beacons.update(s.beacons)
    print(beacons)
    print(len(beacons))
    maxdist = 0
    scanners = list(solved_scanners) 
    for i in range(len(scanners)):
        for j in range(len(scanners)):
            dist = l1(scanners[i].pos,scanners[j].pos)
            if dist > maxdist:
                maxdist = dist
    print(maxdist)
    return scanners



def parsescanner(lines):
    num = int(lines.pop(0).split()[2])
    line = lines.pop(0)
    beacs = []
    while len(line) > 0:
        x,y,z = line.split(',')
        beacs.append((int(x),int(y),int(z)))
        line = lines.pop(0)
    return Scanner(num,beacs)


def day19():
    datalines = [l.strip() for l in open('input.txt').readlines()]
    scans = []
    while len(datalines) > 0:
        scans.append(parsescanner(datalines))
    print(scans)
    for s in scans:
        print(s.num)
    solved_scanners = set([scans.pop(0)])
    while len(scans) > 0:
        solvednums = [str(s.num) for s in solved_scanners]
        unsolvednums = [str(s.num) for s in scans]
        print("SOLVED:",' '.join(solvednums))
        print("TO SOLVE:",' '.join(unsolvednums))
        added = False
        nextscan = scans.pop(0)
        newsolved = set()
        for solved in solved_scanners:
            worked,new = solved.compare(nextscan)
            if worked:
                print("Solved scanner",nextscan.num)
                newsolved.add(new)
                toremove = None
                for s in scans:
                    if s.num == nextscan.num:
                        toremove = s
                if toremove is not None:
                    scans.remove(toremove)
                break
            else:
                print("Can't solve",nextscan.num,"moving on")
                if not added:
                    scans.append(nextscan)
                    added = True
        print('wrapping around')
        solved_scanners.update(newsolved)
    beacons = set()
    for s in solved_scanners:
        beacons.update(s.beacons)
    print(beacons)
    print(len(beacons))
    return solved_scanners




if __name__ == '__main__':
    #solved=day19()
    s=part2()
    """
    testcloud = [
[1,2,3],
[4,5,6],
[-3,-4,5]
            ]
    for i,rot in enumerate(cloudrot24(testcloud)):
        print(i)
        print(rot)

"""
