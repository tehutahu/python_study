#! python3
# strip hand made

import re, sys

def strip_new(text, target):
    strip_regex = re.compile('^(' + target + ')*|(' + target + ')*$')
    print(strip_regex.sub('', text))
    return strip_regex.sub('', text)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage:python strip.py [text] {target}')
        sys.exit()
    elif len(sys.argv) < 3:
        strip_new(sys.argv[1], ' ')
    else:
        strip_new(sys.argv[1], sys.argv[2])
