def solution(inputstring):
    total_part1=0
    total_part2=0
    histories = inputstring.splitlines()
    for historie in histories:
        total_part1 += get_next_value(historie)
        total_part2 += get_next_value(historie,False)

    return total_part1,total_part2

def get_next_value(historie, forward:bool=True):
    print("-------" + historie)
    next_value = 0
    h = list(map(lambda x: int(x),historie.split()))
    differences = []
    difference = h
    print(difference)
    while(not(len(set(difference)) == 1 and difference[0]==0)):
        differences.append(difference)
        difference = [difference[i+1]-difference[i] for i in range(len(difference)-1)]
    differences.append(difference)

    print(differences)
    #------------------next value (forward)
    nxt = 0
    for i in range(len(differences)-1,-1,-1):
        print(i)
        if(forward):
            nxt = nxt + differences[i][-1]
        else:
            nxt = differences[i][0] - nxt

        print("-->" + str(nxt))
    return nxt



if __name__ == "__main__":
    with open("day 9/input.txt", "r") as f:
        part1, part2 = solution(f.read())
        print(f"Part 1: {part1}")
        print(f"Part 2: {part2}")