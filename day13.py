import numpy as np

def part2():
    pass

def foldy(mat,axis):
    left = mat[:,:axis]
    right = mat[:,axis+1:]
    right = np.fliplr(right)
    x1,y1 = left.shape
    x2,y2 = right.shape
    if y1 == y2:
        return left+right
    if y1 > y2:
        ref = np.zeros_like(left)
        ref[:,y1-y2:] = right
        return left + ref
    if y2 > y1:
        ref = np.zeros_like(right)
        ref[:,y2-y1:] = left
        return ref + right

def foldx(mat,axis):
    top = mat[:axis,:]
    bottom = mat[axis+1:,:]
    bottom = np.flipud(bottom)
    print(top)
    print(bottom)
    x1,y1 = top.shape
    x2,y2 = bottom.shape
    print(x1,x2)
    #pad to same size
    if x1 == x2:
        print('equal')
        return top+bottom
    if x1 > x2:
        ref = np.zeros_like(top)
        ref[x1-x2:,:] = bottom
        print(ref)
        return top + ref
    if x2 > x1:
        ref = np.zeros_like(bottom)
        ref[x2-x1:,:] = top
        return ref + bottom

def day13():
    data = open('input.txt').readlines()
    points = []
    folds = []
    reading_points = True
    for line in data:
        if len(line.strip()) == 0:
            reading_points = False
        elif reading_points:
            x,y = line.strip().split(',')
            points.append((int(x),int(y)))
        else:
            expr = line.split(' ')[-1]
            d,val = expr.split('=')
            folds.append((d=='x',int(val)))
    
    max_x = max([x for x,y in points])
    max_y = max([y for x,y in points])
    mat = np.zeros((max_x+1,max_y+1))
    for x,y in points:
        mat[x,y] = 1

    first = None
    for d,axis in folds:
        print(mat)
        if d:
            mat = foldx(mat,axis)
        else:
            mat = foldy(mat,axis)
        if first is None:
            first = np.count_nonzero(mat)
        
    print('='*20)
    print(mat)
    for line in mat:
        s = ''
        for c in line:
            if c == 0:
                s += ' '
            else:
                s += '#'
        print(s)
    print('first:',first)
    print(np.count_nonzero(mat))


if __name__ == '__main__':
    day13()
    part2()
