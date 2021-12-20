
def part2():
    data = [l.strip() for l in open('input.txt').readlines()]
    alg = data.pop(0)
    data.pop(0)
    im = set()
    y = 0
    while len(data) > 0:
        line = data.pop(0)
        x = 0
        for c in line:
            if c == '#':
                im.add((x,y))
            x += 1
        y += 1
    print(im)
    ans = enhance_brightset(alg,im,50)
    print(len(ans))
    

def enhance_darkset(alg,im,count=1):
    x_lower = 9223372036854775800
    y_lower = 9223372036854775800
    x_upper = -9223372036854775800
    y_upper = -9223372036854775800
    for (x,y) in im:
        if x < x_lower:
            x_lower = x
        if x > x_upper:
            x_upper = x
        if y < y_lower:
            y_lower = y
        if y > y_upper:
            y_upper = y
    new_im = set()
    for x in range(x_lower-20,x_upper+30):
        for y in range(y_lower-20,y_upper+30):
            window = []
            for dy in range(-1,2):
                for dx in range(-1,2):
                    if (x+dx,y+dy) not in im:
                        window.append('1')
                    else:
                        window.append('0')
            idx = int(''.join(window),2)
            if alg[idx] == '#':
                new_im.add((x,y))
    if count == 1:
        return new_im
    else:
        return enhance_brightset(alg,new_im,count-1)

def enhance_brightset(alg,im,count=1):
    #return a darkset
    x_lower = 9223372036854775800
    y_lower = 9223372036854775800
    x_upper = -9223372036854775800
    y_upper = -9223372036854775800
    for (x,y) in im:
        if x < x_lower:
            x_lower = x
        if x > x_upper:
            x_upper = x
        if y < y_lower:
            y_lower = y
        if y > y_upper:
            y_upper = y
    new_im = set()
    for x in range(x_lower-20,x_upper+30):
        for y in range(y_lower-20,y_upper+30):
            window = []
            for dy in range(-1,2):
                for dx in range(-1,2):
                    if (x+dx,y+dy) in im:
                        window.append('1')
                    else:
                        window.append('0')
            idx = int(''.join(window),2)
            if alg[idx] == '.':
                new_im.add((x,y))
    if count == 1:
        return new_im
    else:
        return enhance_darkset(alg,new_im,count-1)


def day20():
    data = [l.strip() for l in open('input.txt').readlines()]
    alg = data.pop(0)
    data.pop(0)
    im = set()
    y = 0
    while len(data) > 0:
        line = data.pop(0)
        x = 0
        for c in line:
            if c == '#':
                im.add((x,y))
            x += 1
        y += 1
    print(im)
    dark = enhance_brightset(alg,im)
    ans = enhance_darkset(alg,dark)
    print(len(ans))


if __name__ == '__main__':
    day20()
    part2()
