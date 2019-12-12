import wx
import random

def lottery(event):
	who = random.randint(1, 50)
	print("来啊！", who)
	numText.SetLabel(str(who)) 

# 创建应用程序对象
app = wx.App()

# 创建一个窗口
win = wx.Frame(None, title="翻牌子", size=(400, 300))
#win = wx.Frame(None, title="这个问题谁会", size=(400, 300), style=wx.MAXIMIZE_BOX | wx.CAPTION)

#pnl = wx.Panel(win)

numText = wx.StaticText(win, label="Who?", size=(400, 150), pos=(0, 50), style=wx.ALIGN_CENTER)
font = numText.GetFont()
font.PointSize += 60
font = font.Bold()
numText.SetFont(font)

startBtn = wx.Button(win, label="点名", size=(100, 50), pos=(150, 200))

startBtn.Bind(wx.EVT_BUTTON, lottery)

# 设置可见
win.Show()

# 进入应用程序事件主循环
app.MainLoop()

