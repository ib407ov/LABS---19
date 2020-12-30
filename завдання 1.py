arrey=[]
with open('data.txt') as ff:
    for row in ff:
        numbers = list(map(float, row.split(',')))
        arrey += numbers
print(max(arrey))
