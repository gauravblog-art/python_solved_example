sum=0
n=1536
copy_n=n
order=len(str(n))
while n>0:
    digit=n%10
    sum+=digit**order
    n=n//10
if sum==copy_n:
    print("True")
else:
    print("flase")