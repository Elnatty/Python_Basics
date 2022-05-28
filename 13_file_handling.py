import os
import sys

'''
to join paths, use the os.path.join
p = os.path.join('C:/', 'Users/test')

# listing content in a path
print(os.listdir(p))

# sys info
print(sys.platform)

for i, j in os.environ.items():
    print('Title:', i,'\nContent:', j, '\n')

# current directory
print(os.getcwd())

# list items in cur dir.
print(os.listdir(os.getcwd()))

# changing cur dir into another path
os.chdir('C:/Users/test')
print(os.listdir())

#  --->> renaming a file.
os.renames('C:/Users/test/lang.txt', 'C:/Users/test/test.txt')
print(f'new: {os.listdir()}')


------>> Filing, Opening, Closing, Reading, Writing and Editing
os.chdir('C:/Users/test')

# creating a file in a dir
f = open('newfile.txt', 'w')

# --->>  writing contents to file
f.write('This is the 1st line.\n')
f.write('This is the 2nd line.\n')

# close file
f.close()

#  --->> reading contents
f = open('newfile.txt')
print(f.readline())
print(f.readline())

# --->>  for cursor navigation
f.seek(0)
# to read all content
print(f.read())

#  --->> appending contents to file, use the 'a'
f = open('newfile.txt', 'a')
f.write('This is the 3rd line.\n')
f.close()
f = open('newfile.txt')
print(f.read())
f.close()


# --->>  appending a list to file.
# note, when you use the 'w' it overwrites existing contents in a file, 'a' adds new contents at the bottom of the file
namelist = ['Tim', 'Zoey', 'Anna', 'Philip', 'Nathan', 'Hannah']
mf = open('newlis.txt', 'w')
for name in namelist:
    mf.write(name + '\n')
mf.close()
mf = open('newlis.txt')
print(mf.read())
# or use this to read (more pythonic).
for l in open('newlis.txt').readlines():
    print(l, end='')
    
    
# ---->> deleting a line in a file.    
with open('newlis.txt') as f_old:       # open the old file for read.
    with open('new.txt', 'w') as f_new:     # open newfile for write.
        for line in f_old:                  # iterate through thee old file.
            if line.strip('\n') != 'Zoey':      # remove the exact content.
                f_new.write(line)               # write changes to new file

or use this.....

# create an empty list.
newf = []
# open file as read
with open('new.txt') as f_old:
    # open again as append or write
    with open('new.txt', 'a') as f_edit:
        for old in f_old:
            # stor contents in new empty list, after deleting what you want to delete.
            newf.append(old.replace('Emmanuel is a grudge.', '').lstrip())
# add changes to the main file
with open('new.txt', 'w') as f_new:
    for f in newf:
        f_new.writelines(f)
        
        

# --->> how to walk a directory tree
for root, dirs, files in os.walk(os.curdir):
    print('{0} has {1} files'.format(root, len(files)))
    
# glob is used to return a list of paths matching a path name pattern
import glob
print(glob.glob('C:/Users/test/*.txt'))
'''

os.chdir('C:/Users/test/')
