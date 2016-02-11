i = 0
j = 0
a = 0
b = 0
sum1 = 0
sum2 = 0
answer = 0

for i in range (1,101):
    a = i*i
    sum1 += a

for j in range (1,101):
    b += j
    
sum2 = b*b

answer = sum2 - sum1

print answer
