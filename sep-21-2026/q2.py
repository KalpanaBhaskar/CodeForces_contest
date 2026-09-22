t=int(input())
ans=[]
for i in range(t):
    arr=input().split()
    arr = [int(i) for i in arr]
    score_a = min(abs(arr[0]-arr[1]),abs(arr[0]-arr[1]-arr[2]))
    score_a2=abs(arr[0]-arr[1]+arr[2])
    sol = max(score_a,score_a2)
    ans.append(sol)
for i in ans:
    print(i)
