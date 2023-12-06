
def solution(inputstring):
    return 0,0

if __name__ == "__main__":
    with open("day 5/input.txt", "r") as f:
        part1, part2 = solution(f.read())
        print(f"Part 1: {part1}")
        print(f"Part 2: {part2}")