'''
#Reference Links for me, might remove later we'll see how life goes
    can-utils : https://discuss.cantact.io/t/using-can-utils/24 (eric evenchick)
    canbus-utils : http://www.digitalbond.com/blog/2015/03/05/tool-release-digital-bond-canbus-utils/
    NPM: http://blog.teamtreehouse.com/install-node-js-npm-linux
    NPM2: http://www.hostingadvice.com/how-to/install-nodejs-ubuntu-14-04/#node-version-manager (May 2016)

TO DO:
    BACK-END:
        EXCEPTIONS:
            if repo has already been cloned, want it to continue with installation script
            if something fails to install. pass and skip the rest !!
        SMALL CHANGES:
            fix udsim code to print the correct library names
            caringcaribou hasn't been tested/not confirmed if install works because need to test it with socketCAN

    FRONT-END:
        ADD:
            highlight the buttons that are already installed, maybe gray out and make italics

    TEST:
        test caring caribou because a device needs to be set up to use it

    TO TELL USER:
        Note:
            can either clone our repo (this will probably still update github) or download the zip file and we will install git
            Make sure the user knows that this will all be cloned in the current directory aka most likely ~/Documents/autopen/
        Note:
            ROMRAIDER: SUBARU - THIS IS NOT WORKING, INVALID OR CORRUPT .JAR
                Warning: RomRaider is intended for use only by experienced tuners who understand the consequences. As with any tuning solution, the potential
                for engine damage is very high when altering your ECUs hard coded values. The use of appropriate equipment (ie, knock sensor, wideband oxygen
                sensor) is extremely important. By downloading RomRaider, you agree to assume all risks and accept its license. Use at your own risk.
        Note:
            ELM327:
                Be forewarned that the ELM327 has limited buffer space, so you will lose packets when sniffing,
                and transmission can be a bit imprecise, but if you're in a pinch this is the cheapest route.

TOOLS MAY BE INCLUDED:
    CANIBUS FOR ELM327:
        (go-server)
    CANTACT:
        will provide a section in here with the github link and the website link so that the user can build their own
        Also, will possibly provide steps on how to do so (will learn how to do this first)
    METASPLOIT HARDWARE BRIDGE
    AVRDUDESS:
        (this one not sure if im going to install yet)

'''

import general_use
import dependencies
import subprocess
import os
import uninstall

link_pyobd_debian = 'http://www.obdtester.com/download/pyobd_0.9.3_all.deb'
link_pyserial = 'https://sourceforge.net/projects/pyserial/files/pyserial/2.0/pyserial-2.0.zip/download'
link_pythoncan = 'https://bitbucket.org/hardbyte/python-can/get/77eea796362b.zip'
link_package = 'https://pkgconfig.freedesktop.org/releases/pkg-config-0.21.tar.gz' #needed for bluelog

