def findPairCount(start, item, str):
    count = 0;
    i = start

    while i < len(str):
        if item == str[i]: count += 1
        i += 1
        
    start += 1
    return count

str = input("Enter numbers string: ")

start = 1

myDict = { str[0] : findPairCount(start,str[0],str) + 1}

for item in str:
    if item in myDict:
       start += 1
       continue

    myDict[item] = findPairCount(start,item,str) + 1

for i in myDict:
    print(i + "  " + myDict[i])
