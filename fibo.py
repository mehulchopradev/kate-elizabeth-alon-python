'''
Take integer n as user input
Print n fibonacci numbers

n = 8
0 <- a
1 <- b          <- a
1 <- c (a+b)    <- b         <- a
2               <- c (a+b)   <- b
3                            <- c (a+b)
5
8
13
'''

n = int(input('Enter n: '))

a, b = 0, 1
print(a)
print(b)

nos_left = n - 2

# Sequence of elements from 1 to nos_left -> (1, 2, 3, 4, 5, 6) -> range(1, nos_left + 1)
for v in range(1, nos_left + 1):
    c = a + b
    print(c)
    a, b = b, c