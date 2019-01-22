import palletter as pal
from PIL import Image
def main():
    p=pal.pallette()
    path="C:\\Users\\user\\Desktop\\test.png"
    #GetPath
    
    #/GetPath
    img=Image.open(path)
    l=p.abscol(img)
    print(l)
main()
