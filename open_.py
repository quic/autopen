import general_use
import dependencies
import tools
import os
import subprocess

#OPEN TOOLS IN THE BACKGROUND

def open_(toolname):
    '''
    This function opens the specified tool (toolname)
    '''
    op_rc = -1

    t = ('Kayak', 'caringcaribou', 'Bluelog', 'bluemaho', 'canbus-utils')
    if toolname in t:
        current = os.getcwd()
        path = current + '/' + toolname
        os.chdir(path)

    #CAN TOOLS
    if toolname == 'Kayak':
        kayak_run_path = '/application/target/kayak/bin'
        print 'Changing directory to', kayak_run_path, '...'
        current_dir = os.getcwd()
        path = current_dir + kayak_run_path
        os.chdir(path)
        op_rc = subprocess.call('./kayak', shell = True)
    elif toolname == 'can-utils':
        op_rc = subprocess.call('gnome-terminal', shell=True)
    elif toolname == 'canbus-utils':
        op_rc = subprocess.call('gnome-terminal', shell=True)
    elif toolname == 'caringcaribou':   #will not be able to open
        # recommend adding the functionality to be able to open a specific
        # module but for now it just opens a terminal
        # current_dir = os.getcwd()
        # path = current_dir + '/tool'
        # os.chdir(path)
        # o = '/modules/'
        # op_rc = subprocess.run(['./cc.py', o]).returncode
        pass
    elif toolname == 'pyobd':   #BUGGY
        current = os.getcwd()
        path = current + '/pyobd-0.9.3'
        os.chdir(path)
        op_rc = subprocess.call('./pyobd',shell = True)
    elif toolname == 'o2oo':
        current = os.getcwd()
        path = current + '/O2OO-0.9'
        os.chdir(path)
        op_rc = subprocess.call('gnome-terminal', shell=True)
    elif toolname == 'can-utils-x':
        op_rc = subprocess.call('python main.py', shell = True)
    elif toolname == 'm2':
        op_rc = subprocess.call('python ./M2/m2GUI.py ', shell=True)
    elif toolname == 'j1939':
        op_rc = subprocess.call('gnome-terminal', shell=True)
    elif toolname == 'c0f':
        op_rc = subprocess.call('gnome-terminal', shell=True)
    elif toolname == 'udsim':
        op_rc = subprocess.call('gnome-terminal -e udsim can0', shell=True)
    elif toolname == 'savvy':
        op_rc = subprocess.call( '~/SavvyCAN/SavvyCAN', shell = True)
	#op_rc = subprocess.Popen('python ./M2/m2GUI.py', close_fds = True, shell = True)

    #BLUETOOTH TOOLS
    elif toolname == 'bluelog':
        op_rc = subprocess.call('./bluelog', shell = True)    #works if you have a bluetooth device up
    elif toolname == 'bluemaho':
        op_rc = subprocess.call('./bluemaho.py', shell = True)
    elif toolname == 'btscanner':
        op_rc = subprocess.call('gnome-terminal', shell=True)

    #WIFI TOOLS
    elif toolname == 'wireshark':
        op_rc = subprocess.call('gnome-terminal -e wireshark', shell = True)
    elif toolname == 'aircrack-ng':
        op_rc = subprocess.call('gnome-terminal', shell=True)
    elif toolname == 'tshark':
        op_rc = subprocess.call('gnome-terminal', shell=True)

    #SDR TOOLS
    elif toolname == 'gnuradio':
        op_rc = subprocess.call('gnome-terminal -e gnuradio-companion',shell = True)
    elif toolname == 'gqrx':
        op_rc = subprocess.call('gqrx', shell = True)
    elif toolname == 'freq':
        op_rc = subprocess.call('python ./M2/customFreq_modify.py &', shell=True)
    elif toolname == 'combine':
        op_rc = subprocess.Popen( '~/SavvyCAN/SavvyCAN &', close_fds = True, shell = True)
	op_rc = subprocess.Popen('python ./M2/m2GUI.py &', close_fds = True, shell=True)
    #MISCELLANEOUS TOOLS
    elif toolname == 'katoolin':
        op_rc = subprocess.call('gnome-terminal -e katoolin', shell = True)

    #For hardware tools that do not open anything (canbadger-hw for example)
    else:
        return 0


    if op_rc != 0:
        print 'STARTUP FAILED: Failed to open', toolname
        print 'ERROR CODE:', op_rc
    else:
        print 'STARTUP SUCCESSFUL: Successfully opened', toolname


    #check path to make sure it's in the autopen directory
    curr = os.getcwd()
    back_index = curr.rfind('/')
    ap_index = curr.find('autopen')
    if curr[back_index:] != '/autopen':
        path = curr[:ap_index+7]
    else:
        path = curr

    os.chdir(path)

    return op_rc

def test(tool):
    return 0

