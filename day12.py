
def part2():
    data = open('input.txt').readlines()
    graph = []
    big = set()
    small = set()
    for line in data:
        a,b = line.strip().split('-')
        if a < b:
            graph.append((a,b))
        else:
            graph.append((b,a))
        if a[0].islower():
            small.add(a)
        else:
            big.add(a)
        if b[0].islower():
            small.add(b)
        else:
            big.add(b)
    fringe = []
    fringe = search2(['start'],False,graph)
    print(fringe)
    amount = 0
    while not done2(fringe):
        after = []
        for new,twice in fringe:
            paths = search2(new,twice,graph)
            for path,usedtwice in paths:
                print(path)
                if path[-1] == 'end':
                    amount += 1
                else:
                    after.append((path,usedtwice))
        fringe = after
    print(amount)

def search2(current,usedtwice,graph):
    """
    Take in a path and whether or not it's used a small cave twice, and return all possible next paths
    """
    position = current[-1]
    if position == 'end':
        return []
    fringe = [] #all the next paths
    for a,b in graph:
        other = None
        if position == a:
            other = b
        if position == b:
            other = a
        if other and other != 'start':
            if other[0].islower():
                if other not in current:
                    fringe.append((current + [other],usedtwice))
                elif not usedtwice:
                    fringe.append((current + [other],True))
            elif other[0].isupper():
                fringe.append((current + [other],usedtwice))
    return fringe

def search(current, graph):
    position = current[-1]
    if position == 'end':
        return []
    fringe = []
    for a,b in graph:
        if position == a:
            if b[0].islower() and b not in current:
                fringe.append(b)
            elif b[0].isupper():
                fringe.append(b)
        if position == b:
            if a[0].islower() and a not in current:
                fringe.append(a)
            elif a[0].isupper():
                fringe.append(a)
    return [current + [f] for f in fringe]

def done(fringe):
    for e in fringe:
        if e[-1] != 'end':
            return False
    return True

def done2(fringe):
    for e in fringe:
        if e[0][-1] != 'end':
            return False
    return True

def day12():
    data = open('input.txt').readlines()
    graph = []
    big = set()
    small = set()
    for line in data:
        a,b = line.strip().split('-')
        if a < b:
            graph.append((a,b))
        else:
            graph.append((b,a))
        if a[0].islower():
            small.add(a)
        else:
            big.add(a)
        if b[0].islower():
            small.add(b)
        else:
            big.add(b)
    fringe = []
    current = ['start']
    fringe = search(current,graph)
    print(fringe)
    amount = 0
    while not done(fringe):
        after = []
        for new in fringe:
            paths = search(new,graph)
            for path in paths:
                print(path)
                if path[-1] == 'end':
                    amount += 1
                else:
                    after.append(path)
        fringe = after
    print(amount)
        

if __name__ == '__main__':
    #day12()
    part2()
