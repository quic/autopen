'''

#Reference Links for me, might remove later we'll see how life goes 
	can-utils : https://discuss.cantact.io/t/using-can-utils/24 (eric evenchick)
	canbus-utils : http://www.digitalbond.com/blog/2015/03/05/tool-release-digital-bond-canbus-utils/
	NPM: http://blog.teamtreehouse.com/install-node-js-npm-linux
	NPM2: http://www.hostingadvice.com/how-to/install-nodejs-ubuntu-14-04/#node-version-manager (May 2016)
	build-essential can fail, try this just incase: http://unix.stackexchange.com/questions/275438/kali-linux-2-0-cant-install-build-essentials

TO DO: 
	NEED TO CHANGE ALL THE TOOLS TO DOWNLOAD STUFF INTO THEIR FOLDER so that it doesn't just throw everything in one directory (aka cd right after clone/download)
	NEED TO WRITE SCRIPTS TO IMPLEMENT ATTACKS

Front End/Back End Connection:
	We only want the whole thing to run if the install all or install all CAN button is pressed
	Else, we need to function to take in distro and the name of the tool depending on the button pressed and then install that

Note:
	ELM327:
		Be forewarned that the ELM327 has limited buffer space, so you will lose packets when sniffing,
		and transmission can be a bit imprecise, but if you're in a pinch this is the cheapest route.

	Make sure the user knows that this will all be cloned in the current directory aka most likely /Users/'user'


Tools may be included:
	canibus for ELM327:
		(go-server)
	CANtact:
		will provide a section in here with the github link and the website link so that the user can build their own
		Also, will possibly provide steps on how to do so (will learn how to do this first)

Note:
	RomRaider: Subaru
		Warning: RomRaider is intended for use only by experienced tuners who understand the consequences. As with any tuning solution, the potential
		for engine damage is very high when altering your ECUs hard coded values. The use of appropriate equipment (ie, knock sensor, wideband oxygen 
		sensor) is extremely important. By downloading RomRaider, you agree to assume all risks and accept its license. Use at your own risk.

Tools may be included:
	Octane:
		not made available because runs on Windows	
	AVRDUDESS:
		(this one not sure if im going to install yet)
	OpenPilot:
		Hondas and Acuras (believe this one needs specific hardware / it needs to be installed on that but maybe we can make it possible / do for them)


'''

import general_use
import dependencies
import subprocess
import os


link_pyobd_debian = 'http://www.obdtester.com/download/pyobd_0.9.3_all.deb'
link_pyserial = 'https://sourceforge.net/projects/pyserial/files/pyserial/2.0/pyserial-2.0.zip/download'
link_pythoncan = 'https://bitbucket.org/hardbyte/python-can/get/77eea796362b.zip'
link_package = 'https://pkgconfig.freedesktop.org/releases/pkg-config-0.21.tar.gz' #needed for bluelog


