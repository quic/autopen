import general_use
import dependencies
import subprocess
import os

def update(toolname):
    # add exception to check if the tool is installed, in case they
    # accidentally click this. Possibly add a pop-up that says "need to
    # install first"

    #check path to make sure it's in the autopen directory
    curr = os.getcwd()
    back_index = curr.rfind('/')
    ap_index = curr.find('autopen')
    if curr[back_index:] != '/autopen':
        path = curr[:ap_index+7]
    else:
        path = curr
    os.chdir(path)

    github_tools = ('canbus-utils', 'Kayak', 'caringcaribou', 'c0f', 'udsim', 'j1939', 'canbadger-hw', 'canbadger-sw', 'katoolin', 'bluelog', 'bluemaho')
    downloaded_tools = ('pyobd', 'o2oo', 'romraider')
    commandline_tools = ('bluez', 'btscanner', 'gnuradio', 'aircrack-ng', 'wireshark', 'can-utils', 'tshark', 'gqrx')

    try:
        if toolname in github_tools:
            if toolname == 'udsim':
                p = os.getcwd() + '/UDSim'
                os.chdir(p)
            elif toolname == 'j1939':
                p = os.getcwd() + '/can-utils-j1939'
                os.chdir(p)
            elif toolname == 'canbadger-hw':
                p = os.getcwd() + '/CANBadger'
                os.chdir(p)
            elif toolname == 'canbadger-sw':
                p = os.getcwd() + '/CANBadger-Server'
                os.chdir(p)
            elif toolname == 'bluelog':
                p = os.getcwd() + '/Bluelog'
                os.chdir(p)
            else:
                p = os.getcwd() + '/' + toolname
                os.chdir(p)

            # github tools are updated based on whether local commit is the same version as the master commit    

            master = subprocess.call(['git', 'rev-parse', 'master'], stdout=subprocess.PIPE).stdout
            origin_master = subprocess.call(['git', 'rev-parse', 'master'], stdout=subprocess.PIPE).stdout

            master_id = master.decode('utf-8')
            origin_master_id = origin_master.decode('utf-8')

            #users repo is behind master
            if master_id != origin_master_id:
                print 'Updating', toolname, '...'
                pull_rc = subprocess.call(['git', 'pull', 'origin', 'master'])
                if pull_rc != 0:
                    print 'UPDATE FAILED: Failed to update', toolname
                    print 'ERROR CODE:', pull_rc
                else:
                    print 'UPDATE SUCCESSFUL: Successfully updated', toolname
                    return 0
            else:
                print toolname, 'is already up to date'
                return 0

        elif toolname in commandline_tools:
            print 'Updating', toolname, '...'
            update_rc = subprocess.call(['sudo', 'apt-get', '--only-upgrade', '-y', 'install', toolname])
            if update_rc != 0:
                print 'UPDATE FAILED: Failed to update', toolname
                print 'ERROR CODE:', update_rc
            else:
                print 'UPDATE SUCCESSFUL: Successfully updated', toolname
                return 0
    except:
        print 'Make sure tool is installed. Tool needs to be installed before updating'
        return 0

def test(name):
    return 0

