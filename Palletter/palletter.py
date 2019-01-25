"""
Palletter by DevAir
2019/01/22 Dev Start.

(FuncReturnVal : suffix)
Bool  : B
Float : F
Int   : I
Tuple : T
Void  : no suffix
"""
from PIL import Image
class pallette:
    def __init__(self,MDis=50,cnt=5):
        self.setMDis(MDis)
        self.selColor=[]
        self.cnt=cnt
    def __del__(self):
        pass
    
    def setMDis(self,MDis):
        self.MDis=MDis
        
    def imgGetSizeT(self,img):
        return img.size
    
    def colDisF(self,col1,col2):
        r=0
        for x in range(3):
            r+=col1[x]**2+col2[x]**2
        return r**0.5
    
    def insColB(self,col):
        for c in self.selColor:
            if self.colDisF(c,col)<self.MDis:
                return False
        return True
        
    def reSort(self,arr):
        l=[]
        for x in arr:
            cDis=0
            for y in self.selColor:
                cDis+=self.colDisF(x[1],y)
            for y in self.selColor:
                cDis-=100*self.colDisF((x[1][0]-min(x[1]),x[1][1]-min(x[1]),x[1][2]-min(x[1])),(y[0]-min(y),y[1]-min(y),y[2]-min(y)))
            l.append((3000-self.colDisF(x[1],(127,127,127)),cDis,(x[0],x[1])))
        l.sort()
        #l=l[::-1]
        arr=[]
        for x in range(len(l)):
            arr.append(l[x][2])
    
    def abscol(self,img):
        #preset
        print("Ready for Work...")
        wid,hei=self.imgGetSizeT(img)
        self.wid,self.hei=wid,hei
        imgpix=img.load()
        RGBoft={}#Save Frequency here as Dictionary
        
        #Set Colors Frequency
        print("Setting Frequency...")
        for x in range(wid):
            for y in range(hei):
                tup=imgpix[x,y][0:3]
                try:
                    RGBoft[tup]+=1
                except:
                    RGBoft[tup]=1

        print("Color Sorting...")
        #Set oMax,oMin and Add All colors with Frequency
        oMax,oMin=0,wid*hei*2
        cols=[]
        for r in range(256):
            for g in range(256):
                for b in range(256):
                    try:
                        cols.append((RGBoft[(r,g,b)],(255-r,255-g,255-b)))
                        oMax=max(oMax,RGBoft[(r,g,b)])
                        oMin=min(oMin,RGBoft[(r,g,b)])
                    except Exception as ex:
                        #print(ex)
                        pass
        cols.sort()#sort by Frequency
        cols=cols[::-1]#reverse([0] has hightes frequency)

        print("Color Abstracting...")
        while 0<len(cols) and len(self.selColor)<self.cnt:
            nowCol=(255-cols[0][1][0],255-cols[0][1][1],255-cols[0][1][2])
            if self.insColB(nowCol):
                self.selColor.append(nowCol)
                cols.pop(0)
                self.reSort(cols)
            else:
                cols.pop(0)
        print("Complete!")
        return self.selColor
