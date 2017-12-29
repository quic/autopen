'''
This script has functions that can be used across all scripts
'''

import platform
import subprocess
import os

def check_distribution():
    '''
    This function checks which distribution the user is running and returns
    that distribution type
    '''
    distro = platform.linux_distribution()[0].lower()
    return distro

def package_tool(distro):
    '''
    This function returns which package manager the system uses to install
    scripts based on the distribution
    '''
    debian_distro_tuple = ('kali', 'debian', 'ubuntu')
    red_hat_distro_tuple = ('red hat')
    package_tool = ''

    if distro in debian_distro_tuple:
        package_tool = 'apt-get'
    elif distro in red_hat_distro_tuple:
        package_tool = 'yum'
    return package_tool

def update(pack_man):
    '''
    This function updates software packages based on repository state
    This needs to be included at the beginning of every major installation
    function
    '''
    update_rc = subprocess.run(['sudo', pack_man, 'update']).returncode
    if update_rc != 0:
        print 'UPDATE FAILED: Failed to update system'
        print 'ERROR CODE:', update_rc
    else:
        print 'UPDATE SUCCESSFUL: Successfully updated system'

def move_up_directory():
    '''
    This function moves up one directory from where the program is currently
    running. To successfully install/open tools, different files need to be
    used that could be in other directories. This is used to make sure that at
    the end of the process for that tool, the program ends in the main autopen
    directory. 
    '''
    curr_working_dir = os.getcwd()
    up_dir_index = curr_working_dir.rfind('/')

    if not up_dir_index is 0:
        os.chdir(curr_working_dir[:up_dir_index])

