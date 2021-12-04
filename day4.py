
class Board():

    def __init__(self):
        self.columns = []
        self.rows = []
    
    def parse(self, rows_read):
        self.rows = rows_read
        for i in range(len(self.rows)):
            col = []
            for j in range(len(self.rows)):
                col.append(self.rows[j][i])
            self.columns.append(col)

    def match(self,drawn):
        for idx,col in enumerate(self.columns):
            if all(c in drawn for c in col):
                return drawn[-1]*sum([sum([val for val in other if val not in drawn]) for other in self.columns])
        for idx,row in enumerate(self.rows):
            if all(r in drawn for r in row):
                return drawn[-1]*sum([sum([val for val in other if val not in drawn]) for other in self.rows])
        return None

    def show(self):
        for r in self.rows:
            print(r)
        print()

    def showcols(self):
        for c in self.columns:
            print(c)
        print()




def part2():
    pass

def day4():
    data = open('input.txt').readlines()
    draw = [int(c) for c in data.pop(0).split(",") if len(c)>0]
    data.pop(0)
    boards = []
    read_buffer = []
    for line in data:
        if len(read_buffer) == 5:
            b = Board()
            b.parse(read_buffer)
            boards.append(b)
            b.show()
            read_buffer = []
        else:
            read_buffer.append([int(c) for c in line.split(' ') if len(c)>0])
    b = Board()
    b.parse(read_buffer)
    boards.append(b)
    b.show()
    b.showcols()
    read_buffer = []

    drawbuf = []
    while len(boards) > 1:
        drawbuf.append(draw.pop(0))
        scored = []
        for b in boards:
            score = b.match(drawbuf)
            if score:
                scored.append(b)
        for s in scored:
            boards.remove(s)
    board = boards[0]
    while True:
        drawbuf.append(draw.pop(0))
        s = board.match(drawbuf)
        if s:
            print(s)
            return

if __name__ == '__main__':
    day4()
    part2()
