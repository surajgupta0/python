import random
print('******************Rock Paper Seasor************************')
p = 1

print('Press 1 for Rock')
print('Press 2 for Paper')
print('Press 3 for Seasor')
print('Press 4 for Exit')

while p :
    inp = int(input('\nEnter your Moves: '))
    cases = ['Rock', 'Paper', 'Seasor']
    machine = random.randint(0,2)
    win = 0
    
    # Declaring Result
    if inp == 1:
        if machine == 0:
            win = 2
        elif machine == 1:
            win = 1
        else:
            win = 0
    elif inp == 2:
        if machine == 1:
            win = 2
        elif machine == 2:
            win = 1
        else:
            win = 0
    elif inp == 3:
        if machine == 2:
            win = 2
        elif machine == 1:
            win = 1
        else:
            win = 0
            
    # Added Result Message 
    if win == 0:
        msg = 'You Win'
    elif win == 1:
        msg = 'Machine Win'
    else:
        msg = 'match Draw'
    
    # Showing Result
    match inp:
        case 1:
            print('You have choosen Rock')
            print(f'Machine has choosen {cases[machine]}')
            print(msg)
        case 2:
            print('You have choosen Paper')
            print(f'Machine has choosen {cases[machine]}')
            print(msg)
        case 3:
            print('You have choosen Seasor')
            print(f'Machine has choosen {cases[machine]}')
            print(msg)
        case 4:
            p = 0
        case _:
            print('Invalid Input')    