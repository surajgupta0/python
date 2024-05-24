print('******************Love Calculator************************')
fname = str(input('Enter First name: '))
sname = str(input('Enter Second name: '))
match_name = fname + sname; 
t = r = u = e = l = o = v = e = 0

for i in match_name:
    if i == 't':
        t += 1
    elif  i == 'r':
        r += 1
    elif  i == 'u':
        u += 1
    elif  i == 'e':
        e += 1
    elif  i == 'l':
        l += 1
    elif  i == 'o':
        o += 1
    elif  i == 'v':
        v += 1
        
true_love = str(t + r + u + e) + str(l + o + v + e)

print(f'You love score is {true_love}%')