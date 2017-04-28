'''

This script begins by first checking the distribution that the user has and will install the following commands/libraries:

git
python3

Assumes user is running as root and has apt-get installed

'''

import general_use
import dependencies
import subprocess

distro = general_use.check_distribution()
pack_man = general_use.package_tool(distro)

def install_python(pack_man):
	'''
	This function installs or updates Python 3 depending on whether it is already on the system or not
	'''

	print ('Installing/Updating Python 3...')

	p_rc = dependencies.commandline_install(pack_man, "python3")
	if p_rc != 0:
		print ('INSTALLATION FAILED: Could not install Python 3')
		print ("ERROR CODE:", p_rc)
	else:
		print ('INSTALLATION SUCCESSFUL: Python 3 successfully installed')

def update_git(pack_man):
	'''
		This function installs or updates git depending on whether it is already on the system or not
	'''

	print('Installing git...')
	g_rc = dependencies.commandline_install(pack_man, "git")

	if g_rc != 0:
		print ("INSTALLATION FAILED: Could not install git. This is needed to install some of the tools")
		print ("ERROR CODE:", g_rc)
	else:
		print ("INSTALLATION SUCCESSFUL: Git successfully installed")

def install_curl(pack_man):
	'''
		This function installs curl depending
	'''

	print ('Installing curl...')
	c_rc = dependencies.commandline_install(pack_man, 'curl')
	if c_rc != 0:
		print ('INSTALLATION FAILED: Could not install curl. This is needed to install some of the tools')
		print ('ERROR CODE:', c_rc)
	else:
		print ('INSTALLATION SUCCESSFUL: curl successfully installed')

def install_pip(pack_man):

	pip_rc = dependencies.commandline_install(pack_man, 'python3-pip') #might move this to dependency we'll see.
	if pip_rc != 0:
		print ('INSTALLATION FAILED: Failed to install pip. This is needed to install some dependencies for tools')
		print ('ERROR CODE:', pip_rc)
	else:
		print ('INSTALLATION COMPLETE: Successfully installed pip')		#pip upgrade isn't working for some reason
	#	upgrade_rc = subprocess.run(['pip3', 'install', '--upgrade', 'pip3']).returncode
	#	if upgrade_rc != 0:
	#		print ('UPGRADE FAILED: Failed to upgrade pip. This may cause trouble when installing libraries')
	#		print ('ERROR CODE:', upgrade_rc)
	#	else:
	#		print ('UPGRADE SUCCESSFUL: Successfully upgraded pip to newest version')

install_python(pack_man)
update_git(pack_man)
install_curl(pack_man)
install_pip(pack_man)

