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

### Installing on bootable Linux

To run Autopen, having Python 3 and pip3 installed, the following dependencies must be installed. 

pip3 install python3-kivy

pip3 install cython==0.23

## Running the Program

python3 AutoPen.py 

*README is still being updated*
