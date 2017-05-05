import general_use
import dependencies
import subprocess
import os

#this script is written such that it is not meant for the user to update 
#if the user wants to update then we need to find out which one is ahead of the other
#if any changes were made they need to store those commits before pulling from master the most updated


#tell the user he needs to have commited his most recent changes , except they can't 

def update(toolname):

	#github tools
	repo_canbus_utils = 'https://github.com/digitalbond/canbus-utils.git'
	repo_kayak = 'https://github.com/dschanoeh/Kayak.git'
	repo_caringcaribou = 'https://github.com/CaringCaribou/caringcaribou.git' #want to check this to make sure it works, instructions a bit unclear
	repo_c0f = 'https://github.com/zombieCraig/c0f.git'
	repo_udsim = 'https://github.com/zombieCraig/UDSim.git'
	repo_j1939 = 'https://github.com/wang701/can-utils-j1939.git'
	repo_canbadger = 'https://github.com/Gutenshit/CANBadger.git'
	repo_canbadger_server = 'https://github.com/Gutenshit/CANBadger-Server.git'

	repo_katoolin = 'https://github.com/LionSec/katoolin.git'

	repo_bluelog = 'https://github.com/MS3FGX/Bluelog.git'
	repo_bluemaho = 'https://github.com/zenware/bluemaho.git'

	#downloaded tools
	link_pyobd = 'http://www.obdtester.com/download/pyobd_0.9.3.tar.gz'	#this might not work
	link_o2oo = 'https://www.vanheusden.com/O2OO/O2OO-0.9.tgz'
	link_romraider = 'http://assembla.com/spaces/romraider/documents/a5Ao9gHEir5P9Udmr6QqzO/download/RomRaider0.5.9RC3-linux.jar'

	#add exception to check if the tool is installed, in case they accidentally click this. Possibly add a pop-up that says "need to install first"


	#check path to make sure it's in the autopen directory
	curr = os.getcwd()
	back_index = curr.rfind('/')
	ap_index = curr.find('autopen')
	if curr[back_index:] != '/autopen':
		path = curr[:ap_index+7]
	else:
		path = curr
	os.chdir(path)

	github_tools = ['canbus-utils', 'kayak', 'caringcaribou', 'c0f', 'udsim', 'j1939', 'canbadger-hw', 'canbadger-sw', 'katoolin', 'bluelog', 'bluemaho']
	downloaded_tools = ['pyobd', 'o2oo', 'romraider']
	commandline_tools = ['bluez', 'btscanner', 'gnuradio', 'aircrack-ng', 'wireshark', 'can-utils', 'tshark', 'gqrx']

	
	if toolname in github_tools:
		if toolname == 'canbus-utils':
			os.chdir(os.getcwd() + '/canbus-utils')
		elif toolname == 'kayak':
			os.chdir(os.getcwd() + '/Kayak')
		elif toolname == 'caringcaribou':
			os.chdir(os.getcwd() + 'caringcaribou')
		elif toolname == 'c0f':
			os.chdir(os.getcwd() + 'c0f')
		elif toolname == 'udsim':
			os.chdir(os.getcwd() + 'UDSim')
		elif toolname == 'j1939':
			os.chdir(os.getcwd() + 'can-utils-j1939')
		elif toolname == 'canbadger-hw':
			os.chdir(os.getcwd() + 'CANBadger')
		elif toolname == 'canbadger-sw':
			os.chdir(os.getcwd() + 'CANBadger-Server')
		elif toolname == 'katoolin':
			os.chdir(os.getcwd() + 'katoolin')
		elif toolname == 'bluelog':
			os.chdir(os.getcwd() + 'Bluelog')
		elif toolname == 'bluemaho':
			os.chdir(os.getcwd() + 'bluemaho')

		master = subprocess.run(['git', 'rev-parse', 'master'], stdout=subprocess.PIPE).stdout
		origin_master = subprocess.run(['git', 'rev-parse', 'master'], stdout=subprocess.PIPE).stdout

		master_id = master.decode('utf-8')
		origin_master_id = origin_master.decode('utf-8')

		#users repo is behind master
		if master_id != origin_master_id:
			print ('Updating', toolname, '...')
			pull_rc = subprocess.run(['git', 'pull', 'origin', 'master']).returncode
			if pull_rc != 0:
				print ('UPDATE FAILED: Failed to update', toolname)
				print ('ERROR CODE:', pull_rc)
			else:
				print ('UPDATE SUCCESSFUL: Successfully updated', toolname)
				return 0
		else:
			print (toolname, 'is already up to date')
			return 0

	elif toolname in commandline_tools:
		print ('Updating', toolname, '...')
		update_rc = subprocess.run(['sudo', 'apt-get', '--only-upgrade', '-y', 'install', toolname])
		if update_rc != 0:
			print ('UPDATE FAILED: Failed to update', toolname)
			print ('ERROR CODE:', update_rc)
		else:
			print ('UPDATE SUCCESSFUL: Successfully updated', toolname)
			return 0



def test(name):
	return 0














