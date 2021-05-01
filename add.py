def change(charhairetu):
    inthairetu = [int(index) for index in charhairetu]
    return inthairetu

def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

array = []
outerarray = []

try:

    while(True):

        val = input()
    # Enter values separated by comma: x,y,z
        if val:
            charlist = val.rstrip().split(' ')

        else:
            break
except EOFError:
    pass

for a in charlist:
    mojilist = list(a)
    array.append(mojilist)


for charlist in array:
    innerarray = []
    for char in charlist:

        if(char == 'A'):
            num = 0
        elif(char == 'B'):
            num = 1
        elif(char == 'C'):
            num = 2
        elif(char == 'D'):
            num = 3
        elif(char == 'E'):
            num = 4
        innerarray.append(num)
    outerarray.append(innerarray)

for numarray in outerarray:
    numarray.reverse()

a = 0
for numlist in outerarray:
    b = 0

    for num in range(len(numlist)):
        a += numlist[num] * (5 **num)
    a += b

changed5num = Base_10_to_n (a,5)

list_5 = list(changed5num)
output=''
for char in list_5:
    if(char == '0'):
        output+= 'A'
    elif(char == '1'):
        output+= 'B'
    elif(char == '2'):
        output+= 'C'
    elif(char == '3'):
        output+= 'D'
    elif(char == '4'):
        output+= 'E'

print(output)