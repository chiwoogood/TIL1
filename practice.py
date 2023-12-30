n = int(input())

lst = [0,n-1]

for i in range(n):
    for j in range(n-1-i,0,-1):
        print(' ',end="")
    
    if i in lst:
        for k in range((i+1)*2-1):  #1,3,5,7,9
            print("*",end='')
            
    else:
        print('*',end="")
        for k in range(2*i-1):
            print(' ',end="")
        print('*')