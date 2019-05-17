import hashlib
import os
import wx

class NotBookMainFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(400,300))

        self.tb = self.CreateToolBar()
        self.contrl = wx.TextCtrl(self,style=wx.TE_MULTILINE)

        #Alt

        # 创建一个状态bar，在window的最下端
        self.sbar = self.CreateStatusBar()
        # 创建菜单栏
        menuB  = self.createMenuBar()
        # set menuBar of app
        self.SetMenuBar(menuB)
        acceltbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('Q'), self.selectA.GetId())])
        self.SetAcceleratorTable(acceltbl)

        #frame show
        self.Show(True)

    def createMenuBar(self):
        #Menu

        fileM = wx.Menu()
        newF = fileM.Append(wx.NewId(),"新建(N)\tCtrl+N","打开一个已存在的文件.")
        fmitem = fileM.Append(wx.NewId(),"打开(O)\tCtrl+O","打开一个已存在的文件.")
        save = fileM.Append(wx.NewId(),  "保存(S)\tCtrl+S","保存当前的文件.")
        toSave = fileM.Append(wx.NewId(),"另存为(A)..","保存当前的文件.")
        fileM.AppendSeparator()
        fileM.Append(wx.NewId(),"页面设置(U)..","设置页面格式.")
        printL = fileM.Append(wx.NewId(),"打印(P)\tCtrl+P","打印页面.")
        fileM.AppendSeparator()
        qit = fileM.Append(wx.NewId(),"退出(X)","关闭所有打开的文件.")


        self.Bind(wx.EVT_MENU, self.OnNewFile, newF)
        self.Bind(wx.EVT_MENU, self.OnOpen, fmitem)
        self.Bind(wx.EVT_MENU, self.OnSave, save)
        self.Bind(wx.EVT_MENU, self.OnQuit, qit)


        #编辑
        editM = wx.Menu()
        editM.Append(wx.NewId(),"撤消(U)\tCtrl+Z","撤销最后的操作.")
        editM.AppendSeparator()
        editM.Append(wx.NewId(),"剪切(U)\tCtrl+X","剪切.")
        editM.Append(wx.NewId(),"复制(T)\tCtrl+C","复制.")
        editM.Append(wx.NewId(),"粘贴(C)\tCtrl+V","粘贴.")
        editM.Append(wx.NewId(),"删除(P)\tDel","删除.")
        editM.AppendSeparator()
        editM.Append(wx.NewId(),"查找(F)\tCtrl+F","查找.")
        editM.Append(wx.NewId(),"查找下一个(N)\tF3","查找下一个.")
        editM.Append(wx.NewId(),"删除(P)\tDel","删除.")
        editM.Append(wx.NewId(),"替换(R)\tCtrl+H","替换.")
        editM.Append(wx.NewId(),"转到(G)\tCtrl+G","转到.")
        editM.AppendSeparator()
        self.selectA = editM.Append(wx.NewId(),"全选(A)\tCtrl+A","全选.")

        self.Bind(wx.EVT_MENU, self.OnSelectAll, self.selectA)

        editM.Append(wx.NewId(),"时间/日期(D)\tF5","时间.")
        #格式[O]
        posM = wx.Menu()
        self.autoCutoverLine = self.newline = posM.Append(wx.NewId(),"自动换行(W)","自动换行.",kind=wx.ITEM_CHECK)

        self.Bind(wx.EVT_MENU, self.autoCutoverL, self.autoCutoverLine)

        self.showToolStatus = 0;
        posM.Append(wx.NewId(),"字体(F)..","设置字体.")
        #查看[V]
        viewM = wx.Menu()
        viewM.Append(wx.NewId(),"状态栏","状态栏.")
        self.tool=viewM.Append(wx.NewId(),"工具栏","工具栏",kind=wx.ITEM_CHECK)
        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.tool)
        #帮助[H]
        helpM = wx.Menu()
        helpM.Append(wx.NewId(),"查看帮助(H)","查看帮助.")
        about = helpM.Append(wx.NewId(),"关于记事本(A)","关于记事本.")
        self.Bind(wx.EVT_MENU, self.OnAbout, about)
        #create a menuBar
        menuB = wx.MenuBar()
        # append a menu
        menuB.Append(fileM,"文件(F)")
        menuB.Append(editM,"编辑(E)")
        menuB.Append(posM,"格式[O]")
        menuB.Append(viewM,"查看[V]")
        menuB.Append(helpM,"帮助[H]")
        return menuB

    def autoCutoverL(self,event):
        print("hell")
        #设置字体颜色
        #self.control.SetForegroundColour("#F0FFF0")
        self.control.SetStyle(-1, -1, wx.TextAttr("wx.TE_WORDWRAP"))

    def OnSelectAll(self, event):
            self.control.SelectAll()

    def OnKeyDown(self,event):
        #按键时相应代码
        # Alt + F
        key = event.GetKeyCode();
        if key == ord('f'):
            self.fileM.Show()
        else:
            self.control.AppendText(chr(key))

    #是否显示工具栏
    def ToggleToolBar(self,event):
        self.showToolStatus+=1;
        #if self.newline.IsChecked():
        if self.showToolStatus % 2 == 1:
            print(1111)
            self.control.SetInsertionPoint(50)
            self.tb.Show()
        else:
            print(2222)
            self.tb.Hide()


    #新建文件
    def OnNewFile(self,event):
        if self.control.IsEmpty() != True:
            dlg = wx.MessageDialog(self, "是否将更改保存到无标题?","记事本",wx.YES_NO | wx.ICON_QUESTION | wx.CANCEL)
            retCode = dlg.ShowModal()
            if retCode == wx.ID_YES:
                # 保存
                self.OnSave(event)
                # 保存完后，创建新文件
                self.control.SetValue("")
            elif retCode == wx.ID_NO:
                # 清空
                self.control.SetValue("")
            else:
                # 取消
                dlg.Close();

            dlg.Destroy()

    #保存
    def OnSave(self,event):
        #判断是否有内容
        if self.control.IsEmpty():
            return;
        self.dirname=''
        """ wx.FD_OPEN    
            wx.FD_SAVE    
            wx.FD_OVERWRITE_PROMPT
            wx.FD_MULTIPLE    
            wx.FD_CHANGE_DIR """
        dlg = wx.FileDialog(self,"choose a file",self.dirname,"","*.*",wx.FD_SAVE)

        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'w')
            f.write(self.control.GetValue());
            f.close()
        dlg.Destroy()
        # 重新设置记事本的Title
        self.Title  = self.filename + " - 记事本"

    #打开选择文件的dialog
    def OnOpen(self,event):
        print(self.control.GetValue())
        self.dirname=''
        self.dirname=''
        """ wx.FD_OPEN    
            wx.FD_SAVE    
            wx.FD_OVERWRITE_PROMPT
            wx.FD_MULTIPLE    
            wx.FD_CHANGE_DIR """
        dlg = wx.FileDialog(self,"choose a file",self.dirname,"","*.*",wx.FD_CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()
        self.control.SetFocus()
        wx.StaticText(self.sbar, label=self.filename + ","+ str(self.control.GetNumberOfLines()) + " 行",pos=(0,1))

    # 退出
    def OnQuit(self,event):
        self.Close()

    # 关于
    def OnAbout(self,event):
        dlg = wx.MessageDialog(self, "hello,baby","title is a baby",wx.OK)
        dlg.ShowModal()
        self.control.SelectAll();
        dlg.Destroy()

    def OnHello(self, event):
        pass

    #创建按钮
    def createButtonBar(self, panel, yPos = 10):
            xPos = 0
            for eachLabel, eachHandler in self.buttonData():
                    pos = (xPos, yPos)
                    button = self.buildOneButton(panel, eachLabel,eachHandler, pos)
                    xPos += button.GetSize().width

    def buildOneButton(self, parent, label, handler, pos=(0,0)):
        button = wx.Button(parent, -1, label, pos)
        self.Bind(wx.EVT_BUTTON, handler, button)
        return button

    #get md5
    @staticmethod
    def GetMd5(content):

        return hashlib.new("md5", content).hexdigest()

if __name__=="__main__":
    app = wx.App(False)
    frame = NotBookMainFrame(None,"无标题 - 记事本")
    app.MainLoop()
