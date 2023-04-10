# INPUT = "test_input.txt"
INPUT = "input.txt"

with open(INPUT, "r") as f:
    data = f.read().strip()

buffer = []
counter = 0
unique = False
for char in data:
    if unique and len(buffer) == 14:
        break

    counter += 1

    buffer.append(char)
    if len(buffer) > 14 :
        del buffer[0]

    if len(buffer) == len(set(buffer)):
        unique = True
    else:
        unique = False

print(counter)
