from ast import literal_eval

class SNum():

    def __init__(self,v,l,r,p,isleft):
        self.v = v
        self.l = l
        self.r = r
        self.p = p
        self.isleft = isleft
    
    def add_to_left(num):
        print("adding to left:",num.to_list())
        def add_to_rightmost(val,n):
            print(val.to_list())
            if val.v is not None:
                val.v += n
            else:
                add_to_rightmost(val.r,n)
        n = num.l.v
        print("my leftval is",n)
        if not num.isleft:
            print("num.p")
            num.p.tree_show()
            add_to_rightmost(num.p.l,n)
        elif not num.p.isleft:
            add_to_rightmost(num.p.p.l,n)
        elif not num.p.p.isleft:
            add_to_rightmost(num.p.p.p.l,n)
        elif not num.p.p.p.isleft:
            add_to_rightmost(num.p.p.p.p.l,n)

    def add_to_right(num):
        def add_to_leftmost(val,n):
            print(val.to_list())
            if val.v is not None:
                val.v += n
            else:
                add_to_leftmost(val.l,n)
        n = num.r.v
        print("my rightval is",n)
        if num.isleft:
            print("one layer up")
            num.p.tree_show()
            add_to_leftmost(num.p.r,n)
        elif num.p.isleft:
            print('two layers up')
            add_to_leftmost(num.p.p.r,n)
        elif num.p.p.isleft:
            print('three layers up')
            add_to_leftmost(num.p.p.p.r,n)
        elif num.p.p.p.isleft:
            print('four layers up')
            add_to_leftmost(num.p.p.p.p.r,n)

    def to_list(self):
        if self.v is not None:
            return self.v
        else:
            return [self.l.to_list(),self.r.to_list()]

    def tree_show(self,spaces=0):
        print(" "*spaces + "tree node")
        if self.v is not None:
            print(" "*spaces+"v:"+str(self.v))
        else:
            if self.l:
                self.l.tree_show(spaces+4)
            else:
                print(" " * (spaces+4) + "Missing l")
            if self.r:
                self.r.tree_show(spaces+4)
            else:
                print(" " * (spaces+4) + "Missing r")

    def explode(self,depth=0):
        #return if explosion happened
        did_explode = False
        if depth < 4:
            print('==================')
            print("depth is:",depth)
            print("I am:",self.to_list())
            print('==================')
            if self.l:
                did_explode = self.l.explode(depth+1) or did_explode
                if did_explode:
                    return True
            if self.r:
                did_explode = self.r.explode(depth+1) or did_explode
        elif self.v is None:
            print("going to explode!! i am:",self.to_list())
            self.add_to_left()
            print("Finished adding to left!")
            self.add_to_right()
            if self.isleft:
                self.p.l = SNum(0,None,None,self.p,True)
            else:
                self.p.r = SNum(0,None,None,self.p,False)
            did_explode = True
        return did_explode

    def top_level_explode(self):
        if self.p is None:
            self.explode()
        else:
            self.p.top_level_explode()

    def split(self):
        did_split = False
        print('splitting:',self.to_list())
        if self.v is not None and self.v > 9:
            print(self.v)
            newlist = None
            if self.v % 2 == 0:
                newlist = (self.v/2,self.v/2)
            else:
                newlist = (self.v//2,self.v//2 + 1)
            if self.isleft:
                self.p.l = SNum(None,None,None,self.p,True)
                self.p.l.l = SNum(newlist[0],None,None,self.p.l, True)
                self.p.l.r = SNum(newlist[1],None,None,self.p.l, False)
            else:
                self.p.r = SNum(None,None,None,self.p,False)
                self.p.r.l = SNum(newlist[0],None,None,self.p.r, True)
                self.p.r.r = SNum(newlist[1],None,None,self.p.r, False)
            did_split = True
            self.top_level_explode()
        elif self.v is None:
            print("left:",self.l.to_list())
            did_split = self.l.split() or did_split
            if did_split:
                return True
            did_split = self.r.split() or did_split
        return did_split

    def mag(self):
        if self.v is not None:
            return self.v
        return 3*self.l.mag() + 2*self.r.mag()
    
    def copy(self):
        if self.v is not None:
            return SNum(self.v,None,None,None,None)
        else:
            lc = self.l.copy()
            rc = self.r.copy()
            new = SNum(None,lc,rc,None,None)
            new.l.p = new
            new.l.isleft = True
            new.r.p = new
            new.r.isleft = False
            return new

def add(snum1,snum2):
    snum1.isleft = True
    snum2.isleft = False
    new_snum = SNum(None,snum1,snum2,None,None)
    snum1.p = new_snum
    snum2.p = new_snum
    cont = True
    while cont:
        cont = False
        did = new_snum.explode()
        if did:
            cont = True
            continue
        did = new_snum.split()
        if did:
            cont = True
    return new_snum


    
def add_list(l):
    cur = l.pop(0)
    for num in l:
        cur = add(cur,num)
    return cur


def snum_from_list(l,isleft=None):
    if not isinstance(l,list):
        return SNum(l,None,None,None,isleft)
    root = SNum(None,None,None,None,isleft)
    left = l[0]
    right = l[1]
    lnum = snum_from_list(left,True)
    rnum = snum_from_list(right,False)
    lnum.p = root
    rnum.p = root
    root.l = lnum
    root.r = rnum
    return root

def part2():
    data = [l.strip() for l in open('input.txt').readlines()]
    nums = [snum_from_list(literal_eval(n)) for n in data]
    largest_mag = 0
    for x in range(len(nums)):
        for y in range(len(nums)):
            if x == y:
                continue
            num1 = nums[x].copy()
            num2 = nums[y].copy()
            mag = add(num1,num2).mag()
            if mag > largest_mag:
                largest_mag = mag
    print(largest_mag)

def day18():
    data = [l.strip() for l in open('input.txt').readlines()]
    nums = [snum_from_list(literal_eval(n)) for n in data]

    for num in nums:
        print(num.to_list())

    print("****************")

    #test_explode = snum_from_list([[[[[9,8],1],2],3],4])
    #print(test_explode.to_list())
    #test_explode.explode()
    #print(test_explode.to_list())
    #test_explode = snum_from_list([7,[6,[5,[4,[3,2]]]]])
    #print(test_explode.to_list())
    #test_explode.explode()
    #print(test_explode.to_list())
    #test_explode = snum_from_list([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])
    #print(test_explode.to_list())
    #test_explode.explode()
    #print(test_explode.to_list())

    print("SPLIT TEST:")
    test_split = snum_from_list([[[[0,7],4],[15,[0,13]]],[1,1]])
    print(test_split.to_list())
    test_split.split()
    print(test_split.to_list())
    test_split.explode()
    print(test_split.to_list())
    test_split.explode()
    print(test_split.to_list())
    test_split.explode()
    print(test_split.to_list())
    #test_split.split()
    #print(test_split.to_list())
    #test_split.explode()
    #print(test_split.to_list())

    #test_explode = snum_from_list([[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]])
    #print(test_explode.to_list())
    #test_explode.explode()
    #print(test_explode.to_list())

    res = add_list(nums)
    print(res.to_list())
    print(res.mag())


if __name__ == '__main__':
    #day18()
    part2()
