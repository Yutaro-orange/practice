import string


def change(chararray):
    intarray = [int(index) for index in chararray]
    return intarray

lawer_case = string.ascii_uppercase
charlist = list(lawer_case)

countlist = []


try:

    while(True):

        val = input()
    # Enter values separated by comma: x,y,z
        if val:
            inputlist = list(val)

        else:
            break
except EOFError:
    pass


for char in charlist:
    countlist.append(inputlist.count(char))

downtoplist = sorted(countlist, reverse=True)
maisu = downtoplist[0]


if("*" in inputlist):
    maisu+=1

twocount = downtoplist.count(2)
if(maisu == 4):
    print("FourCard")
elif(maisu == 3):
    print("ThreeCard")
elif(twocount == 2):
    print("TwoPair")
elif(maisu == 2):
    print("OnePair")
else:
    print("NoPair")




