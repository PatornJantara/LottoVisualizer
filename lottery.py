import csv
import random
import math
from tkinter.constants import TRUE
from web_grab_data import WebScrapper
from datetime import date
from datetime import datetime
import os
import time

str_list_month = ["มกราคม","กุมภาพันธ์","มีนาคม","เมษายน","พฤษภาคม","มิถุนายน",
                    "กรกฎาคม","สิงหาคม","กันยายน","ตุลาคม","พฤศจิกายน","ธันวาคม", ]

str_list_year = ["2564","2563","2562","2561","2560","2559","2558","2557","2556","2555",
                "2554","2553","2552","2551","2550","2549","2548","2547","2546","2545",
                "2544","2543","2542","2541","2540","2539"]

dict_month = {'JAN':'1','FEB':'2','MAR':'3','APR':'4','MAY':'5','JUN':'6','JULY':'7','AUG':'8','SEP':'9','OCT':'10','NOV':'11','DEC':'12',}

dict_column = {'DATE':0,'MONTH':1,'YEAR':2,'FIRST PRIZE':3,'1':4,'2':5,
            '3':6,'4':7,'5':8,'6':9}

str_list_digit = ["N","0","1","2","3","4","5","6","7","8","9"]


def UpdateDataBase():
    str_data = ""
    csv_data = ""
    csv_tail = ""
    first_prize = []
    WebData = WebScrapper()
    WebData.check_driver_version()
        

    with open('_LottoFile.csv', newline='') as file:
        reader = csv.reader(file)
        Output = []
        for row in reader:
            Output.append(row[:])


    str_data += Output[1][0] + "/"
    str_data += Output[1][1] + "/"
    str_data += Output[1][2] + "  ถึง  "

    str_data += Output[len(Output)-1][0] + "/"
    str_data += Output[len(Output)-1][1] + "/"
    str_data += Output[len(Output)-1][2] 

    for col in range(1,len(Output)):
        csv_tail += Output[col][0] + ","
        csv_tail += Output[col][1] + ","
        csv_tail += Output[col][2] + ","
        csv_tail += Output[col][3] + "\n"
    
    # collect header 
    csv_data += Output[0][0] +","
    csv_data += Output[0][1] +","
    csv_data += Output[0][2] +","
    csv_data += Output[0][3] +"\n"


    print("ฐานข้อมูล :  "+ str_data)
    
    today = date.today()
    today = ConvertDate(today)

    today = DateToNum(today[2],today[1],today[0])
    dataday = DateToNum(Output[1][0],dict_month[Output[1][1]],Output[1][2])

    DiffDay = today-dataday

    list_day = SearchLottoTime(DiffDay.days,[Output[1][0],dict_month[Output[1][1]],Output[1][2]])
    
    print(list_day)

    if len(list_day) > 0 :



        bUpdate = False

        for next_lottory in list_day :

            bUpdate = TRUE
            NewData = WebData.GetLotteryWeb('https://news.sanook.com/lotto/check/'+next_lottory,'strong',
                {'class':"lotto__number lotto__number--first"})
            first_prize.append(NewData[0])

        if(bUpdate==True):
            WebData.Close()
            os.remove('_LottoFile.csv')

            first_prize = first_prize[::-1]
            list_day = list_day[::-1]

            for sort_lotter in range(0,len(first_prize)):
                if  list_day[sort_lotter][0]=='0':
                    csv_data += str(list_day[sort_lotter][0:2]).replace('0','') + ","
                else:
                    csv_data += str(list_day[sort_lotter][0:2]) + ","
                csv_data += MonthNumtoWord(list_day[sort_lotter]) + ","
                csv_data += list_day[sort_lotter][4:8] + ","
                csv_data += first_prize[sort_lotter]+ "\n"
            
            csv_data += csv_tail
            
            time.sleep(3)
 
            
            print(csv_data)
            WriteFileData(csv_data)



