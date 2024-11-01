def findPairCount(item, listPairs,*,start = 0):
    count = 0;
    i = start

    while i < len(listPairs):
        if item == listPairs[i]: count += 1
        i += 1
        
    return count

import random
myList = list()
for i in range(random.randint(5,30)):
    myList.append(random.randint(0,99))

chosens = list()

for item in myList:
    if findPairCount(item, myList) == 1:
        chosens.append(item)

chosens.reverse()
cortage = tuple(chosens)

print('List: ',myList)
print('Cortage: ',cortage)
