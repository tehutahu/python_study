#count character

count = {}

message = input('input statements\n')

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)
