t=int(input())
ans=[]
max_limit=200005
ref = list(range(max_limit))
for i in range(2,int(max_limit**0.5)+1):
    if ref[i]==i:
        for j in range(i*i,max_limit,i):
            if ref[j]==j:
                ref[j]=i
for i in range(t):
    a,b=input().split()
    a=int(a)
    b=int(b)
    arr=input().split()
    arr=[int(i) for i in arr]

    max_val=max(arr)
    # max_limit = max(max_val+1,200005)
    '''
    ref = list(range(max_limit))
    for i in range(2,int(max_limit**0.5)+1):
        if ref[i]==i:
            for j in range(i*i,max_limit,i):
                if ref[j]==j:
                    ref[j]=i
    '''
    dp = [0]*(max_val+1)
    for i in range(1,max_val+1):
        if i<=b:
            dp[i]=0
        else:
            dp[i]=float('inf')
            temp=i
            while temp>1:
                p=ref[temp]
                cost=1+p*dp[i//p]
                if cost<dp[i]:
                    dp[i]=cost
                while temp%p==0:
                    temp//=p
    ops=sum(dp[i] for i in arr)
    ans.append(ops)
for i in ans:
    print(i)
