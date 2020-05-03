r = int(input())
n = int(input())
s = 0

for c in range(1,n+1,r):
    s += c

print('A somatoria da PA eh: {}'.format(s))