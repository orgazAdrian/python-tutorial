
import os
print(os.getcwd())

# Changing directory

os.chdir('../Users/Desktop/')

# Printing the list of directories
print(os.listdir()) 

# Create a directory (2 options):
# 1. mkdir
# 2. mkdirs -> will reate all the sublevels down you write while mkdir won´t

os.mkdir('Os-demo-2')
os.mkdirs('Os-demo-2/Sub-Dir-1')

# Remove a directory (2 options):
# 1. rmdir
# 2. removedirs -> will delete all the intermediate levels down you write while rmdir won´t

os.rmdir('Os-demo-2/Sub-Dir-1')

# Rename a directory:
#os.rename(existing file name, replacing name)
os.rename('text.txt', 'demo.txt')

# Print out all the information about all the file
print(os.stat('demo.txt'))

# Size of a file
print(os.stat('demo.txt').st_size) #in bytes

# Last modification of a file
print(os.stat('demo.txt').st_mtime) #will print 1458678798

# Convert that datetime into human readable format
from datetime import datetime

mod_time =  os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time)) # will print 2016-04-04 19:21:55

# Print all the directories trees and directories within

# For each yield it iterates, will print three values:
# directory_path, directories_within, files_within_directory_path
os.chadir('path')
for dirpath, dirnames, filenames in os.walk('path'):
	print('Current Path:',dirpath)
	print('Directories:', dirnames)
	print('Files:', filenames)
	print()

# We can get environment variables
os.environ.get('HOME') #Users/User

# Create a new file in our environment directory
# Preventing mispelling errors:

file_path = os.path.join(os.environ.get('HOME'), 'text.txt')
print(file_path)

# Obtain the path of a file
# 1. Check a whether a path exists
print(os.path.exists('/tmp/test.txt'))

# 2. Check whether a path is directory
print(os.path.isdir('/tmp/test.txt')) #bool:True or False

# 3. Split the filename withou the extension
print(os.path.splitext('/tmp/test.txt')) # 'test', '.txt'





