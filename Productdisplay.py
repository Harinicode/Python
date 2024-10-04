class A:
    def __init__(self,name="",prc=0.0,dp=0):
        self.name=name
        self.prc=prc
        self.dp=dp
    def calcDA(self):
        return self.dp*self.prc/100
    def calcNP(self):
        return self.prc-self.calcDA()
print("PRODUCTS\n1 Hammer\n2 cutting plier\n3 screw driver")
n=int(input("enter the product no.:"))
if(n==1): #implement with while
    p=A("Hammer",120,20)
    print("PRODUCT DATA:\nName:{:s}\nPrice:{:.2f}\nDiscount:{:d}%\nDiscount amount:{:.2f}\nDiscount price:{:.2f}".format(p.name,p.prc,p.dp,p.calcDA(),p.calcNP()))
elif(n==2):
    p=A("Cutting plier",100,15)
    print("PRODUCT DATA:\nName:{:s}\nPrice:{:.2f}\nDiscount:{:d}%\nDiscount amount:{:.2f}\nDiscount price:{:.2f}".format(p.name,p.prc,p.dp,p.calcDA(),p.calcNP()))
elif(n==3):
    p=A("Screw Driver",75,17)
    print("PRODUCT DATA:\nName:{:s}\nPrice:{:.2f}\nDiscount:{:d}%\nDiscount amount:{:.2f}\nDiscount price:{:.2f}".format(p.name,p.prc,p.dp,p.calcDA(),p.calcNP()))        
        
    
                                                                                                                    
