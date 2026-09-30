'''
t =int(input())
for i in range(t):
    n,d = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    
    # res1=[]
    # res2=[]
    # for i in range(n):
    #     if i % 2==0:
    #         res1.append(arr[i])
    #     else:
    #         res2.append(arr[i])
    # res = res1 + res2[::-1]
    # print(res)

    max_diff =0
    sec_max=0
    dif_arr=[]
    for i in range(1,n):
        diff=arr[i]-arr[i-1]
        if diff>=max_diff:
            sec_max = max_diff
            max_diff=diff 
    #print(max_diff,sec_max)           
    if max_diff >d:
        if n%2==1:
            if sec_max<=d:
                print("YES")
                continue
        print("NO")
        continue
    else:
        print("YES")
'''
t = int(input())
ans=[]
for _ in range(t):
    n, d = map(int, input().split())
    arr = sorted(map(int, input().split()))

    bad = 0

    for i in range(1, n):
        if arr[i] - arr[i - 1] > d:
            bad += 1

    #print("YES" if bad <= 1 else "NO")
    if bad<=1:
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)


        
