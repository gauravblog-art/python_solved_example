# Twenty random cards are placed in a row all face down. 
# A turn consists of taking two adjacent cards where the left one is 
# face up and the right one can be face up or face down and flipping them both. 
# Show that this process must terminate. (with all the cards facing up).


def transform(n):
    for i in range(len(n)-1):
        if n[i] == '1':
            n[i]= '0'
            if n[i+1]=='0':
                n[i+1]='1'
            else:
                n[i+1]='0'
    return n

if __name__== "__main__":
    a=list("01111101110111100")
    print(a)
    while a!=transform(a.copy()):
        a=transform(a.copy())
    print(a)
    

