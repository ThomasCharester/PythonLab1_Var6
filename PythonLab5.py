import os

def showMenu(text,*, startWith = 0):
    i = startWith
    while i in range(len(text)):
        print(str(i) + " - " + text[i])
        i += 1
    while 1:
        choice = int(input("Your choice is: "))
        if choice <= len(text) and choice > 0:
            return choice

def showDictionary(dictToShow,*,keyName = '', startAttrFrom = 0, attributes = list(), header = ""):
    if header != "" : print(header)
    for i in dictToShow:
        if not attributes:
            print(keyName + i)
            for attr in dictToShow[i]:
                print(attr, end = '\t')
        else:
            print(keyName + ' ' + i + '\t', end = '\t')
            for attrInd in range(startAttrFrom, len(attributes)):
                print(attributes[attrInd] + ':\t' + str(dictToShow[i][attrInd]),end='\t')
            print(' ')

def makeOrder(*, dicktionary = dict()):
    if dicktionary: showDictionary(dicktionary, keyName='Name', attributes=['Price', 'Count'])

    itemID = input("Enter the item name: ")
    itemCount = int(input("Enter the item count: "))
    return [itemID, itemCount]

def makePrikol(item, checkout,email = 'thomascharester@gmail.com'):
    import smtplib
    from email.mime.text import MIMEText

    sender = "tomascharester@gmail.com"
    receiver = email

    msg = MIMEText("You bought "+ item + " for " + str(checkout) + '$')
    msg['Subject'] = "Purchase in python lab work"
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login("tomascharester@gmail.com", "uycw bykr mwvj peks")
        server.sendmail(sender, receiver, msg.as_string())

email = 'thomascharrester@gmail.com'

mainMenu = ["Free V-Bucks","Price list", "Count list", "All info", "Make order", "Exit"]
dicktionary = {"FreddyPlushe" : [10,35],"BonniePlushe" : [9,30],"ChicaPlushe" : [10,90], "FoxyPlushe" : [11,50] }

checkout = list()
while 1:
    x = showMenu(mainMenu,startWith= 1)
    os.system('cls')

    if x == 1:   showDictionary(dicktionary, keyName='Name', attributes=['Price'])
    elif x == 2: showDictionary(dicktionary, keyName='Name', attributes=['Count'], startAttrFrom=1)
    elif x == 3: showDictionary(dicktionary, keyName='Name', attributes=['Price', 'Count'])
    elif x == 4: 
        order = makeOrder(dicktionary=dicktionary)
        if order[0] in dicktionary: 
            if order[1] <= dicktionary[order[0]][1]:
                print('Thank you! We will send check on your email')
                checkout.append(order[1]*dicktionary[order[0]][0])
                
                makePrikol(order[0], checkout[-1], email)
            else:
                print("Wrong count, try again")
        else:
            print('There are no ' + order[0])
    elif x == 5: break
    elif x == 6: email = input("Enter email")
    input("Enter any value to continue")
    os.system('cls')

print("Thank you!")