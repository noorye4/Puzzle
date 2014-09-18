import itertools


li = []
for i in range(144):
    li.append(i)

x = list(itertools.permutations(li, len(li)))

print len(x)