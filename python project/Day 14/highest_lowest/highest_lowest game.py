import random
import celebrity_list
status = True
count = 0
while status:
    f_celeb = random.choice(celebrity_list.celebrities)
    s_celeb = random.choice(celebrity_list.celebrities)
    while f_celeb == s_celeb:
        s_celeb = random.choice(celebrity_list.celebrities)

    if f_celeb['followers'] > s_celeb['followers']:
        highest_follower = 'f'
    else:
        highest_follower = 's'
    print(f"{f_celeb['name']}, {f_celeb['description']} stays at {f_celeb['country']}.")
    print('VS')
    print(f"{s_celeb['name']}, {s_celeb['description']} stays at {s_celeb['country']}.")
    select = input('Select who has more followers. Type F for first Celebrity and S for second.')
    if select.lower() == highest_follower:
        count += 1
        print(f"Correct! {f_celeb['name']}, has {f_celeb['followers']} and {s_celeb['name']}, has {s_celeb['followers']}.")
        print(f"Your score is {count}.\n")
    else:
        print(f"Sorry you loose! {f_celeb['name']}, has {f_celeb['followers']} and {s_celeb['name']}, has {s_celeb['followers']}.")
        status = False
    
