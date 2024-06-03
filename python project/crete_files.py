import os 

for a in range(2,101):
    parent_dir = 'C:/Users\kumar/Suraj/My Projects/python/python project/'
    folder = f'Day {a}'
    path = os.path.join(parent_dir, folder) 
    os.mkdir(path)