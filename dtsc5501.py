lis = [1,2,3,4,5,6,7,8,9,10,11]
i=0
while (i < len(lis)):
    if(lis[i]%2==0):
        lis[i]=(lis[i]*lis[i])
    i+=1 
    
print(lis) 