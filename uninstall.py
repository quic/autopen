import general_use
import dependencies
import tools
import subprocess

def uninstall(toolname):
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

	link_pyobd = 'http://www.obdtester.com/download/pyobd_0.9.3.tar.gz'	#this might not work
	link_o2oo = 'https://www.vanheusden.com/O2OO/O2OO-0.9.tgz'
	link_romraider = 'http://assembla.com/spaces/romraider/documents/a5Ao9gHEir5P9Udmr6QqzO/download/RomRaider0.5.9RC3-linux.jar'

	d = general_use.check_distribution()
	pack_man = general_use.package_tool(d)

	#check path to make sure it's in the autopen directory
	curr = os.getcwd()
	back_index = curr.rfind('/')
	ap_index = curr.find('autopen')
	if curr[back_index:] != '/autopen':
		path = curr[:ap_index+7]
	else:
		path = curr

	os.chdir(path)

	#wrap in exception so that if path isn't correct it doesn't crash program
	#catch will be a print statement that prints out the directory that the user is in and tells them to go to that directory

	if toolname == 'canbus-utils':
		rm_rc = subprocess.run(['rm', '-rf', 'canbus-utils']).returncode
	elif toolname == 'kayak':
		rm_rc = subprocess.run(['rm', '-rf', 'Kayak']).returncode
	elif toolname == 'caringcaribou':
		rm_rc = subprocess.run(['rm', '-rf', 'caringcaribou']).returncode
	elif toolname == 'c0f':
		rm_rc = subprocess.run(['rm', '-rf', 'c0f']).returncode
	elif toolname == 'udsim':
		rm_rc = subprocess.run(['rm', '-rf', 'UDSim']).returncode
	elif toolname == 'katoolin':
		rm_rc = subprocess.run(['rm', '-rf', 'katoolin']).returncode
	elif toolname == 'bluelog':
		rm_rc = subprocess.run(['rm', '-rf', 'Bluelog']).returncode
	elif toolname == 'bluemaho':
		rm_rc = subprocess.run(['rm', '-rf', 'bluemaho']).returncode
	elif toolname == 'j1939':
		rm_rc = subprocess.run(['rm', '-rf', 'can-utils-j1939']).returncode
	elif toolname == 'canbadger-hw':
		rm_rc = subprocess.run(['rm', '-rf', 'CANBadger']).returncode
		#https://github.com/Gutenshit/CANBadger/wiki/Getting-the-board-ready
	elif toolname == 'canbadger-sw':
		rm_rc = subprocess.run(['rm', '-rf', 'CANBadger-Server']).returncode

	elif toolname == 'pyobd':
		try:
			rm_rc = subprocess.run(['rm', '-rf','pyobd_0.9.3.tar.gz']).returncode
		except:
			pass
		try:
			rm_rc = subprocess.run('rm', '-rf', 'pyobd-0.9.3').returncode
		except:
			pass
	elif toolname == 'o2oo':
		try:
			rm_rc = subprocess.run(['rm', '-rf','O2OO-0.9.tgz']).returncode
		except:
			pass
		try:
			rm_rc = subprocess.run('rm', '-rf', 'O2OO-0.9').returncode
		except:
			pass

	elif toolname == 'bluez':
		rm_rc = subprocess.run(['sudo', pack_man, 'purge', 'bluez']).returncode
	elif toolname == 'btscanner':
		rm_rc = subprocess.run(['sudo', pack_man, 'purge', 'btscanner']).returncode
	elif toolname == 'gnuradio':
		rm_rc = subprocess.run(['sudo', pack_man, 'purge', 'gnuradio']).returncode
	elif toolname == 'aircrack-ng':
		rm_rc = subprocess.run(['sudo', pack_man, 'purge', 'aircrack-ng']).returncode
	elif toolname == 'gqrx':
		rm_rc = subprocess.run(['sudo', pack_man, 'purge', 'gqrx']).returncode
	elif toolname == 'can-utils':
		rm_rc = subprocess.run(['sudo', pack_man, 'purge', 'can-utils']).returncode
	elif toolname == 'wireshark':
		rm_rc = subprocess.run(['sudo', pack_man, 'purge', 'wireshark']).returncode
	elif toolname == 'tshark':
		rm_rc = subprocess.run(['sudo', pack_man, 'purge', 'tshark']).returncode

def test(name):
	return 0

