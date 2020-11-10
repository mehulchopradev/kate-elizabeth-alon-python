'''
1. Fibo Series
2. Odd Series
3. Even or Odd
4. Exit
Please enter ur choice: 1
Enter n: 8
0
1
1
2
3
5
8
13
1. Fibo Series
2. Odd Series
3. Even or Odd
4. Exit
Please enter ur choice: 2
Enter n: 10
1
3
5
7
9
1. Fibo Series
2. Odd Series
3. Even or Odd
4. Exit
Please enter ur choice: 3
Enter n: 13
It is odd
1. Fibo Series
2. Odd Series
3. Even or Odd
4. Exit
Please enter ur choice: 4
'''

# Module name -> menu_driven

# import a module
# import series
import com.abc.lib.series as series

# import the functions directly from the module

# module namespace conflict
''' from math import even_odd
from math import factorial '''

from com.abc.lib.math import even_odd
from math import factorial as fact

while True:
    print('1. Fibo Series')
    print('2. Odd Series')
    print('3. Even or Odd')
    print('4. Factorial')
    print('5. Exit')

    choice = int(input('Please enter ur choice: '))
    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        n = int(input('Enter n: '))

    if choice == 1:
        # fibo series till n
        # print(com.abc.lib.series.fibo_series(n=n))
        print(series.fibo_series(n=n))
    elif choice == 2:
        # odd series till n
        # print(com.abc.lib.series.odd_series(n=n))
        print(series.odd_series(n=n))
    elif choice == 3:
        # even or odd -> n
        print(even_odd(n=n))
    elif choice == 4:
        # factorial of number n
        # print(factorial(n))
        print(fact(n))
    else:
        break # breaks out forcibly from the closest loop