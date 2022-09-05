

#Ham tra ve so thu tu cua chu A trong chuoi
def findCharacter(string1):
    locChar=int(string1.find("a"))
    return locChar

#Ham viet hoa ky tu
def upperString(string1):
    #Viet hoa tung ky tu
    if string1!="":
        for i in string1:
            listStr1.append(string1.replace(i, i.upper()))
            #print(string1.replace(i, i.upper()))
    return listStr1
    
#Ham thay the a=@
def repA(string1):
    if string1!="":
        for i in listStr1:
            if findCharacter(i) >= 0:
                listStr1.append(i.replace(i[findCharacter(i)], "@"))
                #print(i.replace(i[findCharacter(i)], "@"))
    return listStr1
    
#Ham thay the a=4
def rep4(string1):    
    if string1!="":
        for i in listStr1:
            if findCharacter(i) >= 0:
                listStr1.append(i.replace(i[findCharacter(i)], "4"))
                #print(i.replace(i[findCharacter(i)], "4"))
    return listStr1

#Ham nhap ngay sinh
def inputDay():
    print("Day: ", end="")
    strDay = str(input())
    print("Month: ", end="")
    strMonth = str(input())
    print("Year: ", end="")
    strYear = str(input())
    listDay=[]
    listDay.append(strDay)
    listDay.append(strMonth)
    listDay.append(strYear)
    return listDay
#Ham nhap chuoi so
def inputNum():
    print("Number: ", end="")
    strNum = str(input())
    listNum=[]
    listNum.append(strNum)
    return listNum
#Ham nhap ky tu dac biet
def speChar():
    print("Special character: ", end="")
    speChar = str(input())
    return speChar
#Nhap chuoi ky tu
def inpChar():
    print("Input string: ", end="")
    string1 = str(input())
    return string1


#--------------------------------------------------------------------------------

#Khai bao bien
listStr1=[]
listStrDay=[]
allList=[]

#Cau hoi dau
print("Basic (Y/N): ", end="")
menu0=str(input())

print("Name file: ", end="")
nameFile=str(input())

#0. Basic
if menu0.upper()=="Y":
    string1 = inpChar();
    tmpNum=inputNum()
    tmpSChar=speChar()
    repA=repA(string1)
    
    for i in upperString(string1): 
        allList.append(i+tmpSChar+tmpNum[0])
        allList.append(tmpNum[0]+tmpSChar+i)
        
        allList.append(tmpSChar+i+tmpNum[0])
        allList.append(tmpSChar+tmpNum[0]+i)
        
        allList.append(i+tmpNum[0]+tmpSChar)
        allList.append(tmpNum[0]+i+tmpSChar)
        
    for i in repA:
        allList.append(i+tmpNum[0])
        allList.append(tmpNum[0]+i)
    
    allList = list(dict.fromkeys(allList))
    for i in allList:
        print(i)
    
    with open(nameFile,'w', encoding = 'utf=8') as file:
        for i in allList:
            file.write(i+"\n")
            check = 1
    if check == 1:
        print("-------------")
        print("Success")
    else:
        print("-------------")
        print("Failue")
        
#2. Co ky tu dac biet, khong replace
elif menu0.upper()=="N":
    string1 = inpChar();
    tmpDay1=inputDay()
    tmpSChar=speChar()
    
    allList.append(string1+tmpDay1[0]+tmpDay1[1])
    allList.append(tmpSChar+string1+tmpDay1[0]+tmpDay1[1])
    allList.append(string1+tmpSChar+tmpDay1[0]+tmpDay1[1])
    allList.append(string1+tmpDay1[0]+tmpDay1[1]+tmpSChar)
    
    allList.append(string1+tmpDay1[2])
    allList.append(tmpSChar+string1+tmpDay1[2])
    allList.append(string1+tmpSChar+tmpDay1[2])
    allList.append(string1+tmpDay1[2]+tmpSChar)
    
    allList.append(string1+tmpDay1[0]+tmpDay1[1]+tmpDay1[2])
    allList.append(tmpSChar+string1+tmpDay1[0]+tmpDay1[1]+tmpDay1[2])
    allList.append(string1+tmpSChar+tmpDay1[0]+tmpDay1[1]+tmpDay1[2])
    allList.append(string1+tmpDay1[0]+tmpDay1[1]+tmpDay1[2]+tmpSChar)
    
    for i in upperString(string1):
        allList.append(i+tmpDay1[2])
        allList.append(i+tmpDay1[0]+tmpDay1[1])
        allList.append(i+tmpDay1[0]+tmpDay1[2])
        allList.append(tmpDay1[2]+i)
        allList.append(tmpDay1[0]+tmpDay1[1]+i)
        allList.append(tmpDay1[0]+tmpDay1[2]+i)
        
        allList.append(i+tmpSChar+tmpDay1[2])
        allList.append(i+tmpSChar+tmpDay1[0]+tmpDay1[1])
        allList.append(i+tmpSChar+tmpDay1[0]+tmpDay1[2])
        allList.append(tmpDay1[2]+tmpSChar+i)
        allList.append(tmpDay1[0]+tmpDay1[1]+tmpSChar+i)
        allList.append(tmpDay1[0]+tmpDay1[2]+tmpSChar+i)
        
        allList.append(tmpSChar+i+tmpDay1[2])
        allList.append(tmpSChar+i+tmpDay1[0]+tmpDay1[1])
        allList.append(tmpSChar+i+tmpDay1[0]+tmpDay1[2])
        allList.append(tmpSChar+tmpDay1[2]+i)
        allList.append(tmpSChar+tmpDay1[0]+tmpDay1[1]+i)
        allList.append(tmpSChar+tmpDay1[0]+tmpDay1[2]+i)
        
        allList.append(i+tmpDay1[2]+tmpSChar)
        allList.append(i+tmpDay1[0]+tmpDay1[1]+tmpSChar)
        allList.append(i+tmpDay1[0]+tmpDay1[2]+tmpSChar)
        allList.append(tmpDay1[2]+i+tmpSChar)
        allList.append(tmpDay1[0]+tmpDay1[1]+i+tmpSChar)
        allList.append(tmpDay1[0]+tmpDay1[2]+i+tmpSChar)
    for i in repA(string1):
        allList.append(i+tmpDay1[2])
        allList.append(i+tmpDay1[0]+tmpDay1[1])
        allList.append(i+tmpDay1[0]+tmpDay1[1]+tmpDay1[2])
        
        allList.append(tmpDay1[2]+i)
        allList.append(tmpDay1[0]+tmpDay1[1]+i)
        allList.append(tmpDay1[0]+tmpDay1[1]+tmpDay1[2]+i)
    
    allList = list(dict.fromkeys(allList))
    for i in allList:
        print(i)
    
    with open(nameFile,'w', encoding = 'utf=8') as file:
        for i in allList:
            file.write(i+"\n")
            check = 1
    if check == 1:
        print("-------------")
        print("Success")
    else:
        print("-------------")
        print("Failue")