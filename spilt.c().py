import sys

for line in sys.stdin:
    a=line.split()[0]
    l=len(a)
    print(l)
    n = 0

for i in range(l):
    if line[i]=='o':
            n += 1

    if n%2== 1:
        print(len(a)-1)
    else:
        print(len(a))



