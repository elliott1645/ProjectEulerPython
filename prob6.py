# i = 0  - Unnesecary to instantiate and initialize variables in python
# j = 0
# a = 0

sumOfElements = 0
sumOfSquares = 0

# Calculate the sum of all integers squared 1 through 100
for element in range (1,101):
    square = element * element
    sumOfSquares += square

# Calculate the sum of all integers 1 through 100 (Then Square it on line 17)
for element in range (1,101):
    sumOfElements += element
    
squareOfSums = sumOfElements * sumOfElements

answer = squareOfSums - squareOfSums

print(answer) # Now it will run in python 2 and 3!
