import time
a = 3
b = 5
sum = 0
startTime = time.time()
for i in range(3,1000,1):
    if ((i%3==0) or (i%5==0)):
        # print('i =', i)
        sum = sum + i
        # print('sum = ', sum)
        
endTime = time.time()
print('THe Sum is: ', sum, 'and total Time taken is: {:.6f} seconds'.format(endTime - startTime))