def github_tools(pack_man, toolname, repo):
    '''
    This function installs the tools that use github. rc stands for returncode
    '''
    general_use.update(pack_man)
    f_rc = -1
    it = open('installed.txt', 'a')

    print "Cloning repository..."

    try:
        remove = uninstall.uninstall(toolname)
    except Exception as exception:
        print exception

    git_rc = dependencies.clone_git_repo(repo)
    if git_rc != 0:
        print 'CLONING FAILED: Failed to clone repository at', repo
        print 'ERROR CODE:', git_rc
    else:
        print 'CLONING SUCCESSFUL: Successfully cloned repository at', repo

    back_index = repo.rfind('/')
    dot_index = repo.rfind('.')
    folder_name = repo[back_index:dot_index]
    print 'Changing directory to', folder_name[1:], '...'
    os.chdir(os.getcwd() + folder_name)

    if toolname == 'canbus-utils':
        print 'Beginning canbus-utils installation...'
        npm_check_rc = dependencies.check_NPM(pack_man)
        if npm_check_rc != 0:
            print 'INSTALLATION FAILED: Failed to install canbus-utils dependencies. Check node.js and npm status'
            print 'ERROR CODE:', npm_check_rc
        else:
            print 'INSTALLATION SUCCESSFUL: Successfully installed node.js and npm'
            print 'Installing canbus-utils...'
            f_rc = subprocess.call(['npm', 'install'])
            if f_rc != 0:
                print 'INSTALLATION FAILED: Failed to run "npm install". Cannot complete canbus-utils installation'
                print 'ERROR CODE:', f_rc
            else:
                print 'INSTALLATION SUCCESSFUL: Successfully installed canbus-utils'

    elif toolname == 'Kayak':
        print 'Beginning kayak installation...'
        check_maven_rc = dependencies.commandline_install(pack_man, 'maven')
        if check_maven_rc != 0:
            print 'INSTALLATION FAILED: Failed to install maven. Cannot complete kayak installation'
            print 'ERROR CODE:', check_maven_rc
        else:
            print 'Installing jdk...'
            jdk_rc = dependencies.commandline_install(pack_man, 'default-jdk')
            if jdk_rc != 0:
                print 'INSTALLATION FAILED: Failed to install jdk. This compiler is needed to run mvn clean. Cannot complete kayak installation'
            else:
                ('Installing kayak...')
                f_rc = (subprocess.call(['mvn', 'clean', 'package']))
                if f_rc != 0:
                    print 'INSTALLATION FAILED: Failed to run "mvn clean package". Cannot complete kayak installation'
                    print 'ERROR CODE:', f_rc
                else:
                    print 'INSTALLATION SUCCESSFUL: Successfully installed kayak'

    elif toolname == 'caringcaribou':
        print 'Beginning caringcaribou installation...'
        print 'Setting up usb-to-can connection...'
        load_rc = subprocess.call(['sudo', 'modprobe', 'can'])
        if load_rc != 0:
            print 'LOAD FAILED: Failed to load CAN module. Cannot complete caringcaribou installation'
            print 'ERROR CODE:', load_rc
        else:
            print 'LOAD SUCCESSFUL: Successfully loaded CAN module'

            #user needs to know the CAN bus they are on (change can_bus)
            #user needs to know the bitrate that the bus runs with (change bitrate)
            #add front-end functionality later so that the user can input it from there vs. modifying the code

            can_bus = 'can0'
            bitrate = 500000
            print 'Setting up CAN device...'
            setup_can_rc = subprocess.call(['sudo', 'ip', 'link', 'set', can_bus, 'up', 'type', 'can', 'bitrate', str(bitrate)])
            if setup_can_rc != 0:
                print 'SETUP FAILED: Failed to set-up can device.'
                print 'ERROR CODE:', setup_can_rc
            else:
                print 'SETUP SUCCESSFUL: Successfully set-up can device. This will now display as a normal network interface as can0'
                pcan_rc = dependencies.download_install(link_pythoncan)
                if pcan_rc != 0:
                    print 'DOWNLOAD FAILED: Failed to download pythoncan from', link_pythoncan, 'Cannot complete caringcaribou installation'
                    print 'ERROR CODE:', pcan_rc
                else:
                    print 'DOWNLOAD SUCCESSFUL: Successfully downloaded pythoncan from', link_pythoncan
                    f_rc = subprocess.call(['sudo', 'python', 'setup.py', 'install'])
                    if f_rc != 0:
                        print 'DOWNLOAD SUCCESSFUL: Failed to install python-can. Cannot complete caringcaribou installation'
                        print 'ERROR CODE:', f_rc
                    else:
                        print 'INSTALLATION SUCCESSFUL: Successfully installed python-can. Caringcaribou installation complete'


    elif toolname == 'c0f':
        print 'Beginning c0f installation'
        print 'Installing gem...'
        gem_rc = dependencies.commandline_install(pack_man, 'rubygems')
        if gem_rc != 0:
            print 'INSTALLATION FAILED: Failed to install gem. Cannot complete c0f installation'
            print 'ERROR CODE:', gem_rc
        else:
            print 'INSTALLATION SUCCESSFUL: Successfully installed gem'
            headers_rc = dependencies.commandline_install(pack_man, 'ruby-dev')
            if headers_rc != 0:
                print 'INSTALLATION FAILED: Failed to install header files for ruby. Cannot complete c0f installation'
                print 'ERROR CODE:', headers_rc
            else:
                print 'INSTALLATION SUCCESSFUL: Successfully installed header files for ruby'
                print 'Installing sqlite3 library...'
                sql_rc = dependencies.commandline_install(pack_man, "libsqlite3-dev")
                if sql_rc != 0:
                    print 'INSTALLATION FAILED: Failed to install sqlite3 library'
                    print 'ERROR CODE:'. sql_rc
                else:
                    print 'INSTALLATION SUCCESSFUL: Successfully installed sqlite3'
                    print 'Installing c0f...'
                    f_rc = subprocess.call(['sudo', 'gem', 'install', 'c0f'])
                    if f_rc != 0:
                        print 'INSTALLATION FAILED: Failed to install c0f.'
                        print 'ERROR CODE:', f_rc
                    else:
                        print 'INSTALLATION SUCCESSFUL: Successfully installed c0f'

    elif toolname == 'udsim':
        print 'Beginning udsim installation...'
        f_rc = 0

        ttf_dev = dependencies.commandline_install(pack_man, 'libsdl2-ttf-dev')
        image = dependencies.commandline_install(pack_man, 'libsdl2-image-2.0.0')
        returncode_list = [ttf_dev, image]
        lib_names = ['ttf-dev', 'image']
        for i, j in enumerate(returncode_list):
            if j != 0:
                f_rc = -1
                print 'INSTALLATION FAILED: Could not install library libsdl2-', lib_names[i]
                print 'ERROR CODE:', j
            else:
                print 'INSTALLATION SUCCESSFUL: Successfully installed library libsdl2-', i
        if f_rc != 0:
            print 'INSTALLATION FAILED: Failed to install libraries needed to compile UDSIM. Cannot complete udsim installation'
            print 'ERROR CODE:', f_rc
        else:
            print 'INSTALLATION COMPLETE: Successfully installed the libraries needed to compile UDSIM.'


    elif toolname == 'Bluelog': #has an optional web mode so when running want to add that functionality.  (just run make to run)
        print 'Installing bluelog...'
        f_rc = subprocess.call(['sudo', 'make', 'install'])
        if f_rc != 0:
            print 'INSTALLATION FAILED: Failed to install bluelog'
            print 'ERROR CODE:', f_rc
        else:
            print 'INSTALLATION SUCCESSFUL: Successfully installed bluelog'
            it.write('bluelog')
    elif toolname == 'bluemaho':
        print 'Beginning bluemaho installation...'
        print 'Installing bluemaho dependencies...'
        wxpython = dependencies.commandline_install(pack_man, 'python-wxgtk3.0')
        bluez = dependencies.commandline_install(pack_man, 'bluez')
        config = dependencies.download_install(link_package)
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
                    print 'INSTALLATION FAILED: Failed to install dependency', depend[i], '. This may remove the ability to run a specific attack using Bluemaho. Please refer to the github repo'
                    print 'ERROR CODE:', j
                    essential = j
                else:
                    print 'INSTALLATION FAILED: Failed to install dependency', depend[i]
                    essential = -1

        if essential != 0:
            print 'INSTALLATION FAILED: Failed to install all Bluemaho dependencies'
        else:
            print 'INSTALLATION SUCCESSFUL: Successfully installed all dependencies for Bluemaho'
            print 'Building Bluemaho...'
            c_dir = os.getcwd()
            path = c_dir + '/config'
            os.chdir(path)
            f_rc = subprocess.call(['./build.sh'])
            if f_rc != 0:
                print 'BUILD FAILED: Failed to build and complete installation of Bluemaho'
                print 'ERROR CODE:', f_rc
            else:
                print 'BUILD SUCCESSFUL: Successfully completed Bluemaho build'
                general_use.move_up_directory()

    elif toolname == 'katoolin':
        cp_rc = subprocess.call(['sudo', 'cp', 'katoolin.py', '/usr/bin/katoolin'])
        if cp_rc != 0:
            print 'COPY FAILED: Could not copy katoolin.py to /usr/bin/katoolin'
            print 'ERROR CODE:', cp_rc
        else:
            print 'COPY SUCCESSFUL: Successfully copied katoolin.py to /usr/bin/katoolin'
            print "Setting /usr/bin/katoolin to executable..."
            f_rc = subprocess.call(["sudo", "chmod", "+x", "/usr/bin/katoolin"])#executable script for both you and your group but not for the world.
            if f_rc != 0:
                print "CONVERSION FAILED: Could not make /usr/bin/katoolin executable"
                print "ERROR CODE:", f_rc
            else:
                print "CONVERSION SUCCESSFUL: /usr/bin/katoolin set to executable"
                print 'INSTALLATION SUCCESSFUL: Successfully installed katoolin'

    elif toolname == 'j1939':
        f_rc = subprocess.call(['make'])
        if f_rc != 0:
            print 'INSTALLATION FAILED: Failed to install can-utils-j1939. Could not run create executables running make'
            print 'ERROR CODE:', f_rc
        else:
            print 'INSTALLATION SUCCESSFUL: Successfully installed can-utils-j1939'

    elif toolname == 'canbadger-hw':
        f_rc = 0
        print 'REPOSITORY AVAILABLE: The CANBadger repository has been cloned to your machine'
        print 'If you need help, refer to the tutorial on the right side of the tool page to build the hardware'

    elif toolname == 'canbadger-sw':
        print 'here1'
        libs = ['python-qt4', 'pyqt4-dev-tools', 'qtcreator']
        rcs = [dependencies.commandline_install(pack_man, i) for i in libs]

        print 'here2'
        for i,j in enumerate(rcs):
            if j != 0:
                print 'here3'
                if i < 3:
                    print 'here4'
                    print 'INSTALLATION SUCCESSFUL: Failed to install dependency', libs[i], '. This may remove the ability to run a specific attack using Bluemaho. Please refer to the github repo'
                    print 'ERROR CODE:', j
                    f_rc = j
                else:
                    print 'here5'
                    print 'INSTALLATION FAILED: Failed to install dependency', libs[i]
                    f_rc = -1

        if f_rc != 0:
            print 'here6'
            print 'INSTALLATION FAILED: Failed to install canbadger-server dependencies'
            print 'ERROR CODE:', f_rc
        else:
            print 'here7'
            print 'INSTALLATION SUCCESSFUL: Successfully installed all dependencies for canbadger-server'



    #changes back to /autopen --> writes to installed.txt if the tool has been installed successfully
    general_use.move_up_directory()
    if f_rc == 0:
        it.write(toolname)
        it.write('\n')
    it.close()
    return f_rc

