
def CycleNumber(number,data):
    
    avgCount   = 0
    nCountTime = 0

    if number == 'N':
        return avgCount

    lnCount = []
    for idata in data :
        if number == idata :
            lnCount.append(nCountTime)
            nCountTime = 0    

        nCountTime += 1

    avgCount = round(sum(lnCount)/len(lnCount))


    return avgCount


def LastPick(number,data,date,month,year):
    
    strTime = ""
    nLastPick = 0

    if number == 'N':
        return [strTime,nLastPick]

    for idata in data :
        if number == idata :
            strTime = date[nLastPick]+"-"+month[nLastPick]+"-"+ year[nLastPick]
            break

        nLastPick += 1     

    return [strTime,nLastPick]

def PickStat(number,data):
    nCountTime = 0
    nCountTotal = 0

    if number == 'N':
        return [nCountTime,1]

    for idata in data :
        nCountTotal += 1
        if number == idata :
            nCountTime += 1
 
    return [nCountTime,nCountTotal-1]

def SameCount(DatArr1,DatArr2,DatArr3,DatArr4,DatArr5,DatArr6):

    bCount = False

    count = [0,0,0,0,0,0]

    count[0] = [DatArr1,DatArr2,DatArr3,DatArr4,DatArr5,DatArr6].count(DatArr1)

 

    return bCount


def OddOrEven(strFirstPrize):
    
    nCountEven  = 0
    nCountOdd   = 0
    nCountTotal = 0

    for sFirstPrize in strFirstPrize:
        if int(sFirstPrize)%2 == 0 :
            nCountEven += 1 
        else :
            nCountOdd += 1
        nCountTotal += 1

    print("odd :",nCountOdd,"Even :",nCountEven," Total :",nCountTotal)

    return [nCountOdd,nCountEven]


def GroupRange(strFirstPrize):
    groupRange = [0,0,0,0,0,0,0,0,0,0]

    for sFirstPrize in strFirstPrize:
        if 100000 > int(sFirstPrize) >= 0  :
            groupRange[0] += 1
        elif 200000 > int(sFirstPrize) >= 100000  :
            groupRange[1] += 1
        elif 300000 > int(sFirstPrize) >= 200000  :
            groupRange[2] += 1
        elif 400000 > int(sFirstPrize) >= 300000  :
            groupRange[3] += 1
        elif 500000 > int(sFirstPrize) >= 400000  :
            groupRange[4] += 1
        elif 600000 > int(sFirstPrize) >= 500000  :
            groupRange[5] += 1
        elif 700000> int(sFirstPrize) >= 600000  :
            groupRange[6] += 1
        elif 800000 > int(sFirstPrize) >= 700000  :
            groupRange[7] += 1
        elif 900000 > int(sFirstPrize) >= 800000  :
            groupRange[8] += 1
        elif 1000000 > int(sFirstPrize) >= 900000  :
            groupRange[9] += 1

    print(groupRange)

    return groupRange

def SameDigitCount(strFirstPrize):

    nCountSame = [0,0,0,0,0]
    char_set = ["0","1","2","3","4","5","6","7","8","9"]
    num_set = [0,0,0,0,0,0,0,0,0,0]
    nCounter = 0 
    same_set = [0,0,0,0,0,0,0,0,0,0]


    for sFirstPrize in strFirstPrize :
        for _char in char_set :
            for _sFirstPrize in sFirstPrize :
                if _char == _sFirstPrize :
                    nCounter += 1
            num_set[int(_char)] = nCounter
            nCounter = 0
            if num_set [int(_char)] != 1:
                same_set[int(_char)] += num_set[int(_char)]

        if 2 in num_set : nCountSame[0] += 1
        if 3 in num_set : nCountSame[1] += 1
        if 4 in num_set : nCountSame[2] += 1
        if 5 in num_set : nCountSame[3] += 1
        if 6 in num_set : nCountSame[4] += 1

    print(same_set)
 
    return [nCountSame,same_set]