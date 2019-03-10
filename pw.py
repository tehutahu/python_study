#! python3
# pw.py password manager

PASSWORDS = {'email': 'qwerty', 'blog': 'password'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account name]')
    print('copy the password to clipbode')
    sys.exit()

account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS.get(account, 'no'))
    print('copy the password to clipbode ')
else:
    print(account + ' is not found')
