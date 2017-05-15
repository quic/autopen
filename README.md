# autopen

Autopen is an open-source toolkit designed to assist security analysts, manufacturers, and various professionals to detect 
potential vulnerabilities in vehicles using the tools that will be provided. The product is meant to simplify installation, 
help the user in getting to know what tools are at their disposal, and teach them how to use them. 

## Installation

Autopen has only been tested on Ubuntu and Kali Linux. Other linux distributions may work but cannot be guaranteed. Because most of the scripts are written in python 3, these instructions assume you have python 3 installed. To install Python 3 on Linux, run the following command in terminal: 

sudo apt-get install python3

sudo apt-get install python3-pip

### VM Install

Running the software on a VM is different then running it on a dedicated install. VM's generally are missing more dependencies so require more installations. Kivy in specific needs to be run in a Python environment in the VM. Because there are a number of steps needed to do this, we have created a script that will install the dependencies, set-up and enter the Python environment needed to run Kivy. To install, clone/download the repository. In the autopen directory, run the following script: 

python3 vm_install.py

When prompted to keep dash as the default shell, select No. 

### Installing on bootable Linux

To run Autopen, having Python 3 and pip3 installed, the repository needs to be added and the following dependencies must be installed. 

sudo add-apt-repository ppa:kivy-team/kivy

pip3 install python3-kivy

pip3 install cython==0.23

## Running the Program

Once installed, you can run AutoPen using the following command. The second part of the command (*tee log.txt*) will create a log.txt file. (To append to an existing log.txt file, change this command to be (*tee -a log.txt*) In this file, all of the output from the program will be stored making it much easier to trace back an error. Please refer to this file if the program crashes or something does not install properly. 

python3 AutoPen.py | tee log.txt

## Quick Notes

In order to automate things, autopen uses the [subprocess](https://docs.python.org/3/library/subprocess.html#subprocess.check_output) module.
