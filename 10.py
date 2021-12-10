f = open('10input.txt', 'r')
txt = f.readlines()

values = {')': 3, ']': 57, '}': 1197, '>': 25137}
tot_value = 0
incomplete_lines = []
for line in txt:
    while '()' in line or '[]' in line or '{}' in line or '<>' in line:
        line = line.replace('()', '').replace('[]','').replace('{}','').replace('<>','')
    row_value = 0
    for char in line:
        if char in [')', ']', '}', '>'] and row_value == 0:
            row_value = values[char]
    tot_value += row_value
    if row_value == 0:
        incomplete_lines.append(line)
    
print(tot_value)
       
scores = {'(': 1, '[': 2, '{': 3, '<': 4}
tot_score = []
for line in incomplete_lines:
    line_score = 0
    line = line.strip('\n')
    for i in range(len(line)-1, -1, -1):
        line_score = line_score*5 + scores[line[i]]
    tot_score.append(line_score)
        
s = sorted(tot_score)
print( s[(len(s)-1)//2] )
      
            
        
    