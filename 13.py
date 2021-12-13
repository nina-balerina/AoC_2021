f = open('13input.txt', 'r')
txt = f.readlines()
import numpy as np
from operator import itemgetter
import copy as cp
import matplotlib.pyplot as plt

coordinates = {}
fold_instructions = {}
empty_line_discovered = 0
folding = 0
for line in txt:
    if line=='\n':
        empty_line_discovered = 1
    if empty_line_discovered==0:
        x, y = line.split(',')
        coordinates[(int(x), int(y))] = 1
    elif empty_line_discovered==1 and line!='\n':
        folding += 1
        instruction, value = line.split('=')
        fold_instructions[folding] = (instruction.split()[2], int(value))

for i in range(1, len(fold_instructions)+1):
    key_list = list(coordinates.keys())
    new_field = {}
    if fold_instructions[i][0]=='x':
        for point in key_list:
            x, y = point
            if x <= fold_instructions[i][1]:
                new_field[x, y] = 1
            else:
                new_field[int(2*fold_instructions[i][1]-x), y] = 1
    elif fold_instructions[i][0]=='y':
        for point in key_list:
            x, y = point
            if y <= fold_instructions[i][1]:
                new_field[x, y] = 1
            else:
                new_field[x, int(2*fold_instructions[i][1]-y)] = 1
    coordinates = cp.copy(new_field)
    if i==1: print(len(coordinates)) 


x_max = int(max(coordinates, key=itemgetter(0))[0])
y_max = int(max(coordinates, key=itemgetter(1))[1])
final_field = np.zeros([x_max+1, y_max+1])
key_list = list(coordinates.keys())
for point in key_list:
    x, y = point
    final_field[point] = 10
    
plt.imshow(final_field.transpose())
 


