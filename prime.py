n=16
count=0
for i in range(2,n):        # i = 1 2 3 4 5 6 7 
    if n % i==0:
        count+=1   # count = count + 1
if count==0:
    print("prime")
else:
    print("not prime")

    


