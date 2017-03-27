'''

This script begins by first checking the distribution that the user has and will install the following commands/libraries:

git
python3

Assumes user is running as root and has apt-get installed

'''

#send STDERR to STDOUT: http://stackoverflow.com/questions/29580663/save-error-message-of-subprocess-command
#right now it logs everything, once completed add functionality for errors to print in RED and for multiple logs to be made, complete, STDERR, etc.
#current issue a lot of these asks do you want to continue, obvi need to say yes. How does one automate that? 

import general_use
import dependencies

distro = general_use.check_distribution()
pack_man = general_use.package_tool(distro)


def install_python(pack_man):
	'''
	This function installs or updates Python 3 depending on whether it is already on the system or not
	'''

	print ('Installing Python 3...')


	p_rc = dependencies.commandline_install(pack_man, "python3")
	if p_rc != 0:
		print ('INSTALLATION FAILED: Could not install Python 3')
		print ("WITH ERROR CODE:", p_rc)
	else:
		print ('INSTALLATION SUCCESSFUL: Python 3 successfully installed')

def install_git(pack_man):
	'''
		This function installs or updates git depending on whether it is already on the system or not
	'''

	print('Installing git...')
	g_rc = dependencies.commandline_install(pack_man, "git")

	if g_rc != 0:
		print ("INSTALLATION FAILED: Could not install git. This is needed to install some of the tools")
		print ("WITH ERROR CODE:", g_rc)
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
		print ('WITH ERROR CODE:', c_rc)
	else:
		print ('INSTALLATION SUCCESSFUL: curl successfully installed')

def install_pip(pack_man):
	
	pip_rc = commandline_install(pack_man, 'python-pip') #might move this to dependency we'll see.
	if pip_rc != 0:
		print ('INSTALLATION FAILED: Failed to install pip. This is needed to install some dependencies for tools')
		print ('WITH ERROR CODE: ', pip_rc)
	else:
		print ('INSTALLATION COMPLETE: Successfully installed pip')

install_python(pack_man)
install_git(pack_man)
install_curl(pack_man)
install_pip(pack_man)