def github_tools(pack_man, toolname, repo):
	'''
		This function installs the tools that use github
		rc stands for returncode
	'''
	general_use.update(pack_man)

	print ("Cloning repository...")	#might install 
	git_rc = dependencies.clone_git_repo(repo)
	if git_rc != 0:
		print ('CLONING FAILED: Failed to clone repository at', repo)
		print ('WITH ERROR CODE: ', git_rc)
	else:
		print ('CLONING SUCCESSFUL: Successfully cloned repository at', repo)
		back_index = repo.rfind('/')
		dot_index = repo.rfind('.')
		folder_name = repo[back_index:dot_index]
		print ('Changing directory to', folder_name[1:], '...')
		current_dir = os.getcwd()
		path = current_dir + folder_name
		os.chdir(path)

		if toolname == 'can-utils': #this will install SocketCAN first as it is needed to be able to run can-utils
		#ADD HER CODE INSTALLING SOCKET CAN, WRITE FUNCTION IN DEPENDENCIES
			print ('Beginning can-utils installation...')
			can_utils_rc = dependencies.commandline_install(pack_man, 'can-utils')
			if can_utils_rc != 0:
				print ("INSTALLATION FAILED: Failed to install can-utils")
				print ('WITH ERROR CODE: ', can_utils_rc)
			else:
				print ('INSTALLATION SUCCESSFUL: Successfully installed can-utils')
				print ('Ensuring CAN modules are enabled...')
				modprobe_rc = subprocess.run(['sudo', 'modprobe', 'can']).returncode	#not sure if going to keep this yet mainly cuz might not be necessary, also need to check if redhat has modprobe, it should but need to check (also just check generally if other linux has this already installed)
				if modprobe_rc != 0:
					print ('CHECK FAILED: Failed to add a LKM to the kernel. Can-utils may not be fully functional')
					print ('WITH ERROR CODE: ', modprobe_rc)
				else:
					print ('CHECK SUCCESSFUL: Successfully added a LKM to the kernel')

		elif toolname == 'canbus-utils':	#find out if socketCAN needs to be installed to be able to use it
			print ('Beginning canbus-utils installation...')
			npm_check_rc = dependencies.check_NPM(pack_man) #needed for the following step
			if npm_check_rc != 0:
				print ('INSTALLATION FAILED: Failed to install canbus-utils dependencies. Check node.js and npm status')
				print ('WITH ERROR CODE:', npm_check_rc)
			else:
				print ('INSTALLATION SUCCESSFUL: Successfully installed node.js and npm')
				print ('Installing canbus-utils...')
				npm_rc = subprocess.run(['npm', 'install']).returncode
				if npm_rc != 0:
					print ('INSTALLATION FAILED: Failed to run "npm install". Cannot complete canbus-utils installation')
					print ('WITH ERROR CODE: ', npm_rc)
				else:
					print ('INSTALLATION SUCCESSFUL: Successfully installed canbus-utils')
		elif toolname == 'kayak':
			print ('Beginning kayak installation...')
			check_maven_rc = dependencies.commandline_install(pack_man, 'maven')
			if check_maven_rc != 0:
				print ('INSTALLATION FAILED: Failed to install maven. Cannot complete kayak installation')
				print ('WITH ERROR CODE:', check_maven_rc)
			else:
				print ('Installing jdk...')
				jdk_rc = dependencies.commandline_install(pack_man, 'default-jdk')
				if jdk_rc != 0:
					print ('INSTALLATION FAILED: Failed to install jdk. This compiler is needed to run mvn clean. Cannot complete kayak installation')
				else:
					('Installing kayak...')
					mvn_rc = (subprocess.run(['mvn', 'clean', 'package'])).returncode
					if mvn_rc != 0:
						print ('INSTALLATION FAILED: Failed to run "mvn clean package". Cannot complete kayak installation')
						print ('WITH ERROR CODE: ', mvn_rc)
					else:
						print ('INSTALLATION SUCCESSFUL: Successfully installed kayak')

		elif toolname == 'caringcaribou':
			#---------->have a button that pops up that says that the user will have to set up there device, and have some steps on doing that (front end)
			print ('Beginning caringcaribou installation...')
			print ('Setting up usb-to-can connection...')
			load_rc = subprocess.run(['sudo', 'modprobe', 'can']).returncode #might have to install modprobe?
			if load_rc != 0:
				print ('LOAD FAILED: Failed to load CAN module. Cannot complete caringcaribou installation')
				print ('WITH ERROR CODE: ', load_rc)
			else:
				print ('LOAD SUCCESSFUL: Successfully loaded CAN module')

				#--------->when they click install, have them input the bitrate and the can bus they're on and store these values
				#user needs to input the CAN bus they are on (can we fingerprint how many canbuses are on?)
				#user needs to know the bitrate that the bus runs with
				bitrate = 500000 #HARDCODED FOR NOW
				print ('Setting up CAN device...')
				setup_can_rc = subprocess.run(['sudo', 'ip', 'link', 'set', 'can0', 'up', 'type', 'can', 'bitrate', str(bitrate)]).returncode
				# -----------> handle the error that ip is not a command, 
				if setup_can_rc != 0:
					print ('SETUP FAILED: Failed to set-up can device.')
					print ('WITH ERROR CODE: ', setup_can_rc)
				else:
					print ('SETUP SUCCESSFUL: Successfully set-up can device. This will now display as a normal network interface as can0')
					pcan_rc = dependencies.download_install('can', link_pythoncan)
					if pcan_rc != 0:
						print ('DOWNLOAD FAILED: Failed to download pythoncan from', link_pythoncan, 'Cannot complete caringcaribou installation')
						print ('WITH ERROR CODE: ', pcan_rc)
					else:
						print ('DOWNLOAD SUCCESSFUL: Successfully downloaded pythoncan from', link_pythoncan)
						setup_pcan_rc = subprocess.run(['sudo', 'python', 'setup.py', 'install']).returncode
						if setup_pcan_rc != 0:
							print ('DOWNLOAD SUCCESSFUL: Failed to install python-can. Cannot complete caringcaribou installation')
							print ('WITH ERROR CODE: ', setup_pcan_rc)
						else:
							print ('INSTALLATION SUCCESSFUL: Successfully installed python-can. Caringcaribou installation complete')

							# NEED TO HANDLE THE CONFIGURATION FILE, ARE WE GOING TO TRY TO DO THIS OR IS THE USER GOING TO DO THIS

		elif toolname == 'c0f':
			print ('Beginning c0f installation')
			print ('Installing gem...')
			gem_rc = dependencies.commandline_install(pack_man, 'rubygems')
			if gem_rc != 0:
				print ('INSTALLATION FAILED: Failed to install gem. Cannot complete c0f installation')
				print ('WITH ERROR CODE: ', gem_rc)
			else:
				print ('INSTALLATION SUCCESSFUL: Successfully installed gem')
				headers_rc = dependencies.commandline_install(pack_man, 'ruby-dev')
				if headers_rc != 0:
					print ('INSTALLATION FAILED: Failed to install header files for ruby. Cannot complete c0f installation')
					print ('WITH ERROR CODE:', headers_rc)
				else:
					print ('INSTALLATION SUCCESSFUL: Successfully installed header files for ruby')
					print ('Installing sqlite3 library...')
					sql_rc = dependencies.commandline_install(pack_man, libsqlite3_dev)
					if sql_rc != 0:
						print ('INSTALLATION FAILED: Failed to install sqlite3 library')
						print ('WITH ERROR CODE:'. sql_rc)
					else:
						print ('INSTALLATION SUCCESSFUL: Successfully installed sqlite3')
						print ('Installing c0f...')
						c0f_rc = subprocess.run(['gem', 'install', 'c0f']).returncode
						if c0f_rc != 0:
							print ('INSTALLATION FAILED: Failed to install c0f.')
							print ('WITH ERROR CODE: ', c0f_rc)
						else:
							print ('INSTALLATION SUCCESSFUL: Successfully installed c0f')

		elif toolname == 'udsim': #know later that when user starts the program they have to run make in the file that they are in. Or maybe we can run make
			print ('Beginning udsim installation...')
			final_rc = 0

			#lambda these map to function
			ttf_dev = dependencies.commandline_install(pack_man, 'libsdl2-ttf-dev')
			image = dependencies.commandline_install(pack_man, 'libsdl2-image-2.0.0')
			returncode_list = [ttf_dev, image]
			lib_names = ['ttf-dev', 'image']
			for i, j in enumerate(returncode_list):
				if j != 0:
					final_rc = -1
					print ('INSTALLATION FAILED: Could not install library libsdl2-', lib_names[i])
					print ('WITH ERROR CODE: ', j)
				else:
					print ('INSTALLATION SUCCESSFUL: Successfully installed library libsdl2-', i)
			if final_rc != 0:
				print ('INSTALLATION FAILED: Failed to install libraries needed to compile UDSIM. Cannot complete udsim installation')
			else:
				print ('INSTALLATION COMPLETE: Successfully installed the libraries needed to compile UDSIM.')
	
			#Bluetooth tools below

		elif toolname == 'bluelog': #has an optional web mode so when running want to add that functionality.  (just run make to run)
			print ('INSTALLATION SUCCESSFUL: Successfully installed bluelog')
		elif toolname == 'bluemaho':
			print ('Beginning bluemaho installation...')
			print ('Installing bluemaho dependencies...')
			wxpython = dependencies.commandline_install(pack_man, 'python-wxgtk3.0')
			bluez = dependencies.install_bluez(pack_man)
			config = dependencies.download_install('pkg-config', link_package)
			#lightblue = dependencies.install_lightblue(pack_man) ---> issue installing this one so need to figure this out

			depend = ['libopenobex2-dev', 'libxml2', 'libxml2-dev', 'libusb-dev']
			returncodes = [dependencies.commandline_install(pack_man, i) for i in depend]
			#depend.append('lightblue')
			depend.append('wxpython') #appends the name of the dependencies and returncodes to appropriate lists to have one list of 
			depend.append('bluez')
			depend.append('config')
			#returncodes.append(lightblue)
			returncodes.append(wxpython)
			returncodes.append(bluez)
			returncodes.append(config)

			essential = 0

			for i,j in enumerate(returncodes):
				if j != 0:
					if i < 7:
						#maybe we'll be nice and include which library is associate with what attack 
						print ('INSTALLATION FAILED: Failed to install dependency', depend[i], '. This may remove the ability to run a specific attack using Bluemaho. Please refer to the github repo')
						print ('WITH ERROR CODE:', j)
					else:
						print ('INSTALLATION FAILED: Failed to install dependency', depend[i])
						essential = -1

			if essential != 0:
				print ('INSTALLATION FAILED: Failed to install Bluemaho dependencies: either wxPython, bluez or pkg-config')
			else:
				print ('INSTALLATION SUCCESSFUL: Successfully installed all dependencies for Bluemaho')
				print ('Building Bluemaho...')
				c_dir = os.getcwd()
				last_slash = c_dir.rfind('/')
				path = current_dir[:last_slash] + '/config'
				os.chdir(path)
				build_rc = subprocess.run(['./build.sh']).returncode
				if build_rc != 0:
					print ('BUILD FAILED: Failed to build and complete installation of Bluemaho')
					print ('WITH ERROR CODE:', build_rc)
				else:
					print ('BUILD SUCCESSFUL: Successfully completed Bluemaho build')
		elif toolname == 'katoolin':
			cp_rc = subprocess.run(['sudo', 'cp', 'katoolin.py', '/usr/bin/katoolin']).returncode
			if cp_rc != 0:
				print ('COPY FAILED: Could not copy katoolin.py to /usr/bin/katoolin')
				print ('ERROR CODE:', cp_rc)
			else:
				print ('COPY SUCCESSFUL: Successfully copied katoolin.py to /usr/bin/katoolin')
				print ("Setting /usr/bin/katoolin to executable...")
				mode_rc = subprocess.run(["chmod", "754", "/usr/bin/katoolin"]).returncode #executable script for both you and your group but not for the world. 
				if mode_rc != 0:
					print ("CONVERSION FAILED: Could not make /usr/bin/katoolin executable")
					print ("ERROR CODE:", mode_rc)
				else:
					print ("CONVERSION SUCCESSFUL: /usr/bin/katoolin set to executable")
					print ('INSTALLATION SUCCESSFUL: Successfully installed katoolin')

		elif toolname == 'do':
			mat_rc = dependencies.commandline_install(pack_man, 'python-matplotlib')
			if mat_rc != 0:
				print ('INSTALLATION FAILED: Failed to install matplotlib from python. This is needed to run do')
				print ('ERROR CODE:'. mat_rc)
			else:
				print ('INSTALLATION SUCCESSFUL: Successfully installed matplotlib from python')
				socket = github_tools(pack_man, 'can-utils', repo) #this repo is can-utils repo
