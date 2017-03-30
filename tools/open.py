import general_use
import dependencies
import tools

def open(toolname, option):
	'''
	This function opens the specified tool
	'''

	#tools not with 'open' button : can-utils, canbus-utils, c0f, 'UDSim', bluetooth tools (provide a list with the commands it allows), aircrack-ng

	#change dir here
	if toolname == 'Kayak':
		kayak_run_path = '/Application/target/kayak/bin'
		print ('Changing directory to', kayak_run_path, '...')
		current_dir = os.getcwd()
		path = current_dir + kayak_run_path
		os.chdir(path)
		op_rc = subprocess.run(['./kayak']).returncode
	elif toolname == 'caringcaribou':
		current_dir = os.getcwd()
		path = current_dir + '/tool'
		os.chdir(path)
		op_rc = subprocess.run(['./cc.py']).returncode
	elif toolname == 'katoolin':
		op_rc = subprocess.run(['python', 'katoolin.py']).returncode
	elif toolname == 'Bluelog':
		op_rc = subprocess.run(['./bluelog']).returncode
	elif toolname == 'bluemaho':
		op_rc = subprocess.run(['./bluemaho.py']).returncode
	elif toolname == 'pyobd':
		op_rc = subprocess.run(['./pyobd']).returncode
	elif toolname == 'O2OO':
		o = './' + option	#make sure that when this is called it passes O2OO- before the name and not the button name
		op_rc = subprocess.run([o]).returncode
	elif toolname == 'btscanner':
		#mention that this command will just show a list of the devices that are available; else can run btscanner (path to file name) and then potentially have a reset button
		op_rc = subprocess.run(['btscanner']).returncode
	elif toolname == 'gnuradio':
		op_rc = subprocess.run(['gnuradio-companion']).returncode
	elif toolname == 'can-utils-x':
		op_rc = subprocess.run(['python', 'main.py']).returncode

	if op_rc != 0:
		print ('STARTUP FAILED: Failed to open', toolname)
		print ('ERROR CODE:', op_rc)
	else:
		print ('STARTUP SUCCESSFUL: Successfully opened', toolname)

