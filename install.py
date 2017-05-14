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
		return tools.github_tools(pack_man, 'canbus-utils', repo_canbus_utils)
	elif toolname == 'kayak':
		return tools.github_tools(pack_man, 'Kayak', repo_kayak)
	elif toolname == 'caringcaribou':
		return tools.github_tools(pack_man, 'caringcaribou', repo_caringcaribou)	#CANT TEST THIS UNLESS A DEVICE IS ATTACHED AND SET UP
	elif toolname == 'c0f':
		return tools.github_tools(pack_man, 'c0f', repo_c0f)
	elif toolname == 'udsim':
		return tools.github_tools(pack_man, 'udsim', repo_udsim)
	elif toolname == 'katoolin':
		return tools.github_tools(pack_man, 'katoolin', repo_katoolin)
	elif toolname == 'bluelog':
		return tools.github_tools(pack_man, 'Bluelog', repo_bluelog)
	elif toolname == 'bluemaho':
		return tools.github_tools(pack_man, 'bluemaho', repo_bluemaho)
	elif toolname == 'j1939':
		return tools.github_tools(pack_man, 'j1939', repo_j1939)
	elif toolname == 'canbadger-hw':
		return tools.github_tools(pack_man, 'canbadger-hw', repo_canbadger)
	elif toolname == 'canbadger-sw':
		return tools.github_tools(pack_man, 'canbadger-sw', repo_canbadger_server)
	elif toolname == 'can-utils-x':
		return dependencies.can_utils_x(pack_man)

	elif toolname == 'pyobd':
		return tools.downloaded_tools(pack_man, 'pyobd', link_pyobd)
	elif toolname == 'o2oo':
		return tools.downloaded_tools(pack_man, 'o2oo', link_o2oo)

	elif toolname == 'btscanner':
		return tools.installed_tools(pack_man, 'btscanner')
	elif toolname == 'gnuradio':
		return tools.installed_tools(pack_man, 'gnuradio')
	elif toolname == 'aircrack-ng':
		return tools.installed_tools(pack_man, 'aircrack-ng')
	elif toolname == 'gqrx':
		return tools.installed_tools(pack_man, 'gqrx')
	elif toolname == 'can-utils':
		return tools.installed_tools(pack_man, 'can-utils')
	elif toolname == 'wireshark':
		return tools.installed_tools(pack_man, 'wireshark')
	elif toolname == 'tshark':
		return tools.installed_tools(pack_man, 'tshark')

def test(name):
	it = open('installed.txt', 'a')
	it.write(name)
	it.write('\n')
	return 0



