import time


fibonacciSequence = [1, 2]
limit = 4_000_000
evensum = 2 

startTime = time.time()


while True:
    nextNumber = fibonacciSequence[-1] + fibonacciSequence[-2]
    if nextNumber > limit:
        break
    fibonacciSequence.append(nextNumber)
    if nextNumber % 2 == 0:
        print('Even Fibonacci Number is:', nextNumber)
        evensum += nextNumber
        print('Even sum is:', evensum)

endTime = time.time()

print('Fibonacci Sequence is:', fibonacciSequence)
print('Sum of even-valued terms:', evensum)
print('Total time taken: {:.6f} seconds'.format(endTime - startTime))
