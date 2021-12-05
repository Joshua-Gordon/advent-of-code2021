import re
from collections import Counter

def part2():
    data = open('input.txt').readlines()
    pattern = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
    counts = Counter()
    for line in data:
        match = pattern.match(line)
        x = int(match.groups(1)[0])
        y = int(match.groups(1)[1])
        z = int(match.groups(1)[2])
        w = int(match.groups(1)[3])
        if x == z:
            counts.update([(x,i) for i in range(min(w,y),max(y+1,w+1))])
        elif y == w:
            counts.update([(i,y) for i in range(min(z,x),max(x+1,z+1))])
        else:
            min_x = min(x,z)
            max_x = max(x,z)
            min_y = min(y,w)
            max_y = max(y,w)
            if (z - x) / (w - y) > 0:
                counts.update([(min_x+i,min_y+i) for i in range(0,max_x-min_x+1)])
            else:
                counts.update([(min_x+i,max_y-i) for i in range(0,max_x-min_x+1)])
    print(counts)
    l = [c for k,c in counts.items() if c >= 2]
    print(l)
    print(len(l))

def day5():
    data = open('input.txt').readlines()
    pattern = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
    counts = Counter()
    for line in data:
        match = pattern.match(line)
        x = int(match.groups(1)[0])
        y = int(match.groups(1)[1])
        z = int(match.groups(1)[2])
        w = int(match.groups(1)[3])
        if x == z:
            counts.update([(x,i) for i in range(min(w,y),max(y+1,w+1))])
        elif y == w:
            counts.update([(i,y) for i in range(min(z,x),max(x+1,z+1))])
    print(counts)
    l = [c for k,c in counts.items() if c >= 2]
    print(l)
    print(len(l))



if __name__ == '__main__':
    day5()
    part2()
