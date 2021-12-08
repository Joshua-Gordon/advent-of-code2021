import numpy as np

def part2():
    data = [int(c) for c in open('input.txt').read().split(",") if len(c)>0]
    med = np.round(sum(data)/len(data))
    print(med)
    fueltotals = []
    for med in range(0,1000):
        fueltotal = 0
        for d in data:
            dist = abs(d - med)
            for i in range(int(dist)+1):
                fueltotal += i
        fueltotals.append(fueltotal)
    print(min(fueltotals))

def day7():
    data = [int(c) for c in open('input.txt').read().split(",") if len(c)>0]
    med = np.median(data)
    print(med)
    fuels = [abs(c - med) for c in data]
    print(sum(fuels))
    pass

if __name__ == '__main__':
    day7()
    part2()
