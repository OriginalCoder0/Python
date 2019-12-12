import wx

app = wx.App()
win = wx.Frame(None, title="翻牌子", size=(400, 300))

numText = wx.StaticText(win, label="Who?", size=(400, 150), pos=(0, 50), style=wx.ALIGN_CENTER)

font = numText.GetFont()
font.PointSize += 60
font = font.Bold()
numText.SetFont(font)

startBtn = wx.Button(win, label="点名", size=(100, 50), pos=(150, 200))


win.Show()
app.MainLoop()
