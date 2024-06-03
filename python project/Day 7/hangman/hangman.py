import wordlist
import random
print('******************hangman**********************')
word = random.choice(wordlist.word_list)
og_word = word
guess = '_' * len(word)
fault = 0
win = len(word)
can_play = 1

hang_man = [[' ',' ','+','-','-','-','+',' ',' '],
            [' ',' ',' ',' ',' ',' ','|',' ',' '],
            [' ',' ',' ',' ',' ',' ','|',' ',' '],
            [' ',' ',' ',' ',' ',' ','|',' ',' '],
            [' ',' ',' ',' ',' ',' ','|',' ',' '],
            ['=','=','=','=','=','=','=','=','=']]

man_loc = [[1,2,'|'], [2,2,'O'], [3,1,'/'], [3,2,'|'], [3,3,'\\'], [4,1,'/'], [4,3,'\\']]
def char_finder(word, char):
    for i in range(len(word)):
        if word[i] == char:
            word = word[:i] + '_' + word[i+1:] 
            return word , i
        
    return word , -1
            
def print_hangman(hangman):
    print()
    for i  in hang_man:
        for j in i:
            print(j,end='')
        print()
    print()
while can_play:
    
    print(guess)
    char = str(input(f'Choose a letter you have {7-fault} chance: '))
    word , index = char_finder(word,char)
    if index >= 0:
        guess = guess[:index] + char + guess[index+1:]
        win -= 1
        print('')
    else:
        fault += 1
        
    if fault > 0:
        loc = man_loc[fault-1]
        hang_man[loc[0]][loc[1]] = loc[2]
    
    print_hangman(hang_man)        
         
    if win == 0:
        print("You Win")
        can_play = 0
    elif fault >= 7:
        print(f"Your word is {og_word}.")
        print("You Lose")
        can_play = 0
        