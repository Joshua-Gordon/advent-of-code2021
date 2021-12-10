
openc = "({[<"
close = ")}]>"

scoreorder = "([{<"

def part2():
    data = open('input.txt').readlines()
    scores = []
    for line in data:
        keep = True
        score = 0
        stack = []
        for c in line:
            if c in openc:
                stack.append(c)
            if c in close:
                latest = stack[-1]
                if close.index(c) != openc.index(latest):
                    keep = False
                    break
                else:
                    stack.pop()
        print(stack)
        if keep:
            for i in range(1,len(stack)+1):
                score *= 5
                char = stack[len(stack) - i]
                score += 1+scoreorder.index(char)
            scores.append(score)
    scores = sorted(scores)
    print(scores)
    print(len(scores))
    print(scores[len(scores)//2])

dscore = {")":3,"]":57,"}":1197,">":25137}

def day10():
    data = open('input.txt').readlines()
    score = 0
    for line in data:
        stack = []
        for c in line:
            if c in openc:
                stack.append(c)
            if c in close:
                latest = stack[-1]
                if close.index(c) != openc.index(latest):
                    print(line)
                    print(stack)
                    print(c)
                    score += dscore[c]
                    break
                else:
                    stack.pop()
    print(score)

if __name__ == '__main__':
    #day10()
    part2()
