import general_use
import dependencies
import tools
import subprocess
import os

class Tool:
    def __init__(self):
        self.tool_name = ''
        self.tool_path = ''
        self.tool_type = ''

    def init(self, tool_name, tool_path, tool_type):
        self.tool_name = tool_name
        self.tool_path = tool_path
        self.tool_type = tool_type

def uninstall(toolname):
    d = general_use.check_distribution()
    pack_man = general_use.package_tool(d)
    rm_rc = -1

    #check path to make sure it's in the autopen directory
    curr = os.getcwd()
    back_index = curr.rfind('/')
    ap_index = curr.find('autopen')
    if curr[back_index:] != '/autopen':
        path = curr[:ap_index+7]
    else:
        path = curr

    os.chdir(path)

    try:
        if toolname == 'canbus-utils':
            rm_rc = subprocess.call(['rm', '-rf', 'canbus-utils'])
        elif toolname == 'Kayak':
            rm_rc = subprocess.call(['rm', '-rf', 'Kayak'])
        elif toolname == 'caringcaribou':
            rm_rc = subprocess.call(['rm', '-rf', 'caringcaribou'])
        elif toolname == 'c0f':
            rm_rc = subprocess.call(['rm', '-rf', 'c0f'])
        elif toolname == 'udsim':
            rm_rc = subprocess.call(['rm', '-rf', 'UDSim'])
        elif toolname == 'katoolin':
            rm_rc = subprocess.call(['rm', '-rf', 'katoolin'])
        elif toolname == 'bluelog':
            rm_rc = subprocess.call(['rm', '-rf', 'Bluelog'])
        elif toolname == 'bluemaho':
            rm_rc = subprocess.call(['rm', '-rf', 'bluemaho'])
        elif toolname == 'j1939':
            rm_rc = subprocess.call(['rm', '-rf', 'can-utils-j1939'])
        elif toolname == 'canbadger-hw':
            rm_rc = subprocess.call(['rm', '-rf', 'CANBadger'])

            #https://github.com/Gutenshit/CANBadger/wiki/Getting-the-board-ready

        elif toolname == 'canbadger-sw':
            rm_rc = subprocess.call(['rm', '-rf', 'CANBadger-Server'])

        elif toolname == 'pyobd':
            try:
                rm_rc = subprocess.call(['rm', '-rf','pyobd_0.9.3.tar.gz'])
            except:
                pass
            try:
                rm_rc = subprocess.call('rm', '-rf', 'pyobd-0.9.3')
            except:
                pass
        elif toolname == 'o2oo':
            try:
                rm_rc = subprocess.call(['rm', '-rf','O2OO-0.9.tgz'])
            except:
                pass
            try:
                rm_rc = subprocess.call('rm', '-rf', 'O2OO-0.9')
            except:
                pass

        elif toolname == 'btscanner':
            rm_rc = subprocess.call(['sudo', pack_man, 'purge', '-y','btscanner'])
        elif toolname == 'gnuradio':
            rm_rc = subprocess.call(['sudo', pack_man, 'purge','-y', 'gnuradio'])
        elif toolname == 'aircrack-ng':
            rm_rc = subprocess.call(['sudo', pack_man, 'purge','-y', 'aircrack-ng'])
        elif toolname == 'gqrx':
            rm_rc = subprocess.call(['sudo', pack_man, 'purge', '-y','gqrx'])
        elif toolname == 'can-utils':
            rm_rc = subprocess.call(['sudo', pack_man, 'purge','-y', 'can-utils'])
        elif toolname == 'wireshark':
            rm_rc = subprocess.call(['sudo', pack_man, 'purge','-y', 'wireshark'])
        elif toolname == 'tshark':
            rm_rc = subprocess.call(['sudo', pack_man, 'purge','-y', 'tshark'])

    except:
        print ('Not in correct directory')
        print ('current directory is: ', os.getcwd())
        pass

    if rm_rc == 0:
        #remove the tool from the text file
        f = open("installed.txt","r+")
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != toolname:
                f.write(i)
        f.truncate()

        print ('UNINSTALL SUCCESSFUL: Successfully uninstalled', toolname)

    return rm_rc

def test(name):
    return 0

