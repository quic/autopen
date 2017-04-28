import general_use
import install_basics
import dependencies
import tools
import subprocess

def test():
	#this might be placed somewhere else
	repo_can_utils = 'https://github.com/linux-can/can-utils.git'
	repo_canbus_utils = 'https://github.com/digitalbond/canbus-utils.git'
	repo_kayak = 'https://github.com/dschanoeh/Kayak.git'
	repo_caringcaribou = 'https://github.com/CaringCaribou/caringcaribou.git' #want to check this to make sure it works, instructions a bit unclear
	repo_c0f = 'https://github.com/zombieCraig/c0f.git'
	repo_udsim = 'https://github.com/zombieCraig/UDSim.git'
	repo_katoolin = 'https://github.com/LionSec/katoolin.git'

	#BLUETOOTH
	repo_bluelog = 'https://github.com/MS3FGX/Bluelog.git'
	repo_bluemaho = 'https://github.com/zenware/bluemaho.git'

	#for download links
	link_pyobd = 'http://www.obdtester.com/download/pyobd_0.9.3.tar.gz'	#this might not work
	link_o2oo = 'https://www.vanheusden.com/O2OO/O2OO-0.9.tgz'
	link_romraider = 'http://assembla.com/spaces/romraider/documents/a5Ao9gHEir5P9Udmr6QqzO/download/RomRaider0.5.9RC3-linux.jar'

	d = general_use.check_distribution()
	pack_man = general_use.package_tool(d)
	tools.github_tools(pack_man, 'can-utils', repo_can_utils) 			#DONE
	tools.github_tools(pack_man, 'canbus-utils', repo_canbus_utils)		#DONE
	tools.github_tools(pack_man, 'Kayak', repo_kayak)					#DONE
	tools.github_tools(pack_man, 'caringcaribou', repo_caringcaribou)	#CANT TEST THIS UNLESS A DEVICE IS ATTACHED AND SET UP
	tools.github_tools(pack_man, 'c0f', repo_c0f)				#DONE
	tools.github_tools(pack_man, 'udsim', repo_udsim)	#DONE
	tools.github_tools(pack_man, 'katoolin', repo_katoolin)	#DONE
	tools.github_tools(pack_man, 'Bluelog', repo_bluelog)	#DONE
	tools.github_tools(pack_man, 'bluemaho', repo_bluemaho)	#NOT SURE

	tools.downloaded_tools(pack_man, 'pyobd', link_pyobd) #WxPython and some other library	#DONE BUT NOT SURE IF WORKS
	tools.downloaded_tools(pack_man, 'o2oo', link_o2oo) #DONE

	tools.installed_tools(pack_man, 'bluez') #this function is for tools that are apt-getable / yumable 	DONE
	tools.installed_tools(pack_man, 'btscanner') #DONE
	tools.installed_tools(pack_man, 'gnuradio')
	tools.installed_tools(pack_man, 'aircrack-ng')

	dependencies.for_canuntilsx(pack_man)

#test()



'''



	EXCEPTIONS TO CATCH:
		1. if the repo has already been cloned, want to keep going
		2. in dependencies in check_NPM (wrap command -v in exception catching FileNotFoundError), this is because if it's not there it throws this error
		3. 
		


	ERRORS:
		1. Having trouble redirecting output to text file; it's reading it as added arguments


	'''