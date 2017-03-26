import general_use
import install_basics
import dependencies
import tools
import subprocess
'''
TO DO:

1. need to redirect all output to a log file 
	possibly standard out with everything
	standard error with just errors
2. want to keep track of what's been installed and what hasn't to change buttons accordingly
	when installation is done > change button to say open
	also make a quick list to see what's installed and what hasn't been
3. create a open.py for after things are installed and user wants to open the program

'''

#this will be placed somewhere else, maybe a dictionary?
repo_can_utils = 'https://github.com/linux-can/can-utils.git' #needed to run can-utils
repo_canbus_utils = 'https://github.com/digitalbond/canbus-utils.git'
repo_kayak = 'https://github.com/dschanoeh/Kayak.git'
repo_caringcaribou = 'https://github.com/CaringCaribou/caringcaribou.git' #want to check this to make sure it works, instructions a bit unclear
repo_c0f = 'https://github.com/zombieCraig/c0f.git'
repo_udsim = 'https://github.com/zombieCraig/UDSim.git'
repo_katoolin = 'https://github.com/LionSec/katoolin.git'

#BLUETOOTH
repo_bluelog = 'https://github.com/MS3FGX/Bluelog.git'

#for download links
link_pyobd = 'http://www.obdtester.com/download/pyobd_0.9.3.tar.gz'
link_o2oo = 'https://www.vanheusden.com/O2OO/O2OO-0.9.tgz'
link_romraider = 'http://assembla.com/spaces/romraider/documents/a5Ao9gHEir5P9Udmr6QqzO/download/RomRaider0.5.9RC3-linux.jar'

d = general_use.check_distribution()
pack_man = general_use.package_tool(d)
#tools.github_tools(pack_man, 'can-utils', repo_can_utils) 			#DONE
tools.github_tools(pack_man, 'canbus-utils', repo_canbus_utils)
#tools.github_tools(pack_man, 'kayak', repo_kayak)
#tools.github_tools(pack_man, 'caringcaribou', repo_caringcaribou)
#tools.github_tools(pack_man, 'c0f', repo_c0f)
#tools.github_tools(pack_man, 'udsim', repo_udsim)
#tools.github_tools(pack_man, 'katoolin', repo_katoolin)

#tools.downloaded_tools(pack_man, 'pyobd', link_pyobd) #WxPython and some other library
#tools.downloaded_tools(pack_man, 'o2oo', link_o2oo) #WxPython and some other library
#tools.downloaded_tools(pack_man, 'romraider', link_romraider) #WxPython and some other library

#tools.installed_tools(pack_man, 'bluetooth tools') #this function is for tools that are apt-getable / yumable
#tools.installed_tools(pack_man, 'btscanner')
#tools.installed_tools(pack_man, 'gnuradio')


'''

Things to note during testing: 

1. in order to run test_install.py , python3 has to be installed. So, we need to make it that they can just run the python version of make
2. if they clone from git, they have to have git installed. If they download zip, they do not (we will install for them). Need to include instructions for both 

EXCEPTIONS TO CATCH:
	1. if the repo has already been cloned, want to keep going
	2. in dependencies in check_NPM (wrap command -v in exception catching FileNotFoundError), this is because if it's not there it throws this error


ERRORS:
	1. Having trouble redirecting output to text file; it's reading it as added arguments


'''