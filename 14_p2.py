f = open('14input.txt', 'r')
txt = f.readlines()
import copy as cp

polymer = '#' + txt[0].strip('\n') + '#'
pair_insertion_rules = {}
for i, line in enumerate(txt[2:]):
    find, add = line.split(' -> ')
    pair_insertion_rules[find] = add.strip()

group_frequency = {}
for char1, char2 in zip(polymer[0:-1], polymer[1:]):
    group_frequency[char1+char2] = 1
print(group_frequency)
    
for i in range(1,11):
    new_frequency = {}
    for group in group_frequency:
        for rule in pair_insertion_rules:
            if rule == group:
                if group[0] + pair_insertion_rules[rule] in new_frequency:
                    new_frequency[group[0] + pair_insertion_rules[rule]] += group_frequency[group] 
                else:
                    new_frequency[group[0] + pair_insertion_rules[rule]] = group_frequency[group]
                if pair_insertion_rules[rule] + group[1] in new_frequency:
                    new_frequency[pair_insertion_rules[rule] + group[1]] += group_frequency[group] 
                else:
                    new_frequency[pair_insertion_rules[rule] + group[1]] = group_frequency[group]
        if group not in pair_insertion_rules:
                new_frequency[group] = group_frequency[group]
    print(i, new_frequency)
    group_frequency = cp.copy(new_frequency)


character_frequency = {}
for pos, (char1, char2) in enumerate(group_frequency):
    if pos > 0:
        if char1 not in character_frequency:
            character_frequency[char1] = group_frequency[char1 + char2]
        else:
            character_frequency[char1] += group_frequency[char1 + char2]
print(character_frequency)
    
value_list = list(character_frequency.values())
print(max(value_list) - min(value_list))

        