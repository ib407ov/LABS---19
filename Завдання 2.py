arrey=[]
with open('data2.txt') as ff:
    for row in ff:
        numbers = list(map(float, row.split(',')))
        arrey += numbers
print(arrey)

r = 0
for i in arrey:
    if i % 2 == 0:
        r += 1
print('К-мть парних чисел',r)

# with open('NP.dat', 'w') as ff:
