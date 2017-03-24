import subprocess
import os
'''
canbus = subprocess.run(['cd', 'test', ';', 'python3', 's.py'])
if canbus.returncode != 0:
	print ('CLONING FAILED: Failed to clone canbus-utils repository at', link_canbus_utils)
	print ('WITH ERROR CODE:', canbus.returncode)
elif canbus.returncode == 0:
	print ('CLONING SUCCESSFUL: Successfully cloned canbus-utils repository')
	print (os.getcwd())
	n = subprocess.run(['python3', 's.py'])
'''

#current = os.getcwd()
#n = current + '/test'
#os.chdir(n)
'''
then = ''
try: 
	then = subprocess.run(['test', '-h', 'test.py'])
	if then.returncode != 0:
		print ('not symlink')
	else:
		print ('symlink')
except:
	print ('Not existing')
'''

r = subprocess.run(['ls', '-l']).returncode
print (r)

'''

repo_socketCAN = 'https://github.com/linux-can/folder' #needed to run can-utils
index = repo_socketCAN.rfind('/')
folder_name = repo_socketCAN[index:]
current_dir = os.getcwd()
path = current_dir + folder_name
os.chdir(path)
run = subprocess.run(['python3', 's.py'])
print (os.getcwd())

'''