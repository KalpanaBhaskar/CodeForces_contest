t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    s=input()
    if s[0]=='1':
        ans.append(s.count('0'))
        continue
    total_z = s.count('0')
    one_pref = 0
    zero_suf = total_z-1
    min_op = one_pref+zero_suf
    for i in range(1,n):
        if s[i]=='1':
            one_pref+=1
        else:
            zero_suf-=1
        cur_op = one_pref+zero_suf
        min_op=min(min_op,cur_op)
    ans.append(min_op)
    
for i in ans:
    print(i)