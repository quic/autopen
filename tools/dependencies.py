'''
	This script checks and/or installs necessary dependencies to run tools
'''


import general_use
import subprocess
import os

repo_bluez = 'https://github.com/khvzak/bluez-tools.git'

#change redirecting file name later, hardcoding for now for testing

def commandline_install(pack_man, i):
	general_use.update(pack_man)
	return subprocess.run(['sudo', pack_man, '-y', 'install', i]).returncode

def download_install(toolname, link):
	return subprocess.run(['curl', '-o', toolname, link]).returncode

def clone_git_repo(repo):
	return subprocess.run(["git", "clone", repo]).returncode

def install_pyserial(link):
	d_rc = download_install('pyserial', link) #FYI MIGHT BE ABLE TO RUN PIP INSTALL PYSERIAL 
	if d_rc != 0:
		print ('DOWNLOAD FAILED: Failed to download pyserial')
		print ('WITH ERROR CODE:', d_rc)
		return d_rc
	else:
		print ('DOWNLOAD SUCCESSFUL: Successfully downloaded pyserial')
		print ('Building PySerial 2.0 package...')
		current_dir = os.getcwd()
		path = current_dir + '/pyserial-2.0'
		os.chdir(path)
		build_rc = subprocess.run(['python', 'setup.py', 'build']).returncode
		if build_rc != 0:
			print ('BUILD FAILED: Failed to build pyserial.')
			print ('WITH ERROR CODE:', build_rc)
			return build_rc
		else:
			print ('BUILD SUCCESSFUL: Successfully completed pyserial build')
			print ('Installing pyserial...')
			i_rc = subprocess.run(['sudo', 'python', 'setup.py', 'install']).returncode
			if i_rc != 0:
				return i_rc
			else:
				return 0

def install_NPM(pack_man):

	print ('Installing npm...')
	npm_rc = commandline_install(pack_man, 'npm')
	if npm_rc != 0:
		print ('INSTALLATION FAILED: Could not install npm. This package is necessary to run canbus-utils')
		print ('WITH ERROR CODE: ', npm_rc)
		return npm_rc
	else:
		print ('INSTALLATION SUCCESSFUL: Successfully installed npm')
		return 0

def check_symlink(source_file, symlink):
	
	check_rc = subprocess.run(['test', '-h', symlink]).returncode
	if check_rc!= 0:
		print ('Creating symbolic link between', source_file, 'and', symlink, '...')
		symlink_rc = subprocess.run(['sudo', 'ln', '-s', source_file, symlink]).returncode #this might not work
		if symlink_rc != 0:
			print ('SYMLINK CREATION FAILED: Failed to create a symbolic link between', source_file, 'and', symlink)
		elif symlink_rc == 0:
			print ('SYMLINK CREATION SUCCESSFUL: Successfully created a symbolic link between', source_file, 'and', symlink)
		return symlink_rc
	else:
		print ('Symbolic link already created between', source_file, 'and', symlink)
		return 0

def check_NPM(pack_man): #cant decide if should do this / count this as basics, like install ruby and gcc and homebrew so that later can just run brew install node? 

	try:
		check_node_existence_rc = subprocess.run(['/usr/bin/nodejs', '--version']).returncode
	except FileNotFoundError:
		check_node_existence_rc = -1
	try:
		check_npm_existence_rc = subprocess.run(['/usr/bin/node', '--version']).returncode
	except FileNotFoundError:
		check_npm_existence_rc = -1

	if check_node_existence_rc == 0:
		if check_npm_existence_rc == 0:
			print ('CONFIRMATION COMPLETE: Both node.js and npm are installed')
			i_rc = 0
		else:
			i_rc = install_NPM(pack_man)
	else:
		print ('Installing nodejs...')
		node_rc = commandline_install(pack_man, 'nodejs')
		if node_rc != 0:
			print ('INSTALLATION FAILED: Could not install nodejs. This package is necessary to run npm which is used for canbus-utils')
			print ('WITH ERROR CODE: ', node_rc)
			i_rc = node_rc
		else:
			print ('INSTALLATION SUCCESSFUL: Successfully installed nodejs')
			print ('Installing npm...')
			i_rc = install_NPM(pack_man)	

	if i_rc != 0:
		return i_rc
	else:
		print ('Checking for symbolic link existence between nodejs (/usr/bin/nodejs) and npm (/usr/bin/node)')
		symlink_rc = check_symlink('/usr/bin/nodejs', '/usr/bin/node')
		if symlink_rc != 0:
			return symlink_rc
		else:
			print ('Confirming complete installation of nodejs and npm...') #dk if will keep this yet, we'll see
			node_check_rc = subprocess.run(['/usr/bin/nodejs', '--version']).returncode
			npm_check_rc = subprocess.run(['/usr/bin/node', '--version']).returncode
			if node_check_rc == 0 and npm_check_rc == 0:
				print ('CONFIRMATION COMPLETE: Successfully confirmed installation of both node.js and npm')
				return 0
			else:
				if node_check_rc != 0:
					print ('CONFIRMATION FAILED: Could not confirm installation of node.js')
					print ('WITH ERROR CODE: ', node_check_rc)
					return node_check_rc
				elif npm_check_rc != 0:
					print ('CONFIRMATION FAILED: Could not confirm installation of npm')
					print ('WITH ERROR CODE: ', npm_check_rc)
					return npm_check_rc

def install_bluez():
	print ('Installing Bluez...')
	print ('Cloning Bluez repository...')
	clone_rc = clone_git_repo(repo_bluez)
	if clone_rc != 0:
		print ('CLONING FAILED: Failed to clone repository at', repo_bluez)
		print ('WITH ERROR CODE: ', clone_rc)
	else:
		print ('CLONING SUCCESSFUL: Successfully cloned repository at', repo_bluez)
		current_dir = os.getcwd()
		path = current_dir + '/bluez-tools-master'
		os.chdir(path)
		config_rc = subprocess.run(['./configure']).returncode
		if config_rc != 0:
			print ('CONFIGURATION FAILED: Failed to run ./configure after cloning Bluez repo')
			print ('WITH ERROR CODE:', config_rc)
			return config_rc
		else:
			print ('CONFIGURATION SUCCESSFUL: Successfully ran ./configure after cloning Bluez repo')
			print ('Compiling...')
			make_rc = subprocess.run(['make']).returncode
			if make_rc != 0:
				print ('COMPILATION FAILED: Failed to compile bluez package')
				print ('WITH ERROR CODE:', make_rc)
				return make_rc
			else:
				print ('COMPILATION SUCCESSFUL: Successfully compiled bluez package')
				print ('Installing Bluez...')
				make_install_rc = subprocess.run(['make', 'install']).returncode
				if make_install_rc != 0:
					print ('INSTALLATION FAILED: Failed to run "make install"')
					print ('WITH ERROR CODE:', make_install_rc)
					return make_install_rc
				else:
					print ('INSTALLATION SUCCESSFUL: Successfully ran make install')
					return 0








