
import re
import sys

def split_on_empty_lines(s):
    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"
    return re.split(blank_line_regex, s.strip())

#The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.
def get_seeds(inputstring):
    pattern = r'(\d+)'
    for match in re.finditer(pattern, inputstring):
        yield match

def get_seeds_part2(inputstring):
    pattern = r'(\d+)'
    seeds = []
    for match in re.finditer(pattern, inputstring):
        #print('adding '+str(match.group()))
        seeds.append(int(match.group()))
    sublists = [seeds[i:i+2] for i in range(0, len(seeds),2)]
    for sublist in sublists:
        for i in range(0,sublist[1]):
            yield sublist[0]+i

#seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination).
#Each line within a map contains three numbers: the destination range start, the source range start, and the range length.
def map_source_to_destination(mapping_block):
    # print(mapping_block)
    splitted = mapping_block.splitlines()

    #parse first line
    first_line = splitted[0].split(' ')[0].split('-')
    destination = first_line[2]
    source = first_line[0]
    # print('Source "{}" to destination "{}" map'.format(source, destination))

    mapping = []
    #parse subsequent lines
    for i in range(1,len(splitted)):
        mapping.append(map_source_to_destination_line(source,destination, splitted[i]))
    return source,destination, mapping

def map_source_to_destination_line(source, destination,line):
    splitted_line = line.split(' ')
    source_range_start = int(splitted_line[1])
    destination_range_start = int(splitted_line[0])
    range_length = int(splitted_line[2])

    # print('\t {}-{}-{}'.format(destination_range_start,source_range_start,range_length)) 
    return destination_range_start,source_range_start,range_length


class Walker():
    def __init__(self):
        self.matrix = dict()
        self.sources = ['seed','soil','fertilizer','water','light','temperature','humidity']
        self.current_step_index = 0
        for source in self.sources:
            self.matrix[source] = []

    def add_mapping(self, source,destination, mapping):
        self.matrix[source].append(mapping) 

    def walk_seed(self, seed:int)-> int: 
        go_to_next = False
        for source in self.sources:
            #print('------------------------------------------------------------------' + source)
            for mapping in self.matrix[source]:
                for m in mapping:
                    #print(('\t checking if source {} is in interval ' + str(m)).format(seed))
                    if(int(seed) >= m[1] and int(seed) < m[1]+ m[2]): #seed bigger than source_start and smaller than source+interval, than map to destination+interval
                        seed = m[0]-m[1]+seed #new destination
                        #print('\t\t match resulting in destination number ' + str(seed))
                        self.current_step_index +=1
                        go_to_next = True
                        break #stop iterating through mappings because we have found a destination
                  
        return seed
    
    def print_walker(self):
        print(self.matrix)



def solution(raw_input):
    w = Walker()
    splits = split_on_empty_lines(raw_input)
    for i in range(1,len(splits)):
        source,destination, mapping = map_source_to_destination(splits[i])
        w.add_mapping(source,destination, mapping)

    lowest_location_part1 = 100000000000000000000
    seeds = get_seeds(splits[0])
    for seed in seeds:
        seednumber = int(seed.group())
        print('******************' + seed.group())
        location = w.walk_seed(seednumber)
        if (location < lowest_location_part1):
            lowest_location_part1 = location
    
    seeds = get_seeds_part2(splits[0])
    # for seed in seeds:
    #     print(seed)
    lowest_location_part2 = 100000000000000000000
    for seed in seeds:
        seednumber = seed
        print('******************' + str(seed))
        location = w.walk_seed(seednumber)
        if (location < lowest_location_part2):
            lowest_location_part2 = location
    
    w.print_walker()
    return lowest_location_part1,lowest_location_part2


if __name__ == "__main__":
    with open("day 5/input.txt", "r") as f:
        part1, part2 = solution(f.read())
        print(f"Part 1: {part1}")
        print(f"Part 2: {part2}")