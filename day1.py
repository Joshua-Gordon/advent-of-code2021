def day1():
    data = [int(n) for n in open('input.txt').readlines()]
    count = 0
    for i,j in zip(data,data[1:]):
        if j > i:
            print(i,j)
            count += 1
    print(count)

def part2():
    data = [int(n) for n in open('input.txt').readlines()]
    count = 0
    sums = []
    for i,j,k in zip(data,data[1:],data[2:]):
        sums.append(i+j+k)
    for i,j in zip(sums,sums[1:]):
        if j > i:
            print(i,j)
            count += 1
    print(count)


if __name__ == '__main__':
    day1()
    part2()
