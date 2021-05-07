import itertools
from math import factorial
def change(chararray):
    intarray = [int(index) for index in chararray]
    return intarray

def split_list(l, n):

    for idx in range(0, len(l), n):
        yield l[idx:idx + n]


output = []
array = []
itemlist = []
try:

    while(True):

        val = input()
    # Enter values separated by comma: x,y,z
        if val:
            inputlist = change(val.rstrip().split(' '))

        else:
            break
except EOFError:
    pass

wakemae = inputlist[0]
value = 2*wakemae
seiyaku = inputlist[1]

#アイテムリストを作成
for num in range(value):
    itemlist.append(num+1)

#組み合わせを作成

a = factorial(n) / factorial(r) / factorial(n - r)
pairs = list(itertools.combinations(itemlist,wakemae))
length = int(len(pairs)/2)

#Aの分け前とBの分け前に分割
pattern  = list(split_list(pairs,length))

A = pattern[0]
B =list(reversed(pattern[1]))


output = 0


for num in range(len(A)):
    sum = 0
    for count in range(wakemae):
        discription = 0
        discription = A[num][count]-B[num][count]
        if(discription<0):
            discription = discription*-1
        sum+=discription

    if(sum<=seiyaku):
        output+=1
output*=2


print(output)





