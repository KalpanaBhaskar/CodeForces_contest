t=int(input())
ans =[]
for i in range(t):
    n = int(input())
    arr = input().split()
    arr= [int(i) for i in arr]
    min_val = min(arr)
    ans.append(n - min_val)
for i in ans:
    print(i)