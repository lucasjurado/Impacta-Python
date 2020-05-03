mdc = []
mmc = []

n1 = int(input('1º vlr: '))
n2 = int(input('2º vlr: '))

c=1
while True:
   if n1%c == 0 and n2%c == 0:
       mdc.append(c)
   c+=1
   if c == 100:
       break

r=1
while True:
    if r%n1 == 0 and r%n2 == 0:
        mmc.append(r)
    r+=1
    if r == 1000:
        break

print(max(mdc))
print(min(mmc))