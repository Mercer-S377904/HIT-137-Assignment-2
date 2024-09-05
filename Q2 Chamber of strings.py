string = "RedSumis321049232Hit137SoftwareNow1Python2codes3are4fun"
numberstring = ""
letterstring = ""
evennumbers = ""
evenASCII = ""
upperCase = ""
upperASCII = ""

#seperate into letters and numbers
for i in string:
    if i.isalpha():
        letterstring += i
    elif i.isdigit():
        numberstring += i
    else:
        pass
    
print("Letters: ", letterstring)
print("Numbers:", numberstring)

#Seperate even numbers
for i in numberstring:
    if int(i) %2 == 0:
        evennumbers += (i + ',')
    else:
        pass
print("Even: ", evennumbers)

#Convert to string ascii value 
for i in evennumbers:
    evenOrdValue = str(ord(i)) 
    evenASCII += (evenOrdValue + ',')
print("Even ASCII: ", evenASCII)

#Seperate uppercase letters
for i in letterstring:
    if i.isupper():
        upperCase += i
    else:
        pass
print("Uppercase: ", upperCase)

#Convert to ascii value
for i in upperCase:
    upperOrdValue = str(ord(i))
    upperASCII += (upperOrdValue + ',')
print("Upper ASCII: ", upperASCII)
