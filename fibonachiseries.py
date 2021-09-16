def fiborec(n):
    if n==0 or n==1:
        return n
    else:
        return fiborec(n-1)+fiborec(n-2)


def fiboat(n):
    prnum=0
    currentnum=1
    for i in range(1,n):
        prprenum=prnum
        prnum=currentnum
        currentnum=prnum+prprenum

    return currentnum

if __name__== '__main__':
    n=int(input("enter the number : "))
    a=fiborec(n)
    print(a)
    b=fiboat(n)
    print(b)