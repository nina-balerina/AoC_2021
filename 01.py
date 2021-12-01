import time
start_time = time.time()

f = open('01input.txt', 'r')
txt = f.readlines()
depths = []
for a in txt:
    depths.append(int(a))

# inc = 0
dec = 0
for i in range (1,len(depths)):
    if depths[i]-depths[i-1]>0:
        dec +=1
    # elif depths[i]-depths[i-1]<0:
    #     inc +=1
print("part 1: %s" % dec)
        
sum_depths = []
for i in range (2,len(depths)):
    sum_depths.append(sum(depths[i-2:i+1]))

# sd_inc = 0
sd_dec = 0
for i in range (1,len(sum_depths)):
    if sum_depths[i]-sum_depths[i-1]>0:
        sd_dec +=1
    # elif sum_depths[i]-sum_depths[i-1]<0:
    #     sd_inc +=1
print("part 2: %s" % sd_dec)
    
print("---%s seconds..." % (time.time()-start_time))             