#install github if dont have git
#git clone to get katoolin
#Kali Repositories (and make sure to update)

#can install specific tools
# View Categories > # > # and it installs

#Need to change this to be backwards compatable with Python 2

'''

This is the backbone of the Bluetooth tools. It does the following:

1. Installs github if the machine does not have git (or maybe the software will come with github)
2. Clones katoolin so that can run on machine (maybe this will allow users to install tools from Kali Linux that they want)
3. Install Kali Repositories (this step has to happen to be able to install rest of the tools)
4. Installs Bluetooth essentials allowing the user to use

'''

import subprocess
import systemInformation

#need root access in order to run these ?
#but that's a security issue, dk if want to have user install these. Well I guess we aren't the ones that actually check. Assuming that when the user installs the package will allow for root access.
#log everything to /var/log/install_tools.log (user needs root access to this)


# store the Operating System version. Install of katoolin apps depends on OS. apt-get vs brew
osVersion = systemInformation.getOSInfo()
print(osVersion)


def setCommand(osVersion):
    installCmd = ""
    if osVersion == "linux" or "linux2":
        installCmd = "apt-get"
    elif osVersion == "darwin":
        installCmd = "brew"
    return installCmd


def run(osVersion):
    osv = osVersion
    osVersionCommand = setCommand(osv)
    print ("Installing git...")
    git_EC = subprocess.run(["sudo",osVersionCommand , "install", "git"])
    if git_EC.returncode != 0:
        print ("INSTALLATION FAILED: Could not install git")
        print ("ERROR CODE:", git_EC.returncode)
    elif git_EC.returncode == 0:
        print ("INSTALLATION SUCCESSFUL: Git successfully installed")
        print ("Cloning Katoolin...")
        katoolin_EC = subprocess.run(["git", "clone", "https://github.com/LionSec/katoolin.git"]) #installs Katoolin
        if katoolin_EC.returncode != 0:
            print ("INSTALLATION FAILED: Could not clone Katoolin Repository and install Katoolin")
            print ("ERROR CODE:", katoolin_EC.returncode)
        elif katoolin_EC.returncode == 0:
            print ("INSTALLATION SUCCESSFUL: Katoolin successfully installed")
            print ("Setting /usr/bin/katoolin to executable...")
            changemode_EC = subprocess.run(["chmod", "754", "/usr/bin/katoolin"]) #executable script for both you and your group but not for the world.
            if changemode_EC.returncode != 0:
                print ("CONVERSION FAILED: Could not make /usr/bin/katoolin executable")
                print ("ERROR CODE:", changemode_EC.returncode)
            elif changemode_EC.returncode == 0:
                print ("CONVERSION SUCCESSFUL: /usr/bin/katoolin set to executable")
                enter_katoolin_EC = subprocess.run(["katoolin"])
                print ("Starting up Katoolin...")
                if enter_katoolin_EC.returncode != 0:
                    print ("KATOOLIN STARTUP FAILED: attempt to reinstall with the tool or go to README for instructions on how to install")
                    print ("ERROR CODE:", enter_katoolin_EC.returncode)
                elif enter_katoolin_EC.returncode == 0:
                    print ("STARTUP SUCCESSFUL: Entering Katoolin...")


#guide them through using the tool



