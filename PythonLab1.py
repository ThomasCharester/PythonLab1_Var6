
i = int(input("Enter integer number: "))
a = i % 10 
b =  (int(i % 100 / 10))

while i % 10 > (int(i % 100 / 10)):
    a = i % 10 
    b =  (int(i % 100 / 10))
    i = int(i / 10)
else:
    if i != 0 : print("not ok")
    else : print('ok')
    

