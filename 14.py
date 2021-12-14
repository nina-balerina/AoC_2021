f = open('14input.txt', 'r')
txt = f.readlines()
import copy as cp

polymer = txt[0].strip('\n')
pair_insertion_rules = {}
for i, line in enumerate(txt[2:]):
    find, add = line.split(' -> ')
    pair_insertion_rules[find] = add.strip()
  
for i in range(1,11):
    new_polymer = ''
    for char1, char2 in zip(polymer[0:len(polymer)], polymer[1:]):
        if new_polymer=='':
            new_polymer = char1
        for rule in pair_insertion_rules:
            if rule == char1+char2:
                new_polymer = new_polymer +  pair_insertion_rules[rule] + char2
        if new_polymer[-1] != char2:
            new_polymer += char2
    polymer = cp.copy(new_polymer)

character_frequency = {}
for rule in pair_insertion_rules:
    character_frequency[pair_insertion_rules[rule]] = polymer.count(pair_insertion_rules[rule])
    
value_list = list(character_frequency.values())
print(max(value_list) - min(value_list))

        