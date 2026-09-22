t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    arr=input().split()
    arr=[int(i) for i in arr]
    max_len=0
    cur_len=0
    s =set()
    for i in range(n):
        c = arr[i]-(i+1)
        s.add(c)
    ref =sorted(list(s))
    for i in range(len(ref)):
        if i==0 or ref[i]==ref[i-1]+1:
            cur_len+=1
        else:
            max_len=max(cur_len,max_len)
            cur_len=1
    max_len=max(cur_len,max_len)
    ans.append(max_len)

for i in ans:
    print(i)
