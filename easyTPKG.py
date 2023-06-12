#!/usr/bin/python3

import threading
import time
import sys
import os

__author__ = 'TrollSkull'
__version__= 'v1.2'

banner = ('''
                 _____ _____ _____ _____ 
 ___  __ ___ _ _|_   _|  _  |  |  |   __|
| -_||. |_ -| | | | | |   __|    -|  |  |
|___|___|___|_  | |_| |__|  |__|__|_____|
            |___|                        
''')

def banner_message(color, reset):
    print(color + banner + reset)

def error_message(color, reset):
    print(color + 'This tool only works on Termux.')
    print('\nTo see more about this tool, check:')
    print(reset + 'https://github.com/TrollSkull/easyTPKG\n')

if not sys.platform == 'win32':
    if os.system('uname -o') == 'Android':
        os.system('clear')
    else:
        error_message('\033[91m', '\033[0m')
else:
    error_message('\033[91m', '\033[0m')

packages = ['coreutils', 'zip', 'unzip', 'unrar', 'nmap', 'wget', 'openssl', 'openssh',
            'vim', 'php', 'python', 'python2', 'python-dev', 'python3', 'java', 'git',
            'dnsutils', 'hydra', 'macchanger', 'curl', 'perl', 'golang']

def install_packages(package, color, reset):
    print(color + f'\nInstalling {package}...\n' + reset)
    os.system(f'pkg install {package} -y &> /dev/null')
        
if __name__ == '__main__':
    try:
        os.system('clear')
        banner_message('\033[92m', '\033[0m')

        print('\033[92m' + '\n[easyTPKG] ' + '\033[0m' + 'Updating and upgrading packages.\n')
        os.system ('apt update && apt upgrade -y &> /dev/null')

        if not os.path.exists('/data/data/com.termux/files/home/storage'):
            print('\033[92m' + '\n[easyTPKG] ' + '\033[0m' + 'We need storage permission.\n')
            os.system ('termux-setup-storage')

        for package in packages:
            threading.Thread(target = install_packages, args = (package, '\033[0m', '\033[92m')).start()
            time.sleep(5)

    except KeyboardInterrupt:
        sys.exit('[CTRL+C] Detected, exiting.')
