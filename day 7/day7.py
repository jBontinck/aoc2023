from typing import List
from itertools import groupby


class Hand():
    def __init__(self, cards, bid):
        self.cards = cards
        self.proxyvalue = self.__get_proxy_value()
        self.type = self.__get_type()
        print(self.type)
        self.bid = bid
        self.rank = 0
    def __get_proxy_value(self):
        pr = []
        for card in self.cards:
            if card == 'A':
                pr.append(14)
            elif card == 'K':
                pr.append(13)
            elif card == 'Q':
                pr.append(12)
            elif card == 'J':
                #pr.append(11) #part1
                pr.append(1)
            elif card == 'T':
                pr.append(10)
            else:
                pr.append(int(card))
        return pr
    
    def __most_unique(self,List):
        return max(set(List), key = List.count)
    
    def __get_type(self)->int:
        s = len(set(self.cards))
        cpy = self.cards
        counts = [len(list(group)) for key, group in groupby(sorted(cpy))]
        print(counts)
        number_of_pairs = len(list(filter(lambda x: x==2,counts)))
        number_of_threes = len(list(filter(lambda x: x== 3,counts)))
        js = self.cards.count('J')


        if(s==1):
            return 7 # 5 of a kind
        elif(s==2):
            if(js>0): return 7
            if(number_of_threes == 1):
                return 5 #full house
            else:
                return 6 #four of a kind
        elif(s == 3):
            if(number_of_pairs == 2):
                if(js == 1): return 5
                if(js ==2):return 6
                if(js==3): return 7
                return 3 #two pair
            else:
                if(js ==1): return 6
                if(js ==2): return 6
                if(js ==3): return 6
                return 4 #three of a kind
        elif(s == 4):
            if(js ==1): return 4
            if(js ==2): return 4 #unless the pair are the JJ
            return 2  #one pair
        elif(s == 5):
            if(js>0): return 2
            return 1 #high card

    def __lt__(self, other):
        return self.type < other.type  or (self.type == other.type and self.proxyvalue < other.proxyvalue)
    def __str__(self):
        return "{} {} {}\n".format(''.join(self.cards),self.type, self.bid)



class CamelCards():
    def __init__(self):
        self.hands: List[Hand] = []

    def add_hand(self, cards, bid):
        self.hands.append(Hand(cards,bid))
    
    def read_game(self, inputstring:str):
        lines = inputstring.splitlines()
        for line in lines:
            self.add_hand([*line.split()[0]],int(line.split()[1]))
    
    def get_winning(self):
        self.order_hands()
        total = 0
        for i, hand in enumerate(self.hands):
            winning = (i+1)*hand.bid
            print("{}(type {} and proxy {}) has rank {}, therefore {} times {} = {}".format("".join(hand.cards),hand.type,hand.proxyvalue,i+1,i+1,hand.bid,winning))
            total += (i+1)*hand.bid
        return total
    
    def __str__(self):
        res = ''
        for h in self.hands:
            res+= str(h)
        return res
        
    def order_hands(self):
        self.hands.sort()
    
def solution(inputstring):
    cc = CamelCards()
    cc.read_game(inputstring)

    print(cc)
    total_part1 = cc.get_winning()

    return total_part1,0

if __name__ == "__main__":
    with open("day 7/input.txt", "r") as f:
        part1, part2 = solution(f.read())
        print(f"Part 1: {part1}")
        print(f"Part 2: {part2}")