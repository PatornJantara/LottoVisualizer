from tkinter.font import BOLD
from lottery import UpdateDataBase,RollLottery,GetData
from tkinter import *
from PIL import ImageTk
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from lottery_prob import CycleNumber, PickStat , LastPick ,OddOrEven,GroupRange,SameDigitCount
from lottery import str_list_digit,dict_column
import os
import requests

import time


class LotteryDrawer:
    
        def __init__(self):
                self.LotteryData = GetData()
                self.WinDlg = Tk()
                self.WinDlg.title("ฐานข้อมูล  :"
                                +self.LotteryData[dict_column['DATE']][1] + "/"
                                +self.LotteryData[dict_column['MONTH']][1] +"/"
                                +self.LotteryData[dict_column['YEAR']][1] + "  -  "
                                +self.LotteryData[dict_column['DATE']]
                                        [len(self.LotteryData[dict_column['DATE']])-1] + "/"
                                +self.LotteryData[dict_column['MONTH']]
                                        [len(self.LotteryData[dict_column['MONTH']])-1] +"/"
                                +self.LotteryData[dict_column['YEAR']]
                                        [len(self.LotteryData[dict_column['YEAR']])-1])
                self.Mode = False
                self.StatClick = False

                

                self.ManageDlg("main")


        def ManageDlg (self,str_name):
                if str_name == "main":
                        self.Win_w = 600
                        self.Win_h = 500
                
                        self.WinDlg.geometry(str(self.Win_w)+"x"+str(self.Win_h))

                        self.WinDlg.minsize(self.Win_w, self.Win_h)
                        self.WinDlg.maxsize(self.Win_w, self.Win_h)
                
                        self.MainWindow("main")
                
                if str_name == "sub":
                        self.Win_w2 = 1200
                        self.Win_h2 = 300
                
                        self.WinDlg2.geometry(str(self.Win_w2)+"x"+str(self.Win_h2))

                        self.WinDlg2.minsize(self.Win_w2, self.Win_h2)
                        self.WinDlg2.maxsize(self.Win_w2, self.Win_h2)
                
                        self.MainWindow("sub")
 

        def MainWindow(self,str_name):


                if str_name == "main":
                        text = Label(self.WinDlg, text="☺ LUCKY LOTTERY ☻" , font=("Helvetica", 32))
                        text.place(x = self.Win_w*0.1 ,y = self.Win_h*0.05)

                        text2 = Label(self.WinDlg, text="$$$ PICK YOUR LUCKY NUMBER $$$",font=("Helvetica", 14))    
                        text2.place(x = self.Win_w*0.2 ,y = self.Win_h*0.2)
                      

                        RollButton = Button(self.WinDlg,text =" หมุนรางวัล ",bg="gold",
                                font=("Ayuthaya", 22),command = self.RollLotteryDlg)
                        RollButton.place(x = self.Win_w*0.4 ,y = self.Win_h*0.3 )

                        UpdateButton = Button(self.WinDlg,text =" อัพเดตฐานข้อมูล ",
                                font=("Ayuthaya", 18),command = self.UpdateDataBaseDlg)
                        UpdateButton.place(x = self.Win_w*0.01 ,y = self.Win_h*0.9 )
                        
                        StatButton = Button(self.WinDlg,text =" แสดงสถิติ ",
                                font=("Ayuthaya", 18),command = self.StatWindow)
                        StatButton.place(x = self.Win_w*0.4 ,y = self.Win_h*0.9 )

                        GraphButton = Button(self.WinDlg,text =" แสดงกราฟ ",
                                font=("Ayuthaya", 18),command = self.ShowProp)
                        GraphButton.place(x = self.Win_w*0.8 ,y = self.Win_h*0.9 )

                        
                        self.Variable1 = StringVar(self.WinDlg)
                        self.Variable1.set(str_list_digit[0])
                        MenuBar1 = OptionMenu(self.WinDlg, self.Variable1, *str_list_digit)
                        MenuBar1.config(width= 5)
                        MenuBar1.grid(column=1, row=1)
                        MenuBar1.pack()
                        MenuBar1.place(x = self.Win_w*0.05 ,y = self.Win_h*0.5 )

                        self.Variable2 = StringVar(self.WinDlg)
                        self.Variable2.set(str_list_digit[0])
                        MenuBar2 = OptionMenu(self.WinDlg, self.Variable2, *str_list_digit)
                        MenuBar2.config(width= 5)
                        MenuBar2.grid(column=1, row=1)
                        MenuBar2.pack()
                        MenuBar2.place(x = self.Win_w*0.2 ,y = self.Win_h*0.5 )

                        self.Variable3 = StringVar(self.WinDlg)
                        self.Variable3.set(str_list_digit[0])
                        MenuBar3 = OptionMenu(self.WinDlg, self.Variable3, *str_list_digit)
                        MenuBar3.config(width= 5)
                        MenuBar3.grid(column=1, row=1)
                        MenuBar3.pack()
                        MenuBar3.place(x = self.Win_w*0.35 ,y = self.Win_h*0.5 )

                        self.Variable4 = StringVar(self.WinDlg)
                        self.Variable4.set(str_list_digit[0])
                        MenuBar4 = OptionMenu(self.WinDlg, self.Variable4, *str_list_digit)
                        MenuBar4.config(width= 5)
                        MenuBar4.grid(column=1, row=1)
                        MenuBar4.pack()
                        MenuBar4.place(x = self.Win_w*0.5 ,y = self.Win_h*0.5 )

                        self.Variable5 = StringVar(self.WinDlg)
                        self.Variable5.set(str_list_digit[0])
                        MenuBar5 = OptionMenu(self.WinDlg, self.Variable5, *str_list_digit)
                        MenuBar5.config(width= 5)
                        MenuBar5.grid(column=1, row=1)
                        MenuBar5.pack()
                        MenuBar5.place(x = self.Win_w*0.65 ,y = self.Win_h*0.5 )

                        self.Variable6 = StringVar(self.WinDlg)
                        self.Variable6.set(str_list_digit[0])
                        MenuBar6 = OptionMenu(self.WinDlg, self.Variable6, *str_list_digit)
                        MenuBar6.config(width= 5)
                        MenuBar6.grid(column=1, row=1)
                        MenuBar6.pack()
                        MenuBar6.place(x = self.Win_w*0.80 ,y = self.Win_h*0.5 )

                        self.str_graph = ["OddEven","Range","SameCount","SameDigit"]

                        self.graph = StringVar(self.WinDlg)
                        self.graph.set(self.str_graph[0])
                        MenuBar7 = OptionMenu(self.WinDlg, self.graph, *self.str_graph)
                        MenuBar7.config(width= 10)
                        MenuBar7.grid(column=1, row=1)
                        MenuBar7.pack()
                        MenuBar7.place(x = self.Win_w*0.8 ,y = self.Win_h*0.8 )


        
                        self.WinDlg.mainloop()
                
                if str_name == "sub":

                        self.str_last_pick   = ["","","","","",""]
                        self.str_count       = ["","","","","",""]
                        self.str_stat_pick   = ["","","","","",""]


                        #if self.StatClick ==True :
                        #        self.StatLabel.after(0, self.StatLabel.destroy)


                        self.str_last_pick[0] = LastPick(self.Variable1.get(),
                                self.LotteryData[dict_column['1']],
                                self.LotteryData[dict_column['DATE']],
                                self.LotteryData[dict_column['MONTH']],
                                self.LotteryData[dict_column['YEAR']])
                        self.str_count[0] = CycleNumber(self.Variable1.get(),
                                self.LotteryData[dict_column['1']])
                        self.str_stat_pick[0] = PickStat(self.Variable1.get(),
                                self.LotteryData[dict_column['1']])

                        
                        self.str_last_pick[1] = LastPick(self.Variable2.get(),
                                self.LotteryData[dict_column['2']],
                                self.LotteryData[dict_column['DATE']],
                                self.LotteryData[dict_column['MONTH']],
                                self.LotteryData[dict_column['YEAR']])
                        self.str_count[1] = CycleNumber(self.Variable2.get(),
                                self.LotteryData[dict_column['2']])
                        self.str_stat_pick[1] = PickStat(self.Variable2.get(),
                                self.LotteryData[dict_column['2']])


                        self.str_last_pick[2] = LastPick(self.Variable3.get(),
                                self.LotteryData[dict_column['3']],
                                self.LotteryData[dict_column['DATE']],
                                self.LotteryData[dict_column['MONTH']],
                                self.LotteryData[dict_column['YEAR']])
                        self.str_count[2] = CycleNumber(self.Variable3.get(),
                                self.LotteryData[dict_column['3']])
                        self.str_stat_pick[2] = PickStat(self.Variable3.get(),
                                self.LotteryData[dict_column['3']])

                        
                        self.str_last_pick[3] = LastPick(self.Variable4.get(),
                                self.LotteryData[dict_column['4']],
                                self.LotteryData[dict_column['DATE']],
                                self.LotteryData[dict_column['MONTH']],
                                self.LotteryData[dict_column['YEAR']])
                        self.str_count[3] = CycleNumber(self.Variable4.get(),
                                self.LotteryData[dict_column['4']])
                        self.str_stat_pick[3] = PickStat(self.Variable4.get(),
                                self.LotteryData[dict_column['4']])


                        self.str_last_pick[4] = LastPick(self.Variable5.get(),
                                self.LotteryData[dict_column['5']],
                                self.LotteryData[dict_column['DATE']],
                                self.LotteryData[dict_column['MONTH']],
                                self.LotteryData[dict_column['YEAR']])
                        self.str_count[4] = CycleNumber(self.Variable5.get(),
                                self.LotteryData[dict_column['5']])
                        self.str_stat_pick[4] = PickStat(self.Variable5.get(),
                                self.LotteryData[dict_column['5']])  


                        self.str_last_pick[5] = LastPick(self.Variable6.get(),
                                self.LotteryData[dict_column['6']],
                                self.LotteryData[dict_column['DATE']],
                                self.LotteryData[dict_column['MONTH']],
                                self.LotteryData[dict_column['YEAR']])
                        self.str_count[5] = CycleNumber(self.Variable6.get(),
                                self.LotteryData[dict_column['6']])
                        self.str_stat_pick[5] = PickStat(self.Variable6.get(),
                                self.LotteryData[dict_column['6']])   
                
        
        def RollLotteryDlg(self):
                
                self.StrFirstPrize = RollLottery(self.Variable1.get(),
                self.Variable2.get(),
                self.Variable3.get(),
                self.Variable4.get(),
                self.Variable5.get(),
                self.Variable6.get())

                self.output = Label(self.WinDlg, text=str(self.StrFirstPrize),font=("Helvetica",48,"bold"))    
                self.output.place(x = self.Win_w*0.325 ,y = self.Win_h*0.65)



        def StatWindow(self):
      
                self.WinDlg2 = Tk()
                self.WinDlg2.title("หน้าต่างแสดงสถิติ")
                self.ManageDlg("sub")

                StatDigitLabel = Label(self.WinDlg2,text="หลักที่ : ",font=("Helvetica", 16))
                StatNumberLabel = Label(self.WinDlg2,text="หมายเลข : ",font=("Helvetica", 16))
                StatLastLabel = Label(self.WinDlg2,text="ออกรางวัลครั้งล่าสุด (งวดย้อนหลัง) : ",font=("Helvetica", 16))
                StatPickLabel = Label(self.WinDlg2,text="สถิติการออกรางวัล ( % )  : ",      font=("Helvetica", 16))
                StatCyclekLabel = Label(self.WinDlg2,text="รอบการออกรางวัลเฉลี่ย (งวด)  : ",font=("Helvetica", 16))      
 

                StatDigit1Label = Label(self.WinDlg2,text="1",font=("Helvetica", 16))
                StatDigit2Label = Label(self.WinDlg2,text="2",font=("Helvetica", 16))
                StatDigit3Label = Label(self.WinDlg2,text="3",font=("Helvetica", 16))
                StatDigit4Label = Label(self.WinDlg2,text="4",font=("Helvetica", 16))
                StatDigit5Label = Label(self.WinDlg2,text="5",font=("Helvetica", 16))
                StatDigit6Label = Label(self.WinDlg2,text="6",font=("Helvetica", 16))
                
                StatDigitLabel.place(x = self.Win_w2*0.02 ,y = self.Win_h2*0.02)
                StatDigit1Label.place(x = self.Win_w2*0.22 ,y = self.Win_h2*0.02)
                StatDigit2Label.place(x = self.Win_w2*0.35 ,y = self.Win_h2*0.02)
                StatDigit3Label.place(x = self.Win_w2*0.48 ,y = self.Win_h2*0.02)
                StatDigit4Label.place(x = self.Win_w2*0.61 ,y = self.Win_h2*0.02)
                StatDigit5Label.place(x = self.Win_w2*0.74 ,y = self.Win_h2*0.02)
                StatDigit6Label.place(x = self.Win_w2*0.87 ,y = self.Win_h2*0.02)

                StatNumberLabel.place(x = self.Win_w2*0.02 ,y = self.Win_h2*0.2)
                StatLastLabel.place(x = self.Win_w2*0.02 ,y = self.Win_h2*0.4)
                StatPickLabel.place(x = self.Win_w2*0.02 ,y = self.Win_h2*0.6)
                StatCyclekLabel.place(x = self.Win_w2*0.02 ,y = self.Win_h2*0.8)
                

                self.Number1 = Label(self.WinDlg2,
                        text   = str(self.Variable1.get()),
                        font=("Helvetica", 28,"bold"))

                self.StatLastLabel1 = Label(self.WinDlg2,
                        text   = str(self.str_last_pick[0][0]) + "  (" + str(self.str_last_pick[0][1]) +")",
                        font=("Helvetica", 12))
                self.StatPickLabel1 = Label(self.WinDlg2,
                        text   = str(self.str_stat_pick[0][0]) + "  / " + str(self.str_stat_pick[0][1]) +"  ("
                        +str(round(self.str_stat_pick[0][0]*100/self.str_stat_pick[0][1],2))  +"  )",
                        font=("Helvetica", 12))
                self.StatCyclekLabel1 = Label(self.WinDlg2,
                        text   = str(self.str_count[0]),
                        font=("Helvetica", 12))

                
                self.Number2 = Label(self.WinDlg2,
                        text   = str(self.Variable2.get()),
                        font=("Helvetica", 28,"bold"))

                self.StatLastLabel2 = Label(self.WinDlg2,
                        text   = str(self.str_last_pick[1][0]) + "  (" + str(self.str_last_pick[1][1]) +")",
                        font=("Helvetica", 12))
                self.StatPickLabel2 = Label(self.WinDlg2,
                        text   = str(self.str_stat_pick[1][0]) + "  / " + str(self.str_stat_pick[1][1]) +"  ("
                        +str(round(self.str_stat_pick[1][0]*100/self.str_stat_pick[1][1],2))  +"  )",
                        font=("Helvetica", 12))
                self.StatCyclekLabel2 = Label(self.WinDlg2,
                        text   = str(self.str_count[1]),
                        font=("Helvetica", 12))


                self.Number3 = Label(self.WinDlg2,
                        text   = str(self.Variable3.get()),
                        font=("Helvetica", 28,"bold"))

                self.StatLastLabel3 = Label(self.WinDlg2,
                        text   = str(self.str_last_pick[2][0]) + "  (" + str(self.str_last_pick[2][1]) +")",
                        font=("Helvetica", 12))
                self.StatPickLabel3 = Label(self.WinDlg2,
                        text   = str(self.str_stat_pick[2][0]) + "  / " + str(self.str_stat_pick[2][1]) +"  ("
                        +str(round(self.str_stat_pick[2][0]*100/self.str_stat_pick[2][1],2))  +"  )",
                        font=("Helvetica", 12))
                self.StatCyclekLabel3 = Label(self.WinDlg2,
                        text   = str(self.str_count[2]),
                        font=("Helvetica", 12))

                
                self.Number4 = Label(self.WinDlg2,
                        text   = str(self.Variable4.get()),
                        font=("Helvetica", 28,"bold"))
                self.StatLastLabel4 = Label(self.WinDlg2,
                        text   = str(self.str_last_pick[3][0]) + "  (" + str(self.str_last_pick[3][1]) +")",
                        font=("Helvetica", 12))
                self.StatPickLabel4 = Label(self.WinDlg2,
                        text   = str(self.str_stat_pick[3][0]) + "  / " + str(self.str_stat_pick[3][1]) +"  ("
                        +str(round(self.str_stat_pick[3][0]*100/self.str_stat_pick[3][1],2))  +"  )",
                        font=("Helvetica", 12))
                self.StatCyclekLabel4 = Label(self.WinDlg2,
                        text   = str(self.str_count[3]),
                        font=("Helvetica", 12))


                self.Number5 = Label(self.WinDlg2,
                        text   = str(self.Variable5.get()),
                        font=("Helvetica", 28,"bold"))
                self.StatLastLabel5 = Label(self.WinDlg2,
                        text   = str(self.str_last_pick[4][0]) + "  (" + str(self.str_last_pick[4][1]) +")",
                        font=("Helvetica", 12))
                self.StatPickLabel5 = Label(self.WinDlg2,
                        text   = str(self.str_stat_pick[4][0]) + "  / " + str(self.str_stat_pick[4][1]) +"  ("
                        +str(round(self.str_stat_pick[4][0]*100/self.str_stat_pick[4][1],2))  +"  )",
                        font=("Helvetica", 12))
                self.StatCyclekLabel5 = Label(self.WinDlg2,
                        text   = str(self.str_count[4]),
                        font=("Helvetica", 12))

                self.Number6 = Label(self.WinDlg2,
                        text   = str(self.Variable6.get()),
                        font=("Helvetica", 28,"bold"))
                self.StatLastLabel6 = Label(self.WinDlg2,
                        text   = str(self.str_last_pick[5][0]) + "  (" + str(self.str_last_pick[5][1]) +")",
                        font=("Helvetica", 12))
                self.StatPickLabel6 = Label(self.WinDlg2,
                        text   = str(self.str_stat_pick[5][0]) + "  / " + str(self.str_stat_pick[5][1]) +"  ("
                        +str(round(self.str_stat_pick[5][0]*100/self.str_stat_pick[5][1],2))  +"  )",
                        font=("Helvetica", 12))
                self.StatCyclekLabel6 = Label(self.WinDlg2,
                        text   = str(self.str_count[5]),
                        font=("Helvetica", 12))
                
                self.Number1.place(x = self.Win_w2*0.22 ,y = self.Win_h2*0.2)
                self.StatLastLabel1.place(x = self.Win_w2*0.22 ,y = self.Win_h2*0.4)
                self.StatPickLabel1.place(x = self.Win_w2*0.22 ,y = self.Win_h2*0.6)
                self.StatCyclekLabel1.place(x = self.Win_w2*0.22 ,y = self.Win_h2*0.8)

                self.Number2.place(x = self.Win_w2*0.35 ,y = self.Win_h2*0.2)
                self.StatLastLabel2.place(x = self.Win_w2*0.35 ,y = self.Win_h2*0.4)
                self.StatPickLabel2.place(x = self.Win_w2*0.35 ,y = self.Win_h2*0.6)
                self.StatCyclekLabel2.place(x = self.Win_w2*0.35 ,y = self.Win_h2*0.8)

                self.Number3.place(x = self.Win_w2*0.48 ,y = self.Win_h2*0.2)
                self.StatLastLabel3.place(x = self.Win_w2*0.48 ,y = self.Win_h2*0.4)
                self.StatPickLabel3.place(x = self.Win_w2*0.48 ,y = self.Win_h2*0.6)
                self.StatCyclekLabel3.place(x = self.Win_w2*0.48 ,y = self.Win_h2*0.8)

                self.Number4.place(x = self.Win_w2*0.61 ,y = self.Win_h2*0.2)
                self.StatLastLabel4.place(x = self.Win_w2*0.61 ,y = self.Win_h2*0.4)
                self.StatPickLabel4.place(x = self.Win_w2*0.61 ,y = self.Win_h2*0.6)
                self.StatCyclekLabel4.place(x = self.Win_w2*0.61 ,y = self.Win_h2*0.8)

                self.Number5.place(x = self.Win_w2*0.74 ,y = self.Win_h2*0.2)
                self.StatLastLabel5.place(x = self.Win_w2*0.74 ,y = self.Win_h2*0.4)
                self.StatPickLabel5.place(x = self.Win_w2*0.74 ,y = self.Win_h2*0.6)
                self.StatCyclekLabel5.place(x = self.Win_w2*0.74 ,y = self.Win_h2*0.8)


                self.Number6.place(x = self.Win_w2*0.87 ,y = self.Win_h2*0.2)
                self.StatLastLabel6.place(x = self.Win_w2*0.87 ,y = self.Win_h2*0.4)
                self.StatPickLabel6.place(x = self.Win_w2*0.87 ,y = self.Win_h2*0.6)
                self.StatCyclekLabel6.place(x = self.Win_w2*0.87 ,y = self.Win_h2*0.8)

                self.StatPickLabel =True

                self.WinDlg2.mainloop()   

       
        def UpdateDataBaseDlg(self):
                UpdateDataBase()            
                time.sleep(1)
                self.LotteryData = GetData()


        
        def ShowProp(self):

                FirstPrize = self.LotteryData[dict_column['FIRST PRIZE']]            
                FirstPrize = FirstPrize[1:len(FirstPrize)]

                PlotOddEven = OddOrEven(FirstPrize)
                PlotGroupRange = GroupRange(FirstPrize)
                PlotSameDigitCount = SameDigitCount(FirstPrize)

                select = self.graph.get()

                if select == self.str_graph[0]:
                        fig = plt.figure(figsize = (10, 5))
                        
                        plt.bar(["Odd","Even"],  PlotOddEven, color ='maroon',
                                width = 0.4)

                        plt.bar(["Odd","Even"],
                                PlotOddEven, color ='maroon',
                                width = 0.4)

                        for i in range(len(["Odd","Even"])):
                                plt.text(i,PlotOddEven[i],PlotOddEven[i])

                        plt.show()

                elif select == self.str_graph[1]:
                        fig = plt.figure(figsize = (10, 5))
                        
                        x_axis = ["0-100K","100K-200K","200K-300K","300K-400K",
                                "400K-500K","500K-600K","600K-700K","700K-800K","800K-900K","900K-1000K"]
                        
                        plt.bar(x_axis,
                                PlotGroupRange, color ='maroon',
                                width = 0.4)

                        for i in range(len(x_axis)):
                                plt.text(i,PlotGroupRange[i],PlotGroupRange[i])


                        plt.show()
                        
                elif select == self.str_graph[2]:
                        fig = plt.figure(figsize = (10, 5))
                        
                        x_axis = ["2","3","4","5","6"]
                        
                        plt.bar(x_axis,
                                PlotSameDigitCount[0], color ='maroon',
                                width = 0.4)

                        for i in range(len(x_axis)):
                                plt.text(i,PlotSameDigitCount[0][i],PlotSameDigitCount[0][i])

                        plt.xlabel("Times")

                        plt.show()

                elif select == self.str_graph[3]:
                        fig = plt.figure(figsize = (10, 5))
                        
                        x_axis = ["0","1","2","3","4","5","6","7","8","9"]
                        
                        plt.bar(x_axis,
                                PlotSameDigitCount[1], color ='maroon',
                                width = 0.4)

                        for i in range(len(x_axis)):
                                plt.text(i,PlotSameDigitCount[1][i],PlotSameDigitCount[1][i])

                        plt.xlabel("Times")

                        plt.show()
                        
                return None

        
        
        def MainRoutine(self):
                self.WinDlg.mainloop()



Lottery = LotteryDrawer()



