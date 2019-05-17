import wx

import math
global number1
global number2
global status
app = wx.App()
def jiafa(event):
    global number1
    global number2
    global status
    number1=input.GetValue()
    input.Clear()
    status=1
def jianfa(event):
    global number1
    global number2
    global status
    number1=input.GetValue()
    input.Clear()
    status=2
def chengfa(event):
    global number1
    global number2
    global status
    number1=input.GetValue()
    input.Clear()
    status=3
def chufa(event):
    global number1
    global number2
    global status
    number1=input.GetValue()
    input.Clear()
    status=4
def chengfang(event):
    global number1
    global number2
    global status
    number1=input.GetValue()
    input.Clear()
    status=5
def kaifang(event):
    global number1
    global number2
    global status
    number1=input.GetValue()
    status=6
def zhengxian(event):
    global number1
    global number2
    global status
    number1=input.GetValue()
    status=7
def yuxian(event):
    global number1
    global number2
    global status
    number1=input.GetValue()
    status=8
def reset(event):
    global number1
    global number2
    global status
    input.Clear()
    result.Clear()
    status=0
    number1=0
    number2=0
def caculate(event):
    global number1
    global number2
    global status
    number1=float(number1)
    number2=input.GetValue()
    number2=float(number2)
    if status==0:
        pass
    if status==1:
        re=number2+number1
        re=str(re)
        result.SetValue(re)
    if status==2:
        re=number1-number2
        re = str(re)
        result.SetValue(re)
    if status==3:
        re=number1*number2
        re = str(re)
        result.SetValue(re)
    if status==4:
        re=number1/number2
        re = str(re)
        result.SetValue(re)
    if status==5:
        re=number1**number2
        re = str(re)
        result.SetValue(re)
    if status==6:
        re=number1**(1/2)
        re = str(re)
        result.SetValue(re)
    if status==7:
        re=math.sin(number1)
        re = str(re)
        result.SetValue(re)
    if status==8:
        re=math.cos(number1)
        re = str(re)
        result.SetValue(re)

frame = wx.Frame(None,title="caculator",pos=(500,200),size=(500,400))
input = wx.TextCtrl(frame,pos=(5,5),size=(350,24))
run_button = wx.Button(frame,label = "计算",pos = (370,5),size = (50,24))
run_button.Bind(wx.EVT_BUTTON,caculate)

result= wx.TextCtrl(frame,pos=(5,30),size=(350,24))

reset_button = wx.Button(frame,label = "重置",pos = (370,30),size = (50,24))
reset_button.Bind(wx.EVT_BUTTON,reset)

jiafa_button=wx.Button(frame,label="+",pos=(5,60),size=(100,60))
jiafa_button.Bind(wx.EVT_BUTTON,jiafa)

jianfa_button=wx.Button(frame,label="-",pos=(125,60),size=(100,60))
jianfa_button.Bind(wx.EVT_BUTTON,jianfa)

chengfa_button=wx.Button(frame,label="*",pos=(245,60),size=(100,60))
chengfa_button.Bind(wx.EVT_BUTTON,chengfa)

chufa_button=wx.Button(frame,label="/",pos=(365,60),size=(100,60))
chufa_button.Bind(wx.EVT_BUTTON,chufa)

chengfang_button=wx.Button(frame,label="^",pos=(5,160),size=(100,60))
chengfang_button.Bind(wx.EVT_BUTTON,chengfang)

kaifang_button=wx.Button(frame,label="^1/2",pos=(125,160),size=(100,60))
kaifang_button.Bind(wx.EVT_BUTTON,kaifang)

zhengxian_button=wx.Button(frame,label="sin",pos=(245,160),size=(100,60))
zhengxian_button.Bind(wx.EVT_BUTTON, zhengxian)

yuxian_button=wx.Button(frame, label="cos",pos=(365,160),size=(100,60))
yuxian_button.Bind(wx.EVT_BUTTON, yuxian)

frame.Show()
app.MainLoop()