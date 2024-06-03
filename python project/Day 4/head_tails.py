print('******************Head Tails************************')
import random
p = 1
while p :
    print('\nPress 1 for playing game.')
    print('Press 0 for exit the game.')
    key = int(input())
    if key == 1:
        win = random.randint(0,1)
        if win == 1:
            print('***************Head**************')
        else:
            print('***************Tails**************')
    elif key == 0:
        p = 0
    else:
        print('Plaese choose an valid number\n')