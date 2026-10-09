n = int(input())
res=0
for i in range(1,n+1):
    s = str(i)
    if "2" in s or"0" in s or"1" in s:
        res+=1
print(res)