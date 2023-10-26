b = open('input.txt',)
c = set()
for q in a:
    a = q.split()
    for i in a:
        c.add(i.rstrip('\n'))
b.close()
print(len(c))