def downloaded_tools(pack_man, toolname, link): #WxPython and some other library
    '''
    This function installs tools that are found on the internet by using the curl command
    '''
    general_use.update(pack_man)
    d = general_use.check_distribution()
    f_rc = -1
    it = open('installed.txt', 'a')

    #NOTE: If pyOBD link doesn't work, the install.html is available
    down_rc = dependencies.download_install(link)
    if down_rc != 0:
        print 'DOWNLOAD FAILED: Failed to download file for', toolname, 'using download link:', link
        print 'ERROR CODE:', down_rc
    else:
        print 'DOWNLOAD SUCCESSFUL: Successfully downloaded file for', toolname

        if toolname == 'pyobd': #not 100% sure this is going to work (pyserial = 2.0, wxpython = 2.4, doesnt work with 2.5)
            print 'Beginning pyobd installation...'
            if d == 'debian':
                deb_rc = dependencies.download_install(link_pyobd_debian)
                if deb_rc != 0:
                    print 'Download Failed: Failed to download debian specific file'
            print 'Installing pyserial...'
            pyserial_rc = subprocess.call(['python', '-m', 'pip', 'install', 'pyserial'])
            if pyserial_rc != 0:
                print 'INSTALLATION FAILED: Failed to install pyserial. Cannot complete pyobd installation'
                print 'ERROR CODE:', pyserial_rc
            else:
                print 'INSTALLATION SUCCESSFUL: Successfully installed pyserial'
                print 'Installing WxPython version 3.0...'
                wx_rc = dependencies.commandline_install(pack_man, 'python-wxgtk3.0')
                if wx_rc != 0:
                    print 'INSTALLATION FAILED: Failed to install python-wxgtk3.0. Cannot complete pyobd installation'
                    print 'ERROR CODE:', wx_rc
                else:
                    print 'INSTALLATION SUCCESSFUL: Successfully installed python-wxgtk3'
                    print 'Extracting pyobd...'
                    ext_rc = subprocess.call(['tar', '-xzvf', 'pyobd_0.9.3.tar.gz'])
                    if ext_rc != 0:
                        print 'EXTRACTION FAILED: Failed to decompress pyobd tar file'
                        print 'ERROR CODE:', ext_rc
                    else:
                        print 'EXTRACTION SUCCESSFUL: Successfully decompressed tar file. Successfully installed pyobd'
                        print 'Removing .tar.gz file...'
                        f_rc = subprocess.call(['rm', '-rf', 'pyobd_0.9.3.tar.gz'])
                        if f_rc != 0:
                            print 'REMOVAL FAILED: Failed to remove pyobd tar.gz file'
                            print 'ERROR CODE', f_rc
                        else:
                            print 'REMOVAL SUCCESSFUL: Successfully removed pyobd tar.gz file'

        elif toolname == 'o2oo':
            print 'Beginning o2oo installation...'
            extract_rc = subprocess.call(['tar', '-xzvf', 'O2OO-0.9.tgz'])
            if extract_rc != 0:
                print 'EXTRACTION FAILED: Failed to decompress the o2oo tar file'
                print 'ERROR CODE:', extract_rc
            else:
                print 'EXTRACTION SUCCESSFUL: Successfully extracted o2oo tar file.'
                print 'Installing o2oo dependencies...'

                l = ['libncurses-dev', 'libsqlite3-dev', 'libgps-dev', 'libgd2-xpm-dev', 'libhpdf-dev', 'libtinyxml2-dev', 'libcurl4-openssl-dev', 'libfftw3-dev']
                rc = [dependencies.commandline_install(pack_man, i) for i in l]

                ins = 0

                for i,j in enumerate(rc):
                    if j != 0:
                        print 'INSTALLATION FAILED: Failed to install dependency', l[i], '. This may remove the ability to run a specific attack using Bluemaho. Please refer to the github repo'
                        print 'ERROR CODE:', j
                        ins = j

                if ins != 0:
                    print 'INSTALLATION FAILED: Failed to install o2oo dependencies'
                else:
                    print 'INSTALLATION SUCCESSFUL: Successfully installed all dependencies for o2oo'
                    current = os.getcwd()
                    p = current + '/O2OO-0.9'
                    os.chdir(p)
                    mak_rc = subprocess.call(['sudo', 'make', 'install'])
                    if mak_rc != 0:
                        print 'BUILD FAILED: Failed to build o2oo'
                        print 'ERROR CODE:', mak_rc
                    else:
                        print 'BUILD SUCCESSFUL: Successfully built o2oo and installed'
                        print 'Removing .tgz file...'
                        f_rc = subprocess.call(['rm', '-rf', 'O2OO-0.9.tgz'])
                        if f_rc != 0:
                            print 'REMOVAL FAILED: Failed to remove o2oo .tgz file'
                            print 'ERROR CODE', f_rc
                        else:
                            print 'REMOVAL SUCCESSFUL: Successfully removed o2oo .tgz file'
                            general_use.move_up_directory()

        elif toolname == 'romraider':
            print 'Beginning romraider installation...'
            f_rc = dependencies.download_install(link)
            if f_rc != 0:
                print 'INSTALLATION FAILED: Failed to install RomRaiders.'
                print 'ERROR CODE:', f_rc
            else:
                print 'INSTALLATION SUCCESSFUL: Successfully installed RomRaiders'

    if f_rc == 0:
        it.write(toolname)
        it.write('\n')
    it.close()
    return f_rc

