import pythoncom, pyHook
import time
def OnKeyboardEvent(event):
    dirx = '0'
    if event.Message == 256:
        dirx = '1'
    f = open("output.txt","a+")
    f.write(event.Key+","+dirx+","+str(time.time())+"\n")
    f.close()
    return True
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.KeyUp = OnKeyboardEvent
hm.HookKeyboard()
try:
    pythoncom.PumpMessages()
except KeyboardInterrupt:
    pass
