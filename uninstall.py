import general_use
import dependencies
import tools
import subprocess
import os

class Tool:
    def __init__():
        self.tool_name = ''
        self.tool_path = ''
        self.tool_type = ''

    def init(self, tool_name, tool_path, tool_type):
        self.tool_name = tool_name
        self.tool_path = tool_path
        self.tool_type = tool_type

def uninstall(toolname):
    try:
        fh = open('tool_and_repo.txt','r')
    except IOError as io_error:
        print io_error

    lines = fh.readlines()
    tool = Tool()
    for line in lines:
        tool_name, tool_path, tool_type = line.split(',')
        if tool_name is toolname:
            tool.init(tool_name, tool_path, tool_type)
            break

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
            rm_rc = subprocess.run(['rm', '-rf', 'canbus-utils']).returncode
        elif toolname == 'Kayak':
            rm_rc = subprocess.run(['rm', '-rf', 'Kayak']).returncode
        elif toolname == 'caringcaribou':
            rm_rc = subprocess.run(['rm', '-rf', 'caringcaribou']).returncode
        elif toolname == 'c0f':
            rm_rc = subprocess.run(['rm', '-rf', 'c0f']).returncode
        elif toolname == 'udsim':
            rm_rc = subprocess.run(['rm', '-rf', 'UDSim']).returncode
        elif toolname == 'katoolin':
            rm_rc = subprocess.run(['rm', '-rf', 'katoolin']).returncode
        elif toolname == 'bluelog':
            rm_rc = subprocess.run(['rm', '-rf', 'Bluelog']).returncode
        elif toolname == 'bluemaho':
            rm_rc = subprocess.run(['rm', '-rf', 'bluemaho']).returncode
        elif toolname == 'j1939':
            rm_rc = subprocess.run(['rm', '-rf', 'can-utils-j1939']).returncode
        elif toolname == 'canbadger-hw':
            rm_rc = subprocess.run(['rm', '-rf', 'CANBadger']).returncode

            #https://github.com/Gutenshit/CANBadger/wiki/Getting-the-board-ready

        elif toolname == 'canbadger-sw':
            rm_rc = subprocess.run(['rm', '-rf', 'CANBadger-Server']).returncode

        elif toolname == 'pyobd':
            try:
                rm_rc = subprocess.run(['rm', '-rf','pyobd_0.9.3.tar.gz']).returncode
            except:
                pass
            try:
                rm_rc = subprocess.run('rm', '-rf', 'pyobd-0.9.3').returncode
            except:
                pass
        elif toolname == 'o2oo':
            try:
                rm_rc = subprocess.run(['rm', '-rf','O2OO-0.9.tgz']).returncode
            except:
                pass
            try:
                rm_rc = subprocess.run('rm', '-rf', 'O2OO-0.9').returncode
            except:
                pass

        elif toolname == 'btscanner':
            rm_rc = subprocess.run(['sudo', pack_man, 'purge', '-y','btscanner']).returncode
        elif toolname == 'gnuradio':
            rm_rc = subprocess.run(['sudo', pack_man, 'purge','-y', 'gnuradio']).returncode
        elif toolname == 'aircrack-ng':
            rm_rc = subprocess.run(['sudo', pack_man, 'purge','-y', 'aircrack-ng']).returncode
        elif toolname == 'gqrx':
            rm_rc = subprocess.run(['sudo', pack_man, 'purge', '-y','gqrx']).returncode
        elif toolname == 'can-utils':
            rm_rc = subprocess.run(['sudo', pack_man, 'purge','-y', 'can-utils']).returncode
        elif toolname == 'wireshark':
            rm_rc = subprocess.run(['sudo', pack_man, 'purge','-y', 'wireshark']).returncode
        elif toolname == 'tshark':
            rm_rc = subprocess.run(['sudo', pack_man, 'purge','-y', 'tshark']).returncode

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

