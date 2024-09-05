def findPairCount(item, listPairs,*,start = 0):
    count = 0;
    i = start

    while i < len(listPairs):
        if item == listPairs[i]: count += 1
        i += 1
        
    start += 1
    return count

import random
myList = list()
for i in range(random.randint(5,30)):
    myList.append(random.randint(0,99))

chosens = list()

for item in myList:
    if findPairCount(item) == 0:
        chosens.append(item)

cortage = tuple(chosens)

print(cortage)
