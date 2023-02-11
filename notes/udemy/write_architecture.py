import sys
import os

path = sys.path[0]  # current path 

# write README.md
arr_dir = os.listdir(path)
with open(path + '/README.md', 'w') as f:
    f.write('# Architecture \n\n\n')
    f.write('**~\%s :**\\\n' %path[-5:])
    for dir in arr_dir:
        dir_path = './%s' %dir
        f.write(' |- [%s](%s)' %(dir, dir_path))
        if dir != arr_dir[-1]: f.write('\\\n')
    f.write('\n\n> Project folder is confidential.')

# write .gitignore
with open(path + '/.gitignore', 'w') as f:
    f.write('.gitignore\n')
    for dir in arr_dir:
        if '.' not in dir:
            f.write('%s/*\n' %dir)  # hide all inside dir
            f.write('!%s/README.md' %dir)   # except README.md