import random
print('I am selecting number from 1 to 100')
num = random.randint(1,100)
level_type = input('Please Select the level Easy or Hard ? Type E for easy and H for hard: ')
chance = 5 if level_type.lower() == 'h' else 10
while chance != 0:
    guess = int(input(f'\nGusse any number between 1 to 100 You have {chance} chance: '))
    if num > guess:
        if num < guess + 5:
            print('closest low')
        elif num < guess + 10:
            print('less far low')
        else:   
            print('Too Low')
    elif num < guess:
        if num > guess - 5:
            print('closest High')
        elif num > guess - 10:
            print('less far High')
        else:   
            print('Too High')
    else:
        print('Congratulations! You have guessed the number')
        break
    chance -= 1
    if chance == 0 :
        print(f'You loosed the game! Number was {num}')