def clean_data(data):

    str_in_data = str(data)
    str_out_clean_data = ""
    str_temp = ""
    int_count = 0

    for str_sub_list_month in str_list_month :
        if str_in_data.find(str_sub_list_month) != -1 :
            str_temp = str_in_data.replace(str_sub_list_month,","+EngThTrans(str_sub_list_month)+",") 
            for str_character in str_temp :
                if str_character != " ":  
                    if int_count >= 2 :
                        int_count += 1

                        if int_count == 6 :
                            str_character = str_character+","
                        elif int_count > 12 :
                            str_character = ""
                                
                    if str_character == ",":
                        int_count += 1
                    
                    str_out_clean_data += str_character

            break

    return str_out_clean_data


def EngThTrans(data):

    str_eng_month = ""

    if str(data) == "มกราคม" :
        str_eng_month = "JAN"
    elif str(data) == "กุมภาพันธ์" :
        str_eng_month = "FEB"
    elif str(data) == "มีนาคม" :
        str_eng_month = "MAR"
    elif str(data) == "เมษายน" :
        str_eng_month = "APR"
    elif str(data) == "พฤษภาคม" :
        str_eng_month = "MAY"
    elif str(data) == "มิถุนายน" :
        str_eng_month = "JUN"
    elif str(data) == "กรกฎาคม" :
        str_eng_month = "JULY"
    elif str(data) == "สิงหาคม" :
        str_eng_month = "AUG"
    elif str(data) == "กันยายน" :
        str_eng_month = "SEP"
    elif str(data) == "ตุลาคม" :
        str_eng_month = "OCT"
    elif str(data) == "พฤศจิกายน" :
        str_eng_month = "NOV"
    elif str(data) == "ธันวาคม" :
        str_eng_month = "DEC"

    return str_eng_month


def RollLottery(digit1,digit2,digit3,digit4,digit5,digit6):

    str_number = ""
    list_number = ["0","1","2","3","4","5","6","7","8","9",]
    digits = [i for i in range(0, 10)]
    
    if digit1 != "N":
        str_number += digit1
    else :
        str_number += random.choice(list_number)

    if digit2 != "N":
        str_number += digit2
    else :
        str_number += random.choice(list_number)
    
    if digit3 != "N":
        str_number += digit3
    else :
        str_number += random.choice(list_number)

    if digit4 != "N":
        str_number += digit4
    else :
        str_number += random.choice(list_number)

    if digit5 != "N":
        str_number += digit5
    else :
        str_number += random.choice(list_number)
    
    if digit6 != "N":
        str_number += digit6
    else :
        str_number += random.choice(list_number)

    WriteRecord(str_number)

    return str_number


def GetData():

    with open('_LottoFile.csv', newline='') as file:
    
        reader = csv.reader(file)

        Output = []
        for row in reader:  
            Output.append(row[:])

    #/// This used to clean data ///    
    #with open('new.txt', 'r', encoding='utf-8') as f:
    #    lines = f.readlines()
    #for i in lines :
    #    print(clean_data(i))

    FirstDigit = []
    SecondDigit = []
    ThirdDigit = []
    FourthDigit = []
    FifthDigit = []
    SixthDigit = []

    FirstPrize = []

    for row_num, rows in enumerate(Output):
 
        FirstPrize.append(str(rows[dict_column['FIRST PRIZE']]))
        FirstDigit.append(str(rows[dict_column['FIRST PRIZE']])[0])
        SecondDigit.append(str(rows[dict_column['FIRST PRIZE']])[1])
        ThirdDigit.append(str(rows[dict_column['FIRST PRIZE']])[2])
        FourthDigit.append(str(rows[dict_column['FIRST PRIZE']])[3])
        FifthDigit.append(str(rows[dict_column['FIRST PRIZE']])[4])
        SixthDigit.append(str(rows[dict_column['FIRST PRIZE']])[5]) 

    Date = []
    Month = []
    Year = []


    for row_num, rows in enumerate(Output):

        Date.append(str(rows[dict_column['DATE']]))
        Month.append(str(rows[dict_column['MONTH']]))
        Year.append(str(rows[dict_column['YEAR']]))
   
    DataReturn = [Date,Month,Year,FirstPrize,FirstDigit,SecondDigit,ThirdDigit,FourthDigit,FifthDigit,SixthDigit]
   
    return  DataReturn


