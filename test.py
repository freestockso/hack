#-*- coding: utf-8 -*-  ##设置编码方式
import sys,time
reload(sys)
sys.setdefaultencoding('gb2312')
import win32api,win32gui,win32con

def get_child_windows(parent):
    '''
    获得parent的所有子窗口句柄
     返回子窗口句柄列表
     '''
    if not parent:
        return
    hwndChildList = []
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd),  hwndChildList)
    return hwndChildList

def exportDayData():
    """
    [1]解压缩 -Button
    [2]浏览文件 -Button
    [3]检查数据 -Button
    [4]取消 -Button
    [5]000001 -ComboBox
    [6]000001 -Edit
    [7]分割数据 -Button
    [8]读文件完成,股票代码:3846 -Static
    [9]数据类型: -Static
    [10]股票代码: -Static
    [11]D:\dzh365\data\sz\ReportCps_2.DAT -Edit
    [12]日数据 -Edit
    [13]市场类型: -Static
    [14]输出文本 -Button
    [15]SZ -Edit
    [16] -SysListView32
    [17] -SysHeader32
    :return:
    """
    label='DzhTest'
    hld = win32gui.FindWindow(None, label)
    count=0
    if hld > 0:
        l = get_child_windows(hld)
        c = win32gui.SendMessage(l[4], win32con.CB_GETCOUNT, 0, 0)#获取股票数量
        stocklist=[]
        for k in range(0, c):
            bb=' '*10
            win32gui.SendMessage(l[4], win32con.CB_GETLBTEXT, k, bb)
            stocklist.append(bb.strip())
    for s in stocklist:
        win32gui.SendMessage(l[5], win32con.WM_SETTEXT, None, s)
        win32gui.SendMessage(l[0], win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
        win32gui.SendMessage(l[0], win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)
        while True:
            time.sleep(0.05)
            buffer=' '*100
            win32gui.SendMessage(l[7], win32con.WM_GETTEXT, 100, buffer)
            if buffer.strip().startswith(u'解压缩'):
                time.sleep(0.05)
                break
        win32gui.SendMessage(l[13], win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
        win32gui.SendMessage(l[13], win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)
        while True:
            time.sleep(0.05)
            buffer=' '*100
            win32gui.SendMessage(l[7], win32con.WM_GETTEXT, 100, buffer)
            if buffer.strip().startswith(u'写数据完成'):
                time.sleep(0.05)
                break
        print 'export'+s
        count+=1
        # if count>5:
        #     break

exportDayData()
    # dlg = win32gui.FindWindowEx(hld, None, 'Edit', None)#获取hld下第一个为edit控件的句柄
    # len = win32gui.SendMessage(dlg, win32con.WM_GETTEXTLENGTH) + 1
    # btnhld2 = win32gui.FindWindowEx(hld, None, 'Button', None)
    # btnhld = win32gui.FindWindowEx(hld, btnhld2, 'Button', None)
    # win32gui.SendMessage(btnhld, win32con.WM_GETTEXT, len, buffer)  # 读取文本
    # len = win32gui.SendMessage(btnhld, win32con.WM_GETTEXTLENGTH) + 1
    # win32gui.PostMessage(btnhld, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
    #
    # win32gui.PostMessage(btnhld, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)


# count=0
# for i in l:
#     buffer = ' ' * 150
#     len = win32gui.SendMessage(i, win32con.WM_GETTEXTLENGTH) + 1
#     win32gui.SendMessage(i, win32con.WM_GETTEXT, len, buffer)
    # 获取某个句柄的类名和标题
    # title = win32gui.GetWindowText(i)
    # clsname = win32gui.GetClassName(i)
    # buffer=buffer.strip()
    # if i==199510:
        # c=win32gui.SendMessage(i,win32con.CB_GETCOUNT ,0,0)
        # bbb=' '*20000
        # win32gui.SendMessage(i,win32con.WM_GETTEXT,len,bbb)
        # print bbb
        # for k in range(0,c):
        #     bb=' '*10
        #     win32gui.SendMessage(i, win32con.CB_GETLBTEXT   , k,bb)
            # print bb
        # print(buffer)
    # if title==u'检查数据':
    #     print('??')
    #     win32gui.PostMessage(i, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
    #     win32gui.PostMessage(i, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)
    # print len
    # count+=1

