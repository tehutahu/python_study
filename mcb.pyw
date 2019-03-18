#! python3
# multi clip board

import sys, pyperclip
import shelve

# keyword
keywords = ['save', 'list', 'delete']

usage = r'''Usage: python mcb.pyw [command] [key]
            [command]: 'save' or 'list'
            [key]: the key chained with clipboard
            [delete] delete the key and values'''

def mcb(command):
    mcb_shelve = shelve.open('mcb')

    # restore to clipboard
    if len(command) < 2:
        if command[0] in list(mcb_shelve.keys()):
            pyperclip.copy(mcb_shelve[command[0]])
            print('Copy the \'{}\' to clipboard'.format(command[0]))
        else:
            print('Key \'{}\' is not found'.format(command[0]))

    # save to list from clipboard
    elif command[0].lower() == keywords[0]:
        mcb_shelve[command[1]] = pyperclip.paste()
        print('Save to list from clipboard')
    # display list
    elif command[0].lower() == keywords[1]:
        pyperclip.copy('\n'.join(list(mcb_shelve.keys())))
        for key, value in list(mcb_shelve.items()):
            print('key: {}, value: {}'.format(key, value))
        # delete the key and value
    elif command[0].lower() == keywords[2]:
        if command[1].lower() == 'all':
            for key in mcb_shelve:
                del mcb_shelve[key]
        else:
            del mcb_shelve[command[1]]
    # default
    else:
        print(usage)

    mcb_shelve.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(usage)
    elif sys.argv[1].lower() == keywords[0]:
        mcb([keywords[0], sys.argv[2]])
    elif sys.argv[1].lower() == keywords[1]:
        mcb([keywords[1], ''])
    elif sys.argv[1].lower() == keywords[2]:
        mcb([keywords[2], sys.argv[2]])
    else:
        mcb([sys.argv[1]])
