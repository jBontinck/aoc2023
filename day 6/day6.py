def get_count_of_record_breaking_attempts(game_duration,record):
    return len(list(filter(lambda x: x > record, list(map(lambda hold: (hold*1)*(game_duration-hold), range(0, game_duration))))))


def solution(inputstring):
    time = list(map(lambda x: x.strip(),inputstring.splitlines()[0].split()))
    duration = list(map(lambda x:x.strip(), inputstring.splitlines()[1].split()))

    print(time)
    total_part1 = 1
    for i in range(1,len(time)):
        total_part1 *= get_count_of_record_breaking_attempts(int(time[i]),int(duration[i]))

    time = ''.join(time[1:]) 
    duration = ''.join(duration[1:])
    total_part2 = get_count_of_record_breaking_attempts(int(time),int(duration))


    return total_part1,total_part2

if __name__ == "__main__":
    with open("day 6/input.txt", "r") as f:
        part1, part2 = solution(f.read())
        print(f"Part 1: {part1}")
        print(f"Part 2: {part2}")