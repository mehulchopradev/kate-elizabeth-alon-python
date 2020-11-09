'''
>= 70 - A
>= 60 - B
>= 40 - C
< 40 - F
> 100 or < 0 - Invalid
'''

marks = float(input('Enter marks: '))

# branching statements here
# more than 2 branches
# if <> - elif <> - elif <> - elif <> - else

if marks > 100 or marks < 0:
    print('Invalid')
elif marks >= 70:
    print('A')
elif marks >= 60:
    print('B')
elif marks >= 40:
    print('C')
else:
    print('F')
