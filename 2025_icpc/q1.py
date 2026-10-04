t =int(input())
ans=[]
for i in range(t):
    s =input()
    s=s.lower()
    vow =""
    consonant =""
    for j in s:
        if j in "aeiou":
            vow+=j
        else:
            consonant+=j
    if len(vow)%2 == 1 and len(consonant)%2==1:
        ans.append("NO")
    elif (vow == "" or vow == vow[::-1]) and (consonant=="" or consonant==consonant[::-1]):
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)

