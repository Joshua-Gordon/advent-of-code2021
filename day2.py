def day2():
    data = open('input.txt').readlines()
    h = 0
    d = 0
    for line in data:
        command,val = line.split()
        if command == "forward":
            h += int(val)
        elif command == "up":
            d -= int(val)
        elif command == "down":
            d += int(val)
    print(h*d)

def part2():
    data = open('input.txt').readlines()
    h = 0
    d = 0
    a = 0
    for line in data:
        command,val = line.split()
        if command == "forward":
            h += int(val)
            d += a*int(val)
        elif command == "up":
            a -= int(val)
        elif command == "down":
            a += int(val)
    print(h*d)
    

if __name__ == '__main__':
    day2()
    part2()
