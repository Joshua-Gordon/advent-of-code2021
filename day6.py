
def part2():
    data = [int(c) for c in open("input.txt").read().split(",") if len(c)>0]
    print(data)
    fish = [0]*9
    for i in data:
        fish[i] += 1
    for day in range(256):
        newfish = [0]*9
        for idx,f in enumerate(fish):
            if idx == 0:
                newfish[8] += f
                newfish[6] += f
            else:
                newfish[idx-1] += f
        fish = newfish
        print(day)
        print(fish)
    print(fish)
    print(sum(fish))

def day6():
    data = [int(c) for c in open("input.txt").read().split(",") if len(c)>0]
    print(data)
    fish = [0]*9
    for i in data:
        fish[i] += 1
    for day in range(80):
        newfish = [0]*9
        for idx,f in enumerate(fish):
            if idx == 0:
                newfish[8] += f
                newfish[6] += f
            else:
                newfish[idx-1] += f
        fish = newfish
        print(day)
        print(fish)
    print(fish)
    print(sum(fish))

if __name__ == '__main__':
    day6()
    part2()
