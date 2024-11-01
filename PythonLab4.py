def findPairCount(start, item, str):
    count = 0;
    i = start

    while i < len(str):
        if item == str[i]: count += 1
        i += 1
        
    return count

str = input("Enter numbers string: ")

start = 0

myDict = dict()

for item in str:
    if item in myDict:
       start += 1
       continue

    myDict[item] = findPairCount(start,item,str)

for i in myDict:
    print(i, "  " , myDict[i])
