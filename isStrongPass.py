#! python3
#

import sys, re

strong_regex1 = re.compile(r'[a-z]{8,}')
strong_regex2 = re.compile(r'[A-Z]+')
strong_regex3 = re.compile(r'\d+')

def isStrongPass(password):
    if strong_regex1.search(password) != None:
        if strong_regex2.search(password) != None:
            if strong_regex3.search(password) != None:
                print('strong password')
            else:
                print('week password')
        else:
            print('week password')
    else:
        print('week password')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage:python isStrongPass.py [password]')
        sys.exit()
    else:
        isStrongPass(sys.argv[1])
