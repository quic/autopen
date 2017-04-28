import general_use
import dependencies
import tools
import os
import subprocess


#OPEN TOOLS IN THE BACKGROUND

def open_(toolname, option):
	'''
	This function opens the specified tool
	'''

	#tools not with 'open' button : can-utils, canbus-utils, c0f, 'UDSim', bluez (provide a list with the commands it allows), aircrack-ng
	op_rc = -1

	t = ['Kayak', 'caringcaribou', 'Bluelog', 'bluemaho', 'canbus-utils']
	if toolname in t:
		current = os.getcwd()
		path = current + '/' + toolname
		os.chdir(path)

	if toolname == 'Kayak':
		kayak_run_path = '/application/target/kayak/bin'
		print ('Changing directory to', kayak_run_path, '...')
		current_dir = os.getcwd()
		path = current_dir + kayak_run_path
		os.chdir(path)
		op_rc = subprocess.run(['./kayak']).returncode
	elif toolname == 'can-utils':
		op_rc = subprocess.run(['/bin/bash']).returncode
	elif toolname == 'canbus-utils':
		op_rc = subprocess.run(['/bin/bash']).returncode
	elif toolname == 'caringcaribou':
		current_dir = os.getcwd()
		path = current_dir + '/tool'
		os.chdir(path)
		o = '/modules/' + option
		op_rc = subprocess.run(['./cc.py', o]).returncode #option here will be the module
	elif toolname == 'katoolin':
		op_rc = subprocess.run(['katoolin']).returncode
	elif toolname == 'bluelog':
		op_rc = subprocess.run(['./bluelog']).returncode	#works if you have a bluetooth device up
	elif toolname == 'bluemaho':
		op_rc = subprocess.run(['./bluemaho.py']).returncode
	elif toolname == 'pyobd':
		current = os.getcwd()
		path = current + '/pyobd-0.9.3'
		os.chdir(path)
		op_rc = subprocess.run(['./pyobd']).returncode
	elif toolname == 'O2OO':	#isn't going to work unless 
		o = './' + option	#make sure that when this is called it passes O2OO- before the name and not the button name
		current = os.getcwd()
		path = current + '/O2OO-0.9'
		os.chdir(path)
		op_rc = subprocess.run([o]).returncode
	elif toolname == 'btscanner':
		#mention that this command will just show a list of the devices that are available; else can run btscanner (path to file name) and then potentially have a reset button
		op_rc = subprocess.run(['btscanner']).returncode
	elif toolname == 'gnuradio':
		op_rc = subprocess.run(['gnuradio-companion']).returncode
	elif toolname == 'can-utils-x':	#i think i have to change this to cd into the directory but will have to change this to cd into directory ? 
		op_rc = subprocess.run(['python', 'main.py']).returncode
	elif toolname == 'gqrx':
		op_rc = subprocess.run(['gqrx']).returncode
	elif toolname == 'wireshark':
		op_rc = subprocess.run(['wireshark']).returncode

	if op_rc != 0:
		print ('STARTUP FAILED: Failed to open', toolname)
		print ('ERROR CODE:', op_rc)
	else:
		print ('STARTUP SUCCESSFUL: Successfully opened', toolname)

def test(tool):
	return 0