def downloaded_tools(pack_man, toolname, link): #WxPython and some other library
	general_use.update(pack_man)
	d = general_use.check_distribution()

	#NOTE: If pyOBD link doesn't work tell them the install.html is available
	down_rc = dependencies.download_install(toolname, link)
	if down_rc != 0:
		print ('DOWNLOAD FAILED: Failed to download file for', toolname, 'using download link:', link)
		print ('WITH ERROR CODE: ', down_rc)
	else:
		print ('DOWNLOAD SUCCESSFUL: Successfully downloaded file for', toolname)

		if toolname == 'pyobd':
			print ('Beginning pyobd installation...')
			if d == 'debian':
				deb_rc = dependencies.download_install('pyobd_0.9.3_all.deb', link_pyobd_debian)
				if deb_rc != 0:
					print ('Download Failed: Failed to download debian specific file') #need to figure out what this is for
			print ('Beginning pyserial installation...')
			pyserial_rc = dependencies.install_pyserial(link_pyserial)
			if pyserial_rc != 0:
				print ('INSTALLATION FAILED: Failed to install pyserial. Cannot complete pyobd installation')
				print ('WITH ERROR CODE:', pyserial_rc)
			else:
				print ('INSTALLATION SUCCESSFUL: Successfully installed pyobd')	
		elif toolname == 'o2oo':
			print ('Beginning o2oo installation...')
			extract_rc = subprocess.run(['tar', '-xzvf', 'O2OO-0.9.tar']).returncode
			if extract_rc != 0:
				print ('EXTRACTION FAILED: Failed to decompress the o2oo tar file')
				print ('WITH ERROR CODE:', extract_rc)
			else:
				print ('EXTRACTION SUCCESSFUL: Successfully extracted o2oo tar file. o2oo installation complete')
		elif toolname == 'romraider':
			print ('Beginning romraider installation...')
			rom_rc = dependencies.download_install('romraider', link)
			if rom_rc != 0:
				print ('INSTALLATION FAILED: Failed to install RomRaiders.')
				print ('WITH ERROR CODE:', rom_rc)
			else:
				print ('INSTALLATION SUCCESSFUL: Successfully installed RomRaiders')

def installed_tools(pack_man, toolname): #this function is for tools that are apt-getable / yumable
	general_use.update(pack_man)

	install_rc = -1

	if toolname == 'bluetooth tools': #this installs hciconfig, l2ping, hcitool, etc. 
		print ('Beginning bluetooth tools installation...')
		install_rc = dependencies.commandline_install(pack_man, 'bluetooth')
	elif toolname == 'btscanner':
		print ('Beginning btscanner installation...')
		install_rc = dependencies.commandline_install(pack_man, 'btscanner')
	elif toolname == 'gnuradio':
		print ('Beginning gnuradio installation...')
		install_rc = dependencies.commandline_install(pack_man, 'gnuradio')
	elif toolname == 'aircrack-ng':
		print ('Beginning aircrack-ng installation...')
		air_rc = dependencies.commandline_install(pack_man, 'aircrack-ng')

	if install_rc != 0:
		print ('INSTALLATION FAILED: Failed to install', toolname)
		print ('WITH ERROR CODE:', install_rc)
	else:
		print ('INSTALLATION SUCCESSFUL: Successfully installed', toolname)


















