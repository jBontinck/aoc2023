from math import gcd


class Mapping():
    def __init__(self, inputstr:str) -> None:
        self.F = inputstr.split('=')[0].strip()
        raw = inputstr.split("=")[1].strip().split(',')
        self.left = raw[0][1:].strip()
        self.right = raw[1][:-1].strip()
    
    def __str__(self) -> str:
        return 'from {} go left({}) or right({})'.format(self.F,self.left,self.right)
    
    def is_XXA_node(self)->bool:
        return self.F.endswith('A')

def lcm(xs):
  ans = 1
  for x in xs:
    ans = (x*ans)//gcd(x,ans)
  return ans

def solution(inputstring:str):
    total_part1 = 0
    total_part2 = 0

    #parsing
    lines = inputstring.splitlines()
    source_directions = [*lines[0]]
    mappings = lines[2:]
    #initialising
    route = dict()
    route['L']= dict()
    route['R']= dict()
    start_nodes =[]
    for mapping in mappings:
        m = Mapping(mapping)
        route['L'][m.F]=m.left
        route['R'][m.F] = m.right
        if(m.is_XXA_node()):
            start_nodes.append(m.F)
    
    # #part1
    # start = start_nodes[0]
    # directions = list(source_directions)
    # while start!='ZZZ':
    #     dir = directions.pop(0)
    #     next = route[dir][start]
    #     print("Started at {}, went {}, ended up in {}, {} diretions left".format(start,dir,next,len(directions)))
    #     start = next
    #     total_part1+=1
    #     if(len(directions) == 0):
    #         print('refill directions')
    #         directions = list(source_directions)

    #part2
    directions = list(source_directions)
    print(start_nodes)
    T = {}
    t = 0
    while True:
        new_start_nodes = []
        for i,p in enumerate(start_nodes):
            p = route[directions[t%len(directions)]][p]
            print("Started at {}, went {}, ended up in {}, {} diretions left".format(p,directions[t%len(directions)],i,len(directions)))
            if p.endswith('Z'):
                T[i] = t+1
                if len(T) == len(start_nodes):
                    return total_part1,lcm(T.values())
            new_start_nodes.append(p)
        start_nodes = new_start_nodes
        #if all(p.endswith('Z') for p in POS):
        #  break
        t += 1

if __name__ == "__main__":
    with open("day 8/input.txt", "r") as f:
        part1, part2 = solution(f.read())
        print(f"Part 1: {part1}")
        print(f"Part 2: {part2}")