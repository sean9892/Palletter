import palletter as pal
from PIL import Image
import tkinter as _tk
from time import sleep

def tCode(s):
    return "0"*(2-len(s))+s

def raise_above_all(window): 
    window.attributes('-topmost', 1) 
    window.attributes('-topmost', 0) 

def main():
    cnt=int(input("Pallette >> "))
    p=pal.pallette(50,cnt)
    path=""
    #GetPath
    root = _tk.Tk()
    root.withdraw()
    root.attributes('-topmost', 1)
    root.filename =  _tk.filedialog.askopenfilename(initialdir = "E:/Images",title = "choose your file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    root.attributes('-topmost', 0)
    path=root.filename
    #/GetPath
    img=Image.open(path)
    l=p.abscol(img)
    print(l)
    root.deiconify()
    #Draw Pallette
    root.geometry(str(min(cnt,len(l))*100)+"x100")
    canvas=_tk.Canvas(root, relief="solid", bd=2)
    for x in range(0,min(cnt,len(l))):
        print(x,"th Color Printing..")
        colCode = "#"+tCode(hex(l[x][0])[2:])+tCode(hex(l[x][1])[2:])+tCode(hex(l[x][2])[2:])
        w=100
        polygon=canvas.create_polygon(x*w,0,x*w+w,0,x*w+w,100,x*w,100,outline="black",fill=colCode)
        canvas.pack(fill="both",expand=True)
    #/Draw Pallette
    root.mainloop()
    input()
    root.quit()
main()
