#count character

import pprint
count = {}

message = input('input statements\n')

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
