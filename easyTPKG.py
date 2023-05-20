#!/usr/bin/python3

import time
import sys
import os

__author__ = 'TrollSkull'
__version__= 'v1.1'

banner = ('''
                 _____ _____ _____ _____ 
 ___  __ ___ _ _|_   _|  _  |  |  |   __|
| -_||. |_ -| | | | | |   __|    -|  |  |
|___|___|___|_  | |_| |__|  |__|__|_____|
            |___|                        
''')

def banner_message(color, reset):
    print(color + banner + reset)

def error_message():
    print('This tool only works on Termux.')
    print('\nTo see more about this tool, check:')
    print('https://github.com/TrollSkull/easyTPKG')

if not sys.platform == 'win32':
    if os.system('uname -o') == 'Android':
        os.system('clear')
    else:
        error_message()
else:
    error_message()

packages = ['coreutils', 'zip', 'unzip', 'unrar', 'nmap', 'wget', 'openssl', 'openssh',
            'vim', 'php', 'python', 'python2', 'python-dev', 'python3', 'java', 'git',
            'dnsutils', 'hydra', 'macchanger', 'curl', 'perl', 'golang']

def install_packages(delay, color, reset):
    for package in packages:

        print(color + f'\nInstalling {package}...\n' + reset)
        os.system(f'pkg install {package} -y &> /dev/null')

        time.sleep(delay)

if __name__ == '__main__':
    try:
        banner_message('\033[92m', '\033[0m')

        print('\n[easyTPKG] Updating and upgrading packages.\n')
        os.system ('apt update && apt upgrade -y')

        if not os.path.exists('/data/data/com.termux/files/home/storage'):
            print('\n[easyTPKG] We need storage permission.\n')
            os.system ('termux-setup-storage')

        install_packages(delay = 1,
                         reset = '\033[0m',
                         color = '\033[92m')

    except KeyboardInterrupt:
        sys.exit('[CTRL+C] Detected, exiting.')
