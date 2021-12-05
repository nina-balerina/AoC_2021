
f = open('03input.txt', 'r')
txt = f.readlines()
import copy
n = len(txt[0])

# PARTY1

def most_common(l):
    zeros = 0; ones  = 0
    for j in range(len(l)):
        if l[j]!='' and l[j][i]=='0':
            zeros +=1
        elif l[j]!='' and l[j][i]=='1':
            ones += 1
    return zeros, ones

gamma_rate = ''
epsilon_rate = ''
for i in range(12):
    zeros, ones = most_common(txt)
    if ones>zeros:
        gamma_rate = gamma_rate + '1'
        epsilon_rate += '0'
    else:
        gamma_rate = gamma_rate + '0'
        epsilon_rate += '1'

print(int(gamma_rate, 2)*int(epsilon_rate, 2))

# PARTY2

# functions:
    
def oxygen_generator_rating(zeros, ones, l):
    l_new = []
    if ones==zeros or ones>zeros:
        for j in range(len(l)):
            if l[j]!='' and l[j][i]=='1': l_new.append(l[j])
    else:
        for j in range(len(l)):
            if l[j]!='' and l[j][i]=='0': l_new.append(l[j])
    return l_new

def CO2_scrubber_rating(zeros, ones, l):
    l_new = []
    if ones==zeros or ones>zeros:
        for j in range(len(l)):
            if l[j]!='' and l[j][i]=='0': l_new.append(l[j])
    else:
        for j in range(len(l)):
            if l[j]!='' and l[j][i]=='1': l_new.append(l[j])
    return l_new

#main:
    
l1 = copy.copy(txt) 
for i in range(n):
    zeros, ones = most_common(l1)
    if (zeros+ones)>1:
        l1 = oxygen_generator_rating(zeros, ones, l1)
                
l2 = copy.copy(txt) #co2 - least common
for i in range(n):
    zeros, ones = most_common(l2)
    if (zeros+ones)>1:
        l2 = CO2_scrubber_rating(zeros, ones, l2)      
     
print( int(l1[0],2)*int(l2[0],2)  )              
        
    
