from collections import Counter

class Tree():

    def __init__(self,name,c,indirect):
        self.name = name
        self.c = c
        self.indirect=indirect

    def show(self, spaces=0):
        print(" "*spaces + self.name,self.indirect)
        for tree in self.c:
            tree.show(spaces+4)

def halting_oracle(node1,node2):
    #checks if node1 is a parent of node2
    if node1.indirect:
        return halting_oracle(node1.indirect,node2)
    if node1 is node2:
        return True
    if len(node1.c) == 0:
        return False
    for tree in node1.c:
        if halting_oracle(tree,node2):
            return True
    return False


def search_for(name,root,start):
    #prevent recursion by never returning a node that is a parent of the one in question
    if root.name == name:
        return root
    for tree in root.c:
        ans = search_for(name,tree,start)
        if ans and not halting_oracle(ans,start):
            return ans

def get_counts(root,counts={}):
    if root.indirect:
        return get_counts(root.indirect,counts)
    if root in counts:
        return counts
    if len(root.c) == 0:
        l1 = root.name[0]
        l2 = root.name[1]
        counts[root] = Counter(l1) + Counter(l2)
        return counts
    else:
        print(counts)
        for tree in root.c:
            new_counter = get_counts(tree,counts)
            counts += new_counter
        return counts

def do_round(rules,root,whole_thing):
    if root.indirect:
        return
    if len(root.c) == 0:
        # make children but search for an indirection
        pat = root.name
        for ((p1,p2),out) in rules:
            if p1 == pat[0] and p2 == pat[1]:
                c1 = ''.join([pat[0],p1])
                node = search_for(c1,whole_thing,root)
                if node:
                    root.c.append(Tree(c1,[],node))
                else:
                    root.c.append(Tree(c1,[],None))
                c2 = ''.join([p1,p2])
                node = search_for(c2,whole_thing,root)
                if node:
                    root.c.append(Tree(c2,[],node))
                else:
                    root.c.append(Tree(c2,[],None))
                c3 = ''.join([p2,pat[1]])
                node = search_for(c3,whole_thing,root)
                if node:
                    root.c.append(Tree(c3,[],node))
                else:
                    root.c.append(Tree(c3,[],None))
    else:
        for tree in root.c:
            do_round(rules,tree,whole_thing)


def part2():
    data = open('input.txt').readlines()
    poly = data.pop(0).strip()
    data.pop(0)
    rules = []
    for line in data:
        pat,out = line.strip().split(' -> ')
        rules.append((pat,out))
    
    root = Tree('',[],None)
    for idx,val in enumerate(poly):
        if idx < len(poly)-1:
            root.c.append(Tree(''.join([val,poly[idx+1]]),[],None))
    root.show()
    for i in range(40):
        do_round(rules,root,root)

    root.show()

    print(get_counts(root))
    

def real_part_2():
    data = open('input.txt').readlines()
    poly = data.pop(0).strip()
    data.pop(0)
    rules = []
    for line in data:
        pat,out = line.strip().split(' -> ')
        rules.append((pat,out))

    pairs = []
    for idx,val in enumerate(poly):
        if idx < len(poly)-1:
            pairs.append(''.join([val,poly[idx+1]]))
    count = Counter(pairs)
    letters = Counter(poly)
    print(count)
    import re
    p10 = re.compile(r"^10*$")
    for i in range(40):
        if p10.match(str(i)):
            print(i)
        newcount = Counter()
        for name,val in count.items():
            for ((p1,p2),out) in rules:
                if p1 == name[0] and p2 == name[1]:
                    newcount[''.join([name[0],out])] += val
                    newcount[''.join([out,name[1]])] += val
                    letters[out] += val
        count = newcount
    print(newcount)
    print(letters)


def day14():
    data = open('input.txt').readlines()
    poly = data.pop(0).strip()
    data.pop(0)
    rules = []
    for line in data:
        pat,out = line.strip().split(' -> ')
        rules.append((pat,out))

    for i in range(10):
        newpoly = []
        for idx,val in enumerate(poly):
            newpoly.append(val)
            if idx < len(poly)-1:
                for ((p1,p2),out) in rules:
                    if p1 == val and p2 == poly[idx+1]:
                        newpoly.append(out)
        poly = newpoly
        print(poly)

    c = Counter(poly)
    print(c)


if __name__ == '__main__':
    #day14()
    #part2()
    real_part_2()
