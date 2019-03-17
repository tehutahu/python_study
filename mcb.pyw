#! python3
# multi clip board

import sys, pyperclip
import shelve

# keyword
keywords = ['save', 'list']

usage = r'''Usage: python mcb.pyw [command] [key]
            [command]: 'save' or 'list'
            [key]: the key chained with clipboard'''

def mcb(command):
    # restore to clipboard
    if len(command) < 2:
        shelve_mcb = shelve.open('mcb')
        if command[0] in list(shelve_mcb.keys()):
            pyperclip.copy(shelve_mcb[command[0]])
            print('Copy the \'{}\' to clipboard'.format(command[0]))
        else:
            print('Key \'{}\' is not found'.format(command[0]))
        shelve_mcb.close()
    # save to list from clipboard
    elif command[0].lower() == keywords[0]:
        shelve_mcb = shelve.open('mcb')
        shelve_mcb[command[1]] = pyperclip.paste()
        shelve_mcb.close
        print('Save to list from clipboard')
    # display list
    elif command[0].lower() == keywords[1]:
        shelve_mcb = shelve.open('mcb')
        pyperclip.copy('\n'.join(list(shelve_mcb.keys())))
        for key, value in list(shelve_mcb.items()):
            print('key: {}, value: {}'.format(key, value))
        shelve_mcb.close
    else:
        print(usage)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(usage)
    elif sys.argv[1].lower() == keywords[0]:
        mcb([keywords[0], sys.argv[2]])
    elif sys.argv[1].lower() == keywords[1]:
        mcb([keywords[1], ''])
    else:
        mcb([sys.argv[1]])
