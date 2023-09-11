# from pathlib import Path
    # pathlib is a module, Path is a class, (note 'P' in caps)
# now we need to create a path object to reference a file/directory, 2 ways:
# Absolute path ~ we start from the root of our hard disk
    # for eg., c:\Program Files\Microsoft
# Relative path ~ a path starting from the current directory & then go somewhere else

from pathlib import Path

path = Path("ecommerce")
print(path.exists())
path = Path("ecommerce1")
print(path.exists())
path = Path("emails")           #we don't have this directory 'emails'
#but we can create it by calling the make directory method:
#print(path.mkdir())
#returns 'None' coz it doesn't return any value, but a new directory emails is created (check on the left panel)
#print(path.rmdir())            #to remove the directory
#search for files & directories in current path ~
path = Path()
print(path.glob('*.*'))       #* means, all files and all directories
#optionally, you can add an extension *.*, with this, we'll only get the files in the current directory
# Similarly, we can also search all py files (*.py), all excel spreadsheets (*.xls), etc.
# We can iterate or loop through the 'generator object'
for file in path.glob('*.py'):
    print(file)