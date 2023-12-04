from collections import defaultdict
import re


def solution(cards):
    total_part1 = 0
    total_part2 = 0
    copies = defaultdict(int)
    
    for card in cards.splitlines():
        numbers = card.split(':')[1].split('|')
        card_number = int(card.split(':')[0].split( )[1])
        numbers_left = numbers[0]
        numbers_right = numbers[1]
        numbers_left = set(numbers_left.split())
        numbers_right = set(numbers_right.split())

        print('-----------------' + str(card_number) + '---------------')
              
        #part 1
        res = len(numbers_left & numbers_right)
        if(res>0):
            cards_value = 2 ** (res-1)
            print('has ' + str(res) + ' elements in common, therefore adding '+ str(cards_value) +' to the total for part 1')
            total_part1 += cards_value

        #part 2

        #when iterating over cards - count origin first card
        copies[card_number] = copies[card_number] + 1 
        print('*Card ' + str(card_number) + ' has ' + str(copies[card_number]) + ' copies')
        print('\n')


        #following cards added due to matches
        for i in range(copies[card_number]): 
            for following_cards in range(int(card_number)+1, int(card_number)+1+res):
                copies[following_cards] = copies[following_cards] + 1
                print('Card ' + str(following_cards) + ' has ' + str(copies[following_cards]) + ' copies')
        
    for card_number, count in copies.items():
        total_part2 += count

    return total_part1,total_part2


if __name__ == "__main__":
    with open("day4/test_input.txt", "r") as f:
        part1, part2 = solution(f.read())
        print(f"Part 1: {part1}")
        print(f"Part 2: {part2}")