'''
This script begins by first checking the distribution that the user has and
will install the following commands/libraries:

git
python2

Assumes user is running as root and has apt-get installed
'''

import general_use
import dependencies
import subprocess

def install_basics(pack_man, program_list):
    '''
    This function installs every program in program_list
    '''
    for program in program_list:
        print 'Installing', program
        return_code = dependencies.commandline_install(pack_man, program)
        if not return_code is 0:
            print 'INSTALLATION FAILED: Could not install', program
            print 'ERROR CODE:', return_code
        else:
            print 'INSTALLATION SUCCESSFUL:', program, 'succesfully installed'

def install_python(pack_man):
    '''
    This function installs or updates Python 2 depending on whether it is already on the system or not
    '''
    print 'Installing/Updating Python 2...'
    p_rc = dependencies.commandline_install(pack_man, "python")
    if p_rc != 0:
        print 'INSTALLATION FAILED: Could not install Python 2'
        print "ERROR CODE:", p_rc
    else:
        print 'INSTALLATION SUCCESSFUL: Python 2 successfully installed'

def install_git(pack_man):
    '''
    This function installs or updates git depending on whether it is already
    on the system or not
    '''
    print 'Installing git...'
    g_rc = dependencies.commandline_install(pack_man, "git")
    if g_rc != 0:
        print "INSTALLATION FAILED: Could not install git. This is needed to\
               install some of the tools"
        print "ERROR CODE:", g_rc
    else:
        print "INSTALLATION SUCCESSFUL: Git successfully installed"

def install_curl(pack_man):
    '''
    This function installs curl
    '''
    print 'Installing curl...'
    c_rc = dependencies.commandline_install(pack_man, 'curl')
    if c_rc != 0:
        print 'INSTALLATION FAILED: Could not install curl. This is needed to install some of the tools'
        print 'ERROR CODE:', c_rc
    else:
        print 'INSTALLATION SUCCESSFUL: curl successfully installed'

def install_pip(pack_man):
    '''
    This function installs pip
    '''
    print 'Installing pip'
    pip_rc = dependencies.commandline_install(pack_man, 'python3-pip')
    if pip_rc != 0:
        print 'INSTALLATION FAILED: Failed to install pip. This is needed to install some dependencies for tools'
        print 'ERROR CODE:', pip_rc
    else:
        print 'INSTALLATION COMPLETE: Successfully installed pip'

def main():
    distro = general_use.check_distribution()
    pack_man = general_use.package_tool(distro)
    program_list = ('python', 'git', 'curl', 'pip')
    install_basics(pack_man, program_list)
    # install_python(pack_man)
    # install_git(pack_man)
    # install_curl(pack_man)
    # install_pip(pack_man)

if __name__ == '__main__':
    main()
