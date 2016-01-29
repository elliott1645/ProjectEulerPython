total = 0
i = 1
j = 1
k = 0
while i < 4000000:
    k = i + j
    if k % 2 == 0:
        total = total + k
    i = j
    j = k
    
print "Answer:", total
