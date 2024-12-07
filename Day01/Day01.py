
#Input File Path
file_path = "Your file path"


#PART1:
a1 = []
a2 = []
with open(file_path, "r") as o:
    for data in o.readlines():
        t1, t2 = list(map(int, data.split()))
        a1.append(t1)
        a2.append(t2)
a1.sort()
a2.sort()
ans = 0
for i in range(len(a1)):
    ans += abs(a1[i]-a2[i])
print(ans)


#PART2:
a1 = []
a2 = dict()
with open(file_path, "r") as o:
    for data in o.readlines():
        a, b = list(map(int, data.split()))
        if b in a2:
            a2[b] += 1
        else:
            a2[b] = 1
        a1.append(a)
ans = 0
#print(l1, l2)
for k in a1:
    if k in a2:
        ans += k*a2[k]
print(ans)