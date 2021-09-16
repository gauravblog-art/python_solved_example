
def matrix(m,n):
    o=[]
    for i in range(m):
        row=[]
        for j in range(n):
            a=int(input("enter the value in matrix :"))
            row.append(a)
        o.append(row) 
    return o 

if __name__== '__main__':
    a=int(input("entter the number :"))
    b=int(input("enter the value : "))

    m=matrix(a,b)
    print(m)  

