#! python3
# phoneAndEmail.py


import re, pyperclip

def phoneAndEmail():
    # regex for phonenumber
    phone_regex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?     #
        (-|\s|\.)?             # separator
        (\d{3})
        (-|\s|\.)
        (\d{4})
        (\s*(ext|x|ext.)\s*(\d{2,5}))?
        )''', re.VERBOSE)

    # regex for email
    email_regex = re.compile(r'''(
        [a-zA-Z0-9._+%-]+       # user name
        @                       #
        [a-zA-Z0-9.-]+             # domain name
        (\.[a-zA-Z]{2,4})
        )''', re.VERBOSE)

    # search regexs from clipbode
    text = str(pyperclip.paste())

    match = []
    for groups in phone_regex.findall(text):
        phone_num = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phone_num += 'x ' + groups[8]
        match.append(phone_num)

    for groups in email_regex.findall(text):
        match.append(groups[0])

    # copy results to clipbode
    if len(match) > 0:
        pyperclip.copy('\n'.join(match))
        print('\n'.join(match))
    else:
        print('no phone number or email address.')

if __name__ == '__main__':
    phoneAndEmail()
