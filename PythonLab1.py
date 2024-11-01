
i = int(input("Enter integer number: "))
a = i % 10 
b =  (int(i % 100 / 10))

while i % 10 < (int(i % 100 / 10)):
    i = int(i / 10)
else:
    i = int(i / 10)
    if i != 0 : print("not ok")
    else : print('ok')
    

