vowels = 'aeiouyAEIOUY'
consonants = 'bcdfghjklmpqrstvwxzBCDFGHJKLMPQRSTVWXZ'

stin = input("Enter text")
vow, cons= 0 , 0
consstin = ''
for s in stin:
    if s in vowels: vow += 1
    elif s in consonants: 
        cons += 1 
        if s not in consstin:
            consstin += s

else: 
    if vow == cons : print(consstin)

print("Vowels count: ", vow, " Consonants count: ",cons, " Word count: ", len(stin.split(' ')))
    