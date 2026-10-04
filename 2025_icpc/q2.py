t = int(input())
ans=[]

for i in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    cur=0
    #cont = -1
    if k==0:
        ans.append(1)
        break
    # for j in range(n):
    j=0
    while j<n-1 :
        if arr[j]==arr[j+1]:
            #k=j+1
            while j<n and arr[j] == arr[j+1] :
                j+=1
            #print("j : ",j)
        else:
            cur+=1
            j+=1
    if arr[n-1]!=arr[n-2]:
        cur+=1
    if cur>1:
        ans.append(cur)
    else:
        ans.append(1)
for i in ans:
    print(i)
    
            
        
            




