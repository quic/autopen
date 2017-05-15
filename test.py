import subprocess
import os
import sys

from contextlib import contextmanager

# f = open('log.txt', 'w')

# ps = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
# output = subprocess.run(['tee', '-a', 'log.txt'], stdin=ps.stdout)

y = subprocess.run(['ls', '-l']).returncode

print ('never ever')
print ('test')



# back_index = words.rfind('/')
# name = words.find('autopen')
# if words[back_index:] != '/autopen':
# 	print ('not in correct repo')
# 	print (words[back_index:])
# else:
# 	print (name)
# 	print (words[:(name+7)])
# 	print ('you right')
# print (words)

# f = open('output.txt', 'w')

# # master = subprocess.run(['git', 'rev-parse', 'master'], stdout=subprocess.PIPE)
# # print ((master.stdout).decode('utf-8'))
# # print ('UPDATE FAILED: failed to update tool')

# x = subprocess.run(['sudo', 'apt-get', 'install', 'wireshark']).returncode
# if x != 0:
# 	print 'did not install'
# else:
# 	y = subprocess.run(['sudo', 'apt-get', '--only-upgrade', 'install', 'wireshark']).returncode
# 	if y != 0:
# 		print 'dk whats going on'
# 	else:
# 		print 'hey it worked'