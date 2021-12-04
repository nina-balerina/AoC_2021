
f = open('04input.txt', 'r')
txt = f.readlines()
import numpy as np

# Input
 
numbers2draw = [int(x) for x in txt[0].split(',')]
n = int((len(txt)-1)/6)

del txt[0]
boards = np.zeros([5, 5, n])
board_number = -1
j = 0
for line in txt:
    if line=='\n':
        board_number += 1
        j = 0
    else:
        boards_raw = line.split()
        boards[j,:,board_number] = boards_raw[:]
        j += 1

# Playing BINGO:
    
winner = 0 
all_winning= 0 
crossed = np.zeros([5, 5, n])  
winning_board = np.zeros([n])  
for l in range(len(numbers2draw)):
    for k in range(n):
        for i in range(5):
            for j in range(5):
                if boards[i,j,k] == numbers2draw[l]:
                    crossed[i, j, k] = 1
                if sum(crossed[i,:,k]) == 5 or sum(crossed[:,j,k]) == 5:
                    winning_board[k] = 1
                    won_boards = sum(winning_board[:])
                    if winner == 0:
                        print( sum(sum(boards[:,:,k]*(1-crossed[:,:,k]))) * numbers2draw[l] )
                        winner = 1     
                    if all_winning== 0 and won_boards == n:
                        print( sum(sum(boards[:,:,k]*(1-crossed[:,:,k]))) * numbers2draw[l] )
                        all_winning= 1
