'''

This script is to be executed when running Autopen on a VM 
Running Autopen on a VM is not recommended when using hardware mainly because the hardware needs to be set up. 
Autopen works best with a dedicated install

Make sure to run this script first or Autopen will not install 

'''

import subprocess
import general_use

ff_rc = subprocess.run(['sudo', 'apt-get', 'install', '-y', 'ffmpeg']).returncode
if ff_rc != 0:
	print ('INSTALLATION FAILED: Failed to install ffmpeg library, trying alternative option: libav-tools')
	lib_rc = subprocess.run(['sudo', 'apt-get', 'install', '-y', 'libav-tools']).returncode
	if lib_rc != 0:
		print ('INSTALLATION FAILED: Failed to install alternative to ffmpeg install: libav-tools.')
		print ('Attempting to install using ffmpeg PPA')
		ppa_rc = subprocess.run(['sudo', 'add-apt-repository', 'ppa:mc3man/trusty-media']).returncode
		if ppa_rc != 0:
			print ('GET REPO FAILED: Failed to add-apt-repository of trusty-media where ffmpeg is located')
			print ('WITH ERROR CODE:', ppa_rc)
			print ('INSTALLATION FAILED: Could not install ffmpeg package. Functionality may be hindered and/or Autopen may not be able to run')
		else:
			print ('GET REPO SUCCESSFUL: Successfully added trusty-media repo where ffmpeg is located')
			up_rc = general_use.update(general_use.package_tool(check_distribution()))
			if up_rc != 0:
				print ('UPDATE FAILED: Failed to retrieve packages')
				print ('WITH ERROR CODE:', up_rc)
			else:
				print ('UPDATE SUCCESSFUL: Sucessfully retrived updated packages')
				ffm_rc = subprocess.run(['sudo', 'apt-get', 'install', 'ffmpeg']).returncode
				if ffm_rc != 0:
					print ('INSTALLATION FAILED: Could not install ffmpeg package. Functionality may be hindered and/or Autopen may not be able to run')
					print ('WITH ERROR CODE:', ffm_rc)
				else:
					print ('INSTALLATION SUCCESSFUL: Sucessfully installed ffmpeg package')


libraries_rc = subprocess.run(['sudo', 'apt-get', 'install', '-y', 'python3-pip', 'build-essential', 'git', 'python-dev','libsdl2-dev', 'libsdl2-image-dev', 'libsdl2-mixer-dev',\
	'libsdl2-ttf-dev', 'libportmidi-dev', 'libswscale-dev', 'libavformat-dev', 'libavcodec-dev', 'zlib1g-dev']).returncode
if libraries_rc != 0:
	print ('INSTALLATION FAILED: Failed to install one or more libraries needed to run Autopen in a VM environment')
	print ('Please refer to the log.txt file to check which library/dependency failed')
	print ('WITH ERROR CODE:', libraries_rc)
else:
	ch_rc = subprocess.run(['sudo', 'pip3', 'install', 'virtualenv', 'setuptools']).returncode
	if ch_rc != 0:
		print ('INSTALLATION FAILED: Failed to install virtualenv and/or setuptools')
		print ('CANNOT COMPLETE INSTALLATION. Autopen will most likely not run')
	else:
		#virtualenv is a tool for creating isolated Python environments containing their own copy of python, pip
		x_rc = subprocess.run(['virtualenv', '--no-site-packages', 'kivyinstall']).returncode
		if x_rc != 0:
			print ('VIRTUALENV FAILED: Failed to setup kivy isolated environment')
			print ('WITH ERROR CODE:', x_rc)
		else:
			print ('Changing from dash to bash, hit "no" on the next prompt')
			subprocess.run(['sudo', 'dpkg-reconfigure', 'dash'])
			print ('VIRTUALENV SUCCESSFUL: Successfully setup kivy isolated environment')
			print ('Entering the virtualenv environment...')
			enter_rc = subprocess.run(['source ./kivyinstall/bin/activate'],shell=True).returncode
			if enter_rc != 0:
				print ('VIRTUALENV FAILED: Failed to enter the kivy python environment set-up')
				print ('WITH ERROR CODE:', enter_rc)
			else:
				print ('VIRTUALENV SUCCESSFUL: Successfully entered into kivy python envirnoment')
				print ('Installing cython...')
				cython_rc = subprocess.run(['pip3', 'install', 'Cython==0.23']).returncode
				if cython_rc != 0:
					print ('INSTALLATION FAILED: Failed to install Cython version 0.23')
					print ('WITH ERROR CODE:', cython_rc)
				else:
					print ('INSTALLATION SUCCESSFUL: Successfully installed Cython version 0.23')
					print ('Installing kivy...')
					kivy_rc = subprocess.run(['pip3', 'install', 'kivy']).returncode
					if kivy_rc != 0:
						print ('INSTALLATION FAILED: Failed to install kivy')
						print ('WITH ERROR CODE:', kivy_rc)
					else:
						print ('INSTALLATION SUCCESSFUL: Should now be able to run AutoPen.py')


