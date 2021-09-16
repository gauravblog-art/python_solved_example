def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
def factorialcoutzero(n):
    fac=fact(n)
    print(fac)
    c=0
    while (fac%10==0):
        c=c+1
        fac/=fac
    return c

if __name__== "__main__":
    n=int(input("enter the number : "))
    a=fact(n)
    b=factorialcoutzero(n)
    print(b)