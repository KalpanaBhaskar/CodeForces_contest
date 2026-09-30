t =int(input())
ans_arr=[]
for i in range(t):
    a,b,m = map(int, input().split())
    cycle_sum = m*(m-1)//2
    if a//m==b//m:
        rem_b=b%m
        rem_a=a%m
        ans =(rem_b*(rem_b+1)//2)-(rem_a*(rem_a+1)//2)
    else:
        rem1 =a%m
        rem1_sum =rem1*(rem1+1)//2
        pref_sum =cycle_sum-rem1_sum    
        a_start =((a//m)+1)*m
        b_end =(b//m)*m    
        cycles=(b_end-a_start)//m
        cycles_sum =cycles*cycle_sum    
        suffix_sum =(b % m)*((b % m)+1)//2    
        ans = pref_sum +cycles_sum +suffix_sum
    ans_arr.append(ans)
for i in ans_arr:
    print(i)