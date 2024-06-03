print('******************Encrption and Decription**********************')
status = True
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while(status):
    choice = input("Do you want to Encrypt or Decrypt: ")
    shift = int(input("Enter How much you have to Shift: "))
    if choice == 'encrypt':
        encrypt = ''
        text = input("Enter the text you want to encrypt: ")
        for letter in text:
            if letter == ' ':
                encrypt += ' '
            else:
                index = alphabets.index(letter)
                new_index = index + shift
                if new_index > len(alphabets):
                    new_index = new_index - len(alphabets)
                encrypt += alphabets[new_index]
        print(f'After Encription of \'{text}\' is \'{encrypt}\'')
    elif choice == 'decrypt':
        decrypt = ''
        text = input("Enter the text you want to decrypt: ")
        for letter in text:
            if letter == ' ':
                decrypt += ' '
            else:
                index = alphabets.index(letter)
                new_index = index - shift
                if new_index < 0:
                    new_index = new_index + len(alphabets)
                decrypt += alphabets[new_index]
        print(f'After Decription of \'{text}\' is \'{decrypt}\'')
    restart = input('Do you want to encrypt or decrypt again if yes then enter yes otherwise no: ')
    if restart == 'no':
        status = False