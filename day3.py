
def part2():
    lines = open('input.txt').readlines()
    bit = 0
    while len(lines) > 1:
        ones = []
        zeros = []
        for line in lines:
            val = line[bit]
            if val == '1':
                ones.append(line)
            else:
                zeros.append(line)
        if len(ones) >= len(zeros):
            lines = ones
        else:
            lines = zeros
        bit += 1
    o2 = int(''.join(lines[0]),2)
    lines = open('input.txt').readlines()
    bit = 0
    while len(lines) > 1:
        ones = []
        zeros = []
        for line in lines:
            val = line[bit]
            if val == '1':
                ones.append(line)
            else:
                zeros.append(line)
        if len(ones) < len(zeros):
            lines = ones
        else:
            lines = zeros
        bit += 1
    co2 = int(''.join(lines[0]),2)
    print(o2*co2)




def day3():
    lines = open('input.txt').readlines()
    gamma = []
    epsilon = []
    for bit in range(0,12):
        total = 0
        for line in lines:
            if line[bit] == '1':
                total += 1
        if total > len(lines)/2:
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')
    gbitstring = ''.join(gamma)
    ebitstring = ''.join(epsilon)
    power = int(gbitstring,2) * int(ebitstring,2)
    print(power)


if __name__ == "__main__":
    day3()
    part2()
