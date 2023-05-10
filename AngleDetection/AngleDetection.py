import cv2
import math
import numpy as np
#导入图片
path='test.png'
img=cv2.imread(path)
#点击点的位置存储队列
pointsList=[]
#鼠标点击定位绘制函数
def mousePoints(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        #画图
        size=len(pointsList)
        if size!=0 and size%3!=0:
            #这里画线，注意两次画线的起点终点怎么区分
            cv2.line(img,tuple(pointsList[round((size-1)/3)*3]),(x,y),(0,0,255),2)
        cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED)
        pointsList.append([x,y])
        #print(pointsList)
        #print(x,y)
#返回梯度
def gradient(pt1,pt2):
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])
#返回角度
def getAngle(pointsList):
    pt1,pt2,pt3=pointsList[-3:]
    print(pt1,pt2,pt3)
    m1=gradient(pt1,pt2)
    m2=gradient(pt1,pt3)
    angR=math.atan((m2-m1)/(1+m1*m2))
    angD=round(math.degrees(angR))
    print(angD)
    cv2.putText(img,str(angD),(pt1[0]-40,pt1[1]-20),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,255),2)
#刷新图像以显示绘制点
while True:
#当有三的整数点，开始计算角度
    if len(pointsList)%3==0 and len(pointsList)!=0:
        getAngle(pointsList)

    cv2.imshow('Image',img)
    #鼠标点击事件，返回鼠标点击位置的坐标位置
    cv2.setMouseCallback('Image',mousePoints)
    #点击q重置图像和点队列
    if cv2.waitKey(1)&0xFF==ord('q'):
        pointsList=[]
        img=cv2.imread(path)
