file = open("test.txt", "r", encoding="UTF8")

counter = {}

for lines in file:
    words = lines.split()
    for word in words:
        counter[word] = counter.get(word, 0) + 1

bword = None
bcount = None

for keys , values in counter.items():
    if bcount is None or values > bcount:
        bword = keys
        bcount = values


print(bword , bcount)