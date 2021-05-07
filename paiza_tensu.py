import itertools



def change(chararray):
    intarray = [int(index) for index in chararray]
    return intarray
output = []
outerarray = []
array = []
try:

    while(True):

        val = input()
    # Enter values separated by comma: x,y,z
        if val:
            array.append(int(val))


        else:
            break
except EOFError:
    pass


questioncount = array.pop(0)




for num in range(len(array)+1):
    per_list = itertools.combinations(array, num)
    outerarray.append(per_list)

for array in outerarray:
    for num in array:
        print(len(num))
        pattern = 0
        for a in num:
            pattern+=a
        output.append(pattern)


for array in outerarray:
    for num in array:
        tensu = sum(num)
        output.append(tensu)

output = set(output)
output = sorted(output,reverse = False)

print(len(output))
for score in output:
    print(score)


