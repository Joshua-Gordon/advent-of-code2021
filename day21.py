
class DDice():
    def __init__(self):
        self.nextval = 0
        self.numrolls = 0

    def roll(self):
        self.numrolls += 1
        self.nextval += 1
        if self.nextval == 1001:
            self.nextval = 1
            return 1
        return self.nextval 


def part2():
    universes = {}
    #universes[3,0,7,0] = 1
    universes[2,0,9,0] = 1
    p1wins = 0
    p2wins = 0
    while len(universes) > 0:
        new_universes = {}
        for universe, multiplicity in universes.items():
            p1pos,p1score,p2pos,p2score = universe
            for p1roll1 in [1,2,3]:
                for p1roll2 in [1,2,3]:
                    for p1roll3 in [1,2,3]:
                        for p2roll1 in [1,2,3]:
                            for p2roll2 in [1,2,3]:
                                for p2roll3 in [1,2,3]:
                                    p1newpos = (p1pos+p1roll1+p1roll2+p1roll3)%10
                                    p2newpos = (p2pos+p2roll1+p2roll2+p2roll3)%10
                                    if p1score + p1newpos+1 >= 21:
                                        p1wins += multiplicity
                                    elif p2score + p2newpos+1 >= 21:
                                        p2wins += multiplicity
                                    else:
                                        new_universe = (p1newpos,p1score + p1newpos+1, p2newpos, p2score+p2newpos+1)
                                        if new_universe in new_universes:
                                            new_universes[new_universe] += multiplicity
                                        else:
                                            new_universes[new_universe] = multiplicity
        print(new_universes)
        universes = new_universes
    print("p1wins:",p1wins)
    print("p2wins:",p2wins)






def day21():
    data = open('input.txt').read().splitlines()
    print(data)
    p1pos = 2
    p2pos = 9
    p1score = 0
    p2score = 0
    dice = DDice()
    while p1score < 1000 and p2score < 1000:
        p1roll = dice.roll() + dice.roll() + dice.roll()
        p1pos = (p1pos+p1roll) % 10
        p1score += p1pos+1
        if p1score >= 1000:
            break
        p2roll = dice.roll() + dice.roll() + dice.roll()
        p2pos = (p2pos+p2roll) % 10
        p2score += p2pos+1
        print("player 1 at ",p1pos+1,", player 2 at ",p2pos+1)
        print("p1score:",p1score,", p2score:",p2score)
        print(dice.numrolls)
    if p1score >= 1000:
        print(p2score * dice.numrolls)
    else:
        print(p1score * dice.numrolls)


if __name__ == '__main__':
    day21()
    part2()
