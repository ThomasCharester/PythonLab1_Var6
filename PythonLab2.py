vowels = 'aeiouyAEIOUY'
consonants = 'bcdfghjklmpqrstvwxzBCDFGHJKLMPQRSTVWXZ'

str = input("Enter text")
vow, cons = 0 , 0
consstr = ''
for s in str:
    if s in vowels: vow += 1
    elif s in consonants: 
        cons += 1 
        consstr += s
else: 
    if vow == cons : print(consstr)
    