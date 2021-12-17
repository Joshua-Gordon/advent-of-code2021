
def part2():
    pass

def fire(x,y):
    target = (85,145,-163,-108)
    #target = (20,30,-10,-5)
    cur_x = 0
    cur_y = 0
    x_vel = x
    y_vel = y
    while cur_y >= -170:
        cur_x += x_vel
        cur_y += y_vel
        #print(cur_x,cur_y)
        if cur_x in range(target[0],target[1]+1) and cur_y in range(target[2],target[3]+1):
            print("hit:",x,y)
            return True
        if x_vel < 0:
            x_vel += 1
        if x_vel > 0:
            x_vel -= 1
        y_vel -= 1
    return False

def get_highest(y):
    return y*(y+1)/2



def day17():
    data = [l.strip() for l in open('test_input.txt').readlines()]
    start = (0,0)
    x = 1
    y = -170
    hits = []
    while True:
        print('testing x=',x,'and y=',y)
        if fire(x,y):
            hits.append((x,y))
        x += 1
        if x > 150:
            x = 1
            y += 1
        if y > 170:
            break
    print(hits)
    print(len(hits))
    print(len(set(hits)))

if __name__ == '__main__':
    day17()
    #part2()
    #fire(14,-2)
