
sum=0
while (True):
    number=input(" enter the number :")
    
    if number!="q":
        sum=sum+int(number)
    else:
        break
print(sum)