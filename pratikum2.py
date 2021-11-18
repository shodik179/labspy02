a = int(input('masukan nilai a: '))
b = int(input('massukan nilai b: '))
c = int(input('masukan nilai c: '))

maks = 0

print(a,b,c)
if a > b:
    maks = a
else:
    maks = b
if c > maks:
    maks = c
    print('c ')
print("bilangan terbesar: ",maks)