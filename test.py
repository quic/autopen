import subprocess
import os

words = os.getcwd()
back_index = words.rfind('/')
name = words.find('autopen')
if words[back_index:] != '/autopen':
	print ('not in correct repo')
	print (words[back_index:])
else:
	print (name)
	print (words[:(name+7)])
	print ('you right')
print (words)