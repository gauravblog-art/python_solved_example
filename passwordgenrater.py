
import string
import random

if __name__== '__main__':
    s1 = string.ascii_lowercase
    # print(s1)
    s2=string.ascii_uppercase

    s3=string.digits

    s4=string.punctuation
    s=[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    # print(s)/
    random.shuffle(s)
    # print(s)

    p=int(input("enter the leng of passoword : "))

    print("".join(s[0:p]))

