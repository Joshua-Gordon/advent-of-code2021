from sys import exit

def hex2bin(h):
    h=h.replace("0" , "0000")
    h=h.replace("1" , "0001")
    h=h.replace("2" , "0010")
    h=h.replace("3" , "0011")
    h=h.replace("4" , "0100")
    h=h.replace("5" , "0101")
    h=h.replace("6" , "0110")
    h=h.replace("7" , "0111")
    h=h.replace("8" , "1000")
    h=h.replace("9" , "1001")
    h=h.replace("A" , "1010")
    h=h.replace("B" , "1011")
    h=h.replace("C" , "1100")
    h=h.replace("D" , "1101")
    h=h.replace("E" , "1110")
    h=h.replace("F" , "1111")
    return h

class Packet():

    def __init__(self,ver,ident,val,subpackets,packetlen):
        self.ver = ver
        self.ident = ident
        self.val = val
        self.subpackets = subpackets
        self.packetlen = packetlen

    def ver_count(self):
        if len(self.subpackets) == 0:
            return self.ver
        else:
            count = self.ver
            for s in self.subpackets:
                count += s.ver_count()
            return count

    def show(self,spaces=0):
        print(" "*spaces + "Packet (ver ",self.ver,"):")
        print(" "*spaces + " -id=",self.ident)
        if self.val:
            print(" "*spaces + " -val=",self.val)
        elif self.subpackets:
            for s in self.subpackets:
                print(" "*spaces + "Subpacket:")
                s.show(spaces+4)


def part2():
    data = open('input.txt').read().strip()
    bin_str = hex2bin(data)
    bits = list(bin_str)
    print(bits)
    pack = parse_packet(bits)
    pack.show()
    print(pack.ver_count())
    print(evalpacket(pack))

def evalpacket(pack):
    if pack.ident == 4:
        return pack.val
    elif pack.ident == 0:
        return sum(map(evalpacket,pack.subpackets))
    elif pack.ident == 1:
        prod = 1
        for s in pack.subpackets:
            prod *= evalpacket(s)
        return prod
    elif pack.ident == 2:
        return min(map(evalpacket,pack.subpackets))
    elif pack.ident == 3:
        return max(map(evalpacket,pack.subpackets))
    elif pack.ident == 5:
        e1 = evalpacket(pack.subpackets[0])
        e2 = evalpacket(pack.subpackets[1])
        return 1 if e1 > e2 else 0
    elif pack.ident == 6:
        e1 = evalpacket(pack.subpackets[0])
        e2 = evalpacket(pack.subpackets[1])
        return 1 if e1 < e2 else 0
    elif pack.ident == 7:
        e1 = evalpacket(pack.subpackets[0])
        e2 = evalpacket(pack.subpackets[1])
        return 1 if e1 == e2 else 0


def get_literal(bits_helper):
    def next_chunk(bits):
        chunk = bits[:5]
        if chunk[0] == '0':
            return chunk[1:],5
        else:
            n,b = next_chunk(bits[5:])
            return chunk[1:] + n, b+5
    bits, num = next_chunk(bits_helper)
    return int(''.join(bits),2), num

def parse_packet(bits):
    packetlen = 0
    def munch(i):
        nonlocal bits
        nonlocal packetlen
        head = bits[:i]
        bits = bits[i:]
        packetlen+=i
        return head
    def bin2int(bin_list):
        return int(''.join(bin_list),2)
    def readbin(i):
        return bin2int(munch(i))

    ver = readbin(3)
    typ = readbin(3)
    print(ver)
    print(typ)

    if typ == 4:
        litbits = []
        section = [1]
        while section[0] != '0':
            section = munch(5)
            litbits.extend(section[1:])
        lit = bin2int(litbits)
        return Packet(ver,typ,lit,[],packetlen)
    else:
        lentype = munch(1)[0]
        print("lentype:",lentype)
        if lentype == '0':
            subpackets = []
            subpackets_length = readbin(15)
            subpackets_bits = munch(subpackets_length)
            while subpackets_length > 0:
                pack = parse_packet(subpackets_bits)
                subpackets_length -= pack.packetlen
                subpackets_bits = subpackets_bits[pack.packetlen:]
                print("Parsed subpacket with length",pack.packetlen)
                subpackets.append(pack)
            return Packet(ver,typ,None,subpackets,packetlen)
        elif lentype == '1':
            subpackets = []
            num_subpackets = readbin(11)
            while num_subpackets > 0:
                pack = parse_packet(bits)
                print('Parsed subpacket,',num_subpackets-1,"remaining")
                bits = bits[pack.packetlen:]
                packetlen += pack.packetlen
                num_subpackets -= 1
                subpackets.append(pack)
            return Packet(ver,typ,None,subpackets,packetlen)

def day16():
    data = open('input.txt').read().strip()
    bin_str = hex2bin(data)
    bits = list(bin_str)
    print(bits)
    pack = parse_packet(bits)
    pack.show()
    print(pack.ver_count())

if __name__ == '__main__':
    #day16()
    part2()
