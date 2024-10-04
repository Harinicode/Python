class NotSquareMatrixError(Exception):
    def __init__(self,s):
        #print(s)
        self.s=s
        super().__init__(self.s)                    #the string is passed to exception class's init or can also be sent to str



r=int(input("Row: " ))
c=int(input("Col: "))
l=[]

for i in range(r):
    print (f"Enter values for row:{i+1}")
    l2=[]
    for j in range(c):
        l2.append(int(input()))
    l.append(l2)
s=0                #lower triagular
usum=0
try:
    if r==c:
    #sum of lower  triangular matrix
        print("Lower Triangular matrix\n")
        for i in range(r):                                          
            for j in range(c):
                if i!=j and i>j:
                    print(l[i][j],end=' ')          #displaying the lower triangular matrix
                    s+=l[i][j]
                elif i!=j and i<j:
                    usum+=l[i][j]                       #upper triagular
            print() 
        print(f'\nSum of Lower Triangular matrix :{s}\nSum of Lower Triangular matrix :{usum}')
    else:
        try:
            raise NotSquareMatrixError("IndexError:Given Matrix is not a square Matrix\n")

         #   raise IndexError
       # except IndexError as e:
        #   print(type(e),"IndexError:Given Matrix is not a square Matrix",sep="\n")
        
        except NotSquareMatrixError as e:
            print(e)
finally:
    print(f"THE GIVEN MATRIX:{l}")
