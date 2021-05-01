import string

newhairetu = []
lawer_case = string.ascii_lowercase

#hairetu = []
try:

    while(True):

        val = input()
    # Enter values separated by comma: x,y,z
        if val:
            mojilist = list(val)
        else:
            break
except EOFError:
    pass
if(not(mojilist.count(' ') ==0)):
    mojilist.remove(' ')

for moji in mojilist:
    for lawer in lawer_case:
        if(moji ==lawer):
            newhairetu.append(lawer_case.index(moji)+1)
            break
print(newhairetu)

while not (len(newhairetu) == 1):
    innerhairetu = []
    for num in range(len(newhairetu)-1):
        innerhairetu.append(newhairetu[num] + newhairetu[num + 1])

    newhairetu = innerhairetu

    for num in range(len(newhairetu)):
        if(newhairetu[num] >101):
            newhairetu[num] = newhairetu[num] -101

print(newhairetu[0])





