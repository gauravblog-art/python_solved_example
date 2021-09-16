SECURE = (('s', '$'), ('and', '&'), 
            ('a', '@'), ('o', '0'), ('i', '1'),
            ('I', '|'),('u','10'))
def pc(p):
    for a,b in SECURE:
        p=p.replace(a,b)
    return p
if __name__=="__main__":
    s=input("enter the password : ")
    a=pc(s)
    print(a)