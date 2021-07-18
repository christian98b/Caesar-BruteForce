Satz = "LUHDYSXJUJQIJUHYNKDTERUBYN"     #Insert Encrypted Text here




alphabet = 'abcdefghijklmnopqrstuvwxyz'                                         #Create dictionarys
alphabet = alphabet.upper()
alpha = []
for x in alphabet:
    alpha.insert(-1, x)
alpha.insert(0,alpha.pop(-1))
zahlen = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
dictionary = dict(zip(alpha,zahlen))
dictrev = {x : y for (y,x) in dictionary.items()}


Satz = Satz.upper()                                                             #Check if text contains Anything but Letters
Satz = Satz.replace(" ","")
for x in Satz:
    if x.isalpha() == False:
        print("Keine Buchstaben")
        exit(0)

satz = []                                                                       #Convert text to integers
satzasint = []
for x in Satz:
    satz.insert(-1,x)
satz.insert(0,satz.pop(-1))

for x in satz:
    satzasint.insert(-1,dictionary[x])
    
    

count = 1                                                                       #Count up integers
while count < 27:
    satzstring = ""
    i = 0
    while i < len(satzasint):
        satzasint[i] = satzasint[i] + 1
        i+=1 
            
    for x in satzasint:                                                         #Check if numer is greater than 26. in that case x-26
        while x > 26:
            x = x-26
        satzstring = satzstring + dictrev[x]                                    #Create final String
    print(satzstring[-1:] + satzstring[:-1])
    count += 1
