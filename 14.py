f = open('14input.txt', 'r')
txt = f.readlines()
import copy as cp
from collections import defaultdict as dd 

polymer = '#' + txt[0].strip('\n') + '#'
pair_insertion_rules = {}
for i, line in enumerate(txt[2:]):
    find, add = line.split(' -> ')
    pair_insertion_rules[find] = add.strip()

group_frequency = dd(int)
for char1, char2 in zip(polymer[0:-1], polymer[1:]):
    group_frequency[char1+char2] += 1
    
for i in range(1,41):
    new_frequency = dd(int)
    for group in group_frequency:
        if group in pair_insertion_rules:
            new_frequency[group[0] + pair_insertion_rules[group]] += group_frequency[group] 
            new_frequency[pair_insertion_rules[group] + group[1]] += group_frequency[group] 
        if group not in pair_insertion_rules:
                new_frequency[group] = group_frequency[group]
    group_frequency = cp.copy(new_frequency)
    if i == 10:
        part1 = group_frequency

character_frequency = dd(int)
for pos, (char1, char2) in enumerate(part1):
    if pos > 0:
        character_frequency[char1] += part1[char1 + char2]
    
value_list = list(character_frequency.values())
print(max(value_list) - min(value_list))   

character_frequency = dd(int)
for pos, (char1, char2) in enumerate(group_frequency):
    if pos > 0:
        character_frequency[char1] += group_frequency[char1 + char2]
    
value_list = list(character_frequency.values())
print(max(value_list) - min(value_list))     