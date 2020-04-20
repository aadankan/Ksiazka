from pprint import *

message = 'It was a bright, cold April day and the clocks beat thirteenth'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint(count)