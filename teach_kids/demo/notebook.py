import wx

app = wx.App()
win = wx.Frame(None, title="我的记事本")

bkg = wx.Panel(win)
loadBtn = wx.Button(bkg, label="打开")
saveBtn = wx.Button(bkg, label="保存")

filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filename, proportion=1, flag=wx.EXPAND)
hbox.Add(loadBtn,  proportion=0, flag=wx.LEFT, border=5)
hbox.Add(saveBtn,  proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=50)

bkg.SetSizer(vbox)


win.Show()
app.MainLoop()