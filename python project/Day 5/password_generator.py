print('******************Password Generator**********************')
import random
letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

pass_len = int(input('Enter the length of the password: '))
num_len = int(input('Enter the length of the digits: '))
symb_len = int(input('Enter the length of the Special Character: '))
letter_len = pass_len - num_len - symb_len
pass_keys = [letter, digits, punctuation]
pass_lenths = [letter_len, num_len, symb_len]

pswd = ''

for i in range(pass_len):
    key = random.randint(0,2)
    
    while pass_lenths[key] == 0 :
        key = random.randint(0,2)
    
    char_type = pass_keys[key]
    
    if key == 0 and letter_len != 0:
        pswd += char_type[random.randint(0,len(char_type)-1)]
        pass_lenths[key] -= 1
    elif key == 1 and num_len != 0:
        pswd += char_type[random.randint(0,len(char_type)-1)]
        pass_lenths[key] -= 1
    elif key == 2 and symb_len != 0:
        pswd += char_type[random.randint(0,len(char_type)-1)]
        pass_lenths[key] -= 1

print(f"Your password will be : {pswd}")
    

  