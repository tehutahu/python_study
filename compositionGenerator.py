# python3
# 作文ジェネレータ

import re, os, sys

# Usage
usage = r'''Usage: python compositionGenerator.py <file>'''

# compiler
adj_regex = re.compile(r'ADJECTIVE.*?')
noun_regex = re.compile(r'NOUN.*?')
adv_regex = re.compile(r'ADVERBE.*?')
ver_regex = re.compile(r'VERB.*?')

regex_list = [adj_regex, noun_regex, adv_regex, ver_regex]

def compositionGenerator(path):
    # adjust path
    if os.path.abspath(path):
        path = os.path.basename(path)
    new_path = re.sub(r'\.', '_repl.', path)

    # read
    with open(path) as f:
        text = f.read()

    # replace
    for i in range(len(regex_list)):
        repl = input('Enter {}:\n'.format(['an adjective', 'a noun', 'an adverb', 'a verb'][i]))
        text = regex_list[i].sub(repl, text)
    print('new text\n\n{}'.format(text))

    # write
    with open(new_path, 'w') as f:
        f.write(text)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(usage)
    else:
        compositionGenerator(sys.argv[1])
