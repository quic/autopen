'''

	This script has functions that can be used across all scripts

'''
import platform
import subprocess
import os

def check_distribution():
	'''
	This function checks which distribution the user is running and returns that distribution type
	'''

	distro = ''
	distribution = (platform.linux_distribution())[0]

	if 'Kali' == distribution or 'kali' == distribution:
		distro = 'kali'
	elif 'Debian' == distribution or 'debian' == distribution:
		distro = 'debian'
	elif 'Ubuntu' == distribution or 'ubuntu' == distribution:
		distro = 'ubuntu'
	elif 'Red Hat' == distribution or 'red hat' == distribution:
		distro = 'red hat'

	return distro

def package_tool(d):
	'''
	This function returns which package manager the system uses to install scripts based on the distribution
	'''

	pt = ''

	if d == 'kali' or d == 'debian' or d == 'ubuntu':
		pt = 'apt-get'
	elif d == 'red hat':
		pt = 'yum'

	return pt

def update(pack_man):
	'''
		This function updates software packages based on repository state
		This needs to be included at the beginning of every major installation function
	'''	
	update_rc = subprocess.run(['sudo', pack_man, 'update']).returncode
	if update_rc != 0:
		print ('UPDATE_ FAILED: Failed to update_ system')
		print ('ERROR CODE:', update_rc)
	else:
		print ('UPDATE_ SUCCESSFUL: Successfully updated system')

def move_up_directory():
	'''
	This function moves up one directory from where the program is currently running. 
	To successfully install/open tools, different files need to be used that could be in other directories.
	This is used to make sure that at the end of the process for that tool, the program ends in the main autopen directory. 
	'''

	c = os.getcwd()
	s = c.rfind('/')
	os.chdir(c[:s])