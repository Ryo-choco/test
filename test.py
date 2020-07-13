lis = []

while 1:
    b = input().split(":")
    b[0] = int(b[0])    
    if(len(b) == 1):
        m = b[0]
        break
    lis.append(b)

ans = ""
for i,s in sorted(lis):
    if m % i == 0: ans += s

if ans == "" : print(m)
else : print(ans)
