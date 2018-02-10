#！/usr/bin/env python3
#_*_coding:utf-8_*_
import math
import time
import operator
import win32api
import win32gui
import win32con
from PIL import ImageGrab,Image
from functools import reduce

def image_contrast(img1, img2):

    image1 = Image.open(img1)
    image2 = Image.open(img2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return result

def ready(hld):
    print("模拟器正在运行")
    print("窗口句柄为："+str(hld))
    left,top,right,bottom = win32gui.GetWindowRect(hld)
    if left>0:
        print(left, top)
        print(right, bottom)
        width=right-left
        hight=bottom-top
        print("模拟器宽="+str(width)+" 高="+str(hight))
        wz=[width,hight]
        start(hld)

    else:
        print("无法定位模拟器窗口...")

def start(hld):
    mode=input("1.觉醒 2.御魂 3.退出  :")
    if mode=="1":
        md="jx"
    if mode=="2":
        md="yh"
    if mode=="3":
        exit()
    i=0
    start = "%s\start.jpg"%(md)  # 指定图片路径
    end1 = "%s\end1.jpg"%(md)
    end2 = "%s\end2.jpg"%(md)
    temp = "temp.jpg"
    while True:
        try:
            left,top,right,bottom = win32gui.GetWindowRect(hld)
            img=ImageGrab.grab((left, top, right, bottom))
            img.save('temp.jpg','jpeg')
            result=[]
            result.append(image_contrast(start,temp))
            result.append(image_contrast(end1,temp))
            result.append(image_contrast(end2,temp))
            if(result[0]<=1300.0):
                print("[%s] 点击挑战！*" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                click(hld)
                i = i+1
            if(result[1]<=1300.0):
                print("[%s] 任意位置！" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                click(hld)
            if(result[2]<=1300.0):
                print("[%s] 重新开始" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                click(hld)
            result.clear()
            time.sleep(5)
        except KeyboardInterrupt:
            print("已停止脚本，本次共挑战%d次！" % i)
            exit()

def click(hld):
    left,top,right,bottom = win32gui.GetWindowRect(hld)
    width=right-left
    hight=bottom-top
    wz=[width,hight]
    x=int(wz[0]*0.715)+left
    y=int(wz[1]*0.694)+top
    point=[x,y]
    win32api.SetCursorPos(point)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)


def end():
    print("模拟器未运行")
    print("5秒后退出脚本")
    time.sleep(5)
    exit()

def main():
    label="靠谱天天模拟器 2.5.5"
    hld = win32gui.FindWindow(None, label)
    if hld>0:
        ready(hld)
    else:
        end()

if __name__ == '__main__':
    main()