def ConvertDate(Date):
    list_date = []

    str_date = ""
    for sub_str in str(Date):
        if sub_str  == "-":
            list_date.append(str_date) 
            str_date =""
        else :
            if sub_str  != " ":
                str_date += sub_str

    list_date.append(str_date) 
    str_date =""

    list_date[0] = str(int(list_date[0])+543)
    list_date[1] == str(int(list_date[1]))
    list_date[2] = str(int(list_date[2])) 

    return list_date


def DateToNum(dates,month,year):
    dates = int(dates)
    month = int(month)
    year = int(year)-543
 
    day = date(year, month, dates)
 
    return  day

def SearchLottoTime(diffday,DataDayList = []):
    LottoDateList = []
    urlTemp =''

    next = math.floor((diffday)/16)

    print("ฐานข้อมูลล้าหลัง :"+ str(next) + " งวด")

    day = int(DataDayList[0])
    month = int(DataDayList[1])
    year = int(DataDayList[2])

    for nextLotto in range (0,next):

        if day == 1  : 
            if month == 1 :
                urlTemp += '17'
            else:
                urlTemp += '16'
            day = 16
            if month < 10 :
                urlTemp += '0' + str(month)
            
            else:
                 urlTemp += str(month)
                 
            urlTemp += str(year)
 

        elif day == 16 or day == 17 or day == 30:

            if month  == 12 :
                urlTemp += '30'
                urlTemp +=  str(month)
                urlTemp += str(year)
                month = 1
                year += 1
                day = 1

            elif month  == 4 :
                urlTemp += '02'
                urlTemp += '0'+str(month+1)
                urlTemp += str(year)
                month += 1
                day = 1

            elif month <10   :
                urlTemp += '01'
                if month != 9:
                    urlTemp +=  '0'+str(month+1)
                else :
                    urlTemp +=  str(month+1)
                urlTemp += str(year)
                month += 1
                day = 1

            elif month >= 10 and  month  != 12  :
                urlTemp += '01'
                urlTemp += str(month+1)
                urlTemp += str(year)
                month += 1
                day = 1
                
        
        LottoDateList.append(urlTemp)
        urlTemp =''
    
    return LottoDateList
 
def MonthNumtoWord(strMonth):
    MonthWord = ''

    if strMonth[2] == '0' and strMonth[3] == '1':
        MonthWord = 'JAN'
        return MonthWord

    if strMonth[2] == '0' and strMonth[3] == '2':
        MonthWord = 'FEB'
        return MonthWord
    
    if strMonth[2] == '0' and strMonth[3] == '3':
        MonthWord = 'MAR'
        return MonthWord
    
    if strMonth[2] == '0' and strMonth[3] == '4':
        MonthWord = 'APR'
        return MonthWord

    if strMonth[2] == '0' and strMonth[3] == '5':
        MonthWord = 'MAY'
        return MonthWord
    
    if strMonth[2] == '0' and strMonth[3] == '6':
        MonthWord = 'JUN'
        return MonthWord
    
    if strMonth[2] == '0' and strMonth[3] == '7':
        MonthWord = 'JULY'
        return MonthWord

    if strMonth[2] == '0' and strMonth[3] == '8':
        MonthWord = 'AUG'
        return MonthWord
    
    if strMonth[2] == '0' and strMonth[3] == '9':
        MonthWord = 'SEP'
        return MonthWord
    
    if strMonth[2] == '1' and strMonth[3] == '0':
        MonthWord = 'OCT'
        return MonthWord

    if strMonth[2] == '1' and strMonth[3] == '1':
        MonthWord = 'NOV'
        return MonthWord
    
    if strMonth[2] == '1' and strMonth[3] == '2':
        MonthWord = 'DEC'
        return MonthWord

def WriteFileData(data):
    with open('_LottoFile.txt', 'w') as file:  

        file.write(data)
    
    os.rename('_LottoFile.txt','_LottoFile.csv')


def WriteRecord(data):

    if os.path.exists('Roll-record.txt'):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not

    highscore = open('Roll-record.txt',append_write)
    highscore.write( datetime.now().strftime("%d/%m/%Y %H:%M:%S") +'\t'+data+ '\n')
    highscore.close()