def installed_tools(pack_man, toolname):
    '''
        This function installs tools that are apt-getable / yumable
    '''
    print 'in installed tools'
    general_use.update(pack_man)

    install_rc = -1

    if toolname == 'btscanner':
        print 'Beginning btscanner installation...'
        install_rc = dependencies.commandline_install(pack_man, 'btscanner')
    elif toolname == 'gnuradio':
        print 'Beginning gnuradio installation...'
        install_rc = dependencies.commandline_install(pack_man, 'gnuradio')
    elif toolname == 'aircrack-ng':
        print 'Beginning aircrack-ng installation...'
        install_rc = dependencies.commandline_install(pack_man, 'aircrack-ng')
    elif toolname == 'wireshark':
        print 'Beginning wireshark installation...'
        install_rc = dependencies.commandline_install(pack_man, 'wireshark')
    elif toolname == 'can-utils':
        print 'Beginning can-utils installation...'
        install_rc = dependencies.commandline_install(pack_man, 'can-utils')
    elif toolname == 'tshark':
        print 'Beginning tshark installation...'
        install_rc = dependencies.commandline_install(pack_man, 'tshark')
    elif toolname == 'gqrx':
        print 'Beginning gqrx installation...'
        install_rc = dependencies.commandline_install(pack_man, 'gqrx-sdr')

    if install_rc != 0:
        print 'INSTALLATION FAILED: Failed to install', toolname
        print 'ERROR CODE:', install_rc
    else:
        print 'INSTALLATION SUCCESSFUL: Successfully installed', toolname
        if toolname == 'gnuradio':
            dep_rc = dependencies.commandline_install(pack_man, 'gr-osmosdr')
            if dep_rc != 0:
                print 'INSTALLATION FAILED: Failed to install gr-osmosdr dependency. gnuradio may not have certain features'
                print 'ERROR CODE:', dep_rc
            else:
                print 'INSTALLATION SUCCESSFUL: Successfully installed gr-osmosdr dependency for gnuradio'
        elif toolname == 'gqrx':
            dep_rc = dependencies.commandline_install(pack_man, 'libvolk1-bin')
            if dep_rc != 0:
                print 'INSTALLATION FAILED: Failed to install libvolk1-bin. gqrx will still work as expected'
                print 'libvolk1-bin is a tool that optimizes GNU Radio performance'
            else:
                print 'INSTALLATION SUCCESSFUL: Successfully installed libvolk1-bin. This optimizes gqrx usage'
                run_rc = subprocess.call(['volk_profile'])
                if run_rc != 0:
                    print 'RUN FAILED: Failed to run volk_profile to complete gqrx usage optimization'
                    print 'gqrx will still run as expected'
                    print 'ERROR CODE:', run_rc
                else:
                    print 'RUN SUCCESSFUL: Successfully ran volk_profile. gqrx optimization complete'
        elif toolname == 'can-utils':
            print 'Ensuring CAN modules are enabled...'
            f_rc = subprocess.call(['sudo', 'modprobe', 'can'])   #not sure if going to keep this yet mainly cuz might not be necessary, also need to check if redhat has modprobe, it should but need to check (also just check generally if other linux has this already installed)
            if f_rc != 0:
                print 'CHECK FAILED: Failed to add a LKM to the kernel. Can-utils may not be fully functional'
                print 'ERROR CODE:', f_rc
            else:
                print 'CHECK SUCCESSFUL: Successfully added a LKM to the kernel'


    #don't necessarily need to not include in list of installed tools, just might want to list that the libraries were not installed. (log.txt file)
    it = open('installed.txt', 'a')
    if install_rc == 0:
        it.write(toolname)
        it.write('\n')
    it.close()
    return install_rc

