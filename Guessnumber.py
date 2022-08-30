import random
number1 = random.randint(1,10)
n1 = int(number1)
number2 = input('Can you guess the number?')
n2 = int(number2)
while n2 != n1:
    print('Wrong number!')
    number2 = input('Try again')
    n2 = int(number2)
else:
    print('Yep! That is correct! The number is', n1)
