import general_use
#import install_basics
import dependencies
import tools
import subprocess

def install(toolname):
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

	if toolname == 'canbus-utils':
		tools.github_tools(pack_man, 'canbus-utils', repo_canbus_utils)
	elif toolname == 'kayak':
		tools.github_tools(pack_man, 'Kayak', repo_kayak)
	elif toolname == 'caringcaribou':
		tools.github_tools(pack_man, 'caringcaribou', repo_caringcaribou)	#CANT TEST THIS UNLESS A DEVICE IS ATTACHED AND SET UP
	elif toolname == 'c0f':
		tools.github_tools(pack_man, 'c0f', repo_c0f)
	elif toolname == 'udsim':
		tools.github_tools(pack_man, 'udsim', repo_udsim)
	elif toolname == 'katoolin':
		tools.github_tools(pack_man, 'katoolin', repo_katoolin)
	elif toolname == 'bluelog':
		tools.github_tools(pack_man, 'Bluelog', repo_bluelog)
	elif toolname == 'bluemaho':
		tools.github_tools(pack_man, 'bluemaho', repo_bluemaho)
	elif toolname == 'j1939':
		tools.github_tools(pack_man, 'j1939', repo_j1939)
	elif toolname == 'canbadger-hw':
		tools.github_tools(pack_man, 'canbadger-hw', repo_canbadger)
	elif toolname == 'canbadger-sw':
		tools.github_tools(pack_man, 'canbadger-sw', repo_canbadger_server)

	elif toolname == 'pyobd':
		tools.downloaded_tools(pack_man, 'pyobd', link_pyobd)
	elif toolname == 'o2oo':
		tools.downloaded_tools(pack_man, 'o2oo', link_o2oo)

	elif toolname == 'bluez':
		tools.installed_tools(pack_man, 'bluez')
	elif toolname == 'btscanner':
		tools.installed_tools(pack_man, 'btscanner')
	elif toolname == 'gnuradio':
		tools.installed_tools(pack_man, 'gnuradio')
	elif toolname == 'aircrack-ng':
		tools.installed_tools(pack_man, 'aircrack-ng')
	elif toolname == 'gqrx':
		tools.installed_tools(pack_man, 'gqrx')
	elif toolname == 'can-utils':
		tools.installed_tools(pack_man, 'can-utils')
	elif toolname == 'wireshark':
		tools.installed_tools(pack_man, 'wireshark')
	elif toolname == 'tshark':
		tools.installed_tools(pack_man, 'tshark')

def test(name):
	return 0



