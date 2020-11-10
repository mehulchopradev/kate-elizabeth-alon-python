'''
Take the number n as user input
And then print all odd numbers till n
'''
n = int(input('Enter n: '))

# odd numbers from 1 to n

# while loop

''' i = 1 # create the loop variable
while i <= n: # loop condition
    if i % 2:
        print(i)
    i = i + 1 # loop variable incrementing/decrementing
'''

# for loop (Preferred way)
'''
I1, I2, I3 -> repeat in a loop

for v in <<sequence of elements>>:
    I1
    I2
    I3
'''
# Go through every number from 1 to n (including)
    # divide the number by 2 and check the remainder
    # if remainder is more than 0
        # print the number
# Sequence of elements -> (1 to n) -> range(1, n+1)
# n = 21 -> (1, 21) -> (1, 2, 3, 4, 5, ......., 21) -> range(1, 22)
# n = 50 -> (1, 50) -> (1, 2, 3, 4, 5, ......, 50) -> range(1, 51)

for v in range(1, n + 1):
    if v % 2:
        print(v)
