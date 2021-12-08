from constraint import *

graph = {
    0 : "abcdef",
    1 : "bc",
    2 : "abdeg",
    3 : "abcdg",
    4 : "bcfg",
    5 : "acdfg",
    6 : "acdefg",
    7 : "abc",
    8 : "abcdefg",
    9 : "abcdfg",
}
inv = {v:k for k,v in graph.items()}

quick_lookup = {2 : 1, 4 : 4, 3 : 7, 5 : [2,3,5], 6 : [0,6,9]}

def str_intersect(s1,s2):
    return ''.join(sorted(set(s1) & set(s2), key=s1.index))

def part2():
    data = open('input.txt').readlines()
    total = 0
    for line in data:
        uniq,_,pattern = line.partition("|")
        displays = pattern.strip().split()
        constraints = {}
        for u in uniq.strip().split():
            if len(u) in [2,3,4]:
                for letter in u:
                    if letter in constraints:
                        constraints[letter] = str_intersect(constraints[letter],graph[quick_lookup[len(u)]])
                    else:
                        constraints[letter] = graph[quick_lookup[len(u)]]
        for l in "abcdefg":
            if l not in constraints:
                constraints[l] = "abcdefg"
        p = Problem()
        for key,val in constraints.items():
            p.addVariable(key,val)
        p.addConstraint(AllDifferentConstraint())
        sols = p.getSolutions()
        for sol in sols: 
            try:
                val = []
                for d in displays:
                    s = []
                    for letter in d:
                        s.append(sol[letter])
                    num = inv[''.join(sorted(s))]
                    val.append(str(num))
                print(val)
                sval = ''.join(val)
                print(sval)
                total += int(''.join(val))
                break
            except KeyError:
                pass
    print(total)



def day8():
    data = open('input.txt').readlines()
    total = 0
    for line in data:
        uniq,_,pattern = line.partition("|")
        displays = pattern.strip().split()
        print(displays)
        for d in displays:
            if len(d) in [2,3,4,7]:
                total += 1
    print(total)
    

if __name__ == '__main__':
    #day8()
    part2()
