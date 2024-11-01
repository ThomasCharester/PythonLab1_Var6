import random
myList = list()
for i in range(random.randint(5,30)):
    myList.append(random.randint(0,99))

pairs = 0
start = 1
print("Pairs: ")
for item in myList:
    i = start

    while i < len(myList):
        if item == myList[i]:
           pairs += 1
           print(item)
        i += 1

    start += 1

print("Pairs count: " + str(pairs))
print("------\nList: ")

for i in myList:
    print(i)
    