
file_path = "Your file path"

#PART1:
res = 0
with open(file_path) as r:
    for data in r.readlines():
        l = list(map(int, data.split()))
        dir = -1 # 1 increasing, -1 decreasing
        ok= True
        for i in range(len(l)):
            if i == 1:
                if l[i-1] > l[i] and 1 <= abs(l[i-1]-l[i]) <= 3:
                    dir = -1
                elif l[i-1] < l[i] and 1 <= abs(l[i-1]-l[i]) <= 3:
                    dir = 1
                else:
                    ok = False 
                    break
            elif i > 1:
                if (l[i-1] < l[i] and dir == -1) or (l[i-1] > l[i] and dir == 1) or 1 > abs(l[i-1]-l[i]) or abs(l[i-1]-l[i]) > 3:
                    ok = False
                    break
            last = l[i]
        res += ok
print(res) 


#PART2:
res = 0
with open(file_path) as r:
    for data in r.readlines():
        l1 = list(map(int, data.split()))
        for j in range(len(l1)):
            dir = -1 # 1 increasing, -1 decreasing
            ok = True
            l = l1.copy()
            l.pop(j)
            for i in range(len(l)):
                if i == 1:
                    if l[i-1] > l[i] and 1 <= abs(l[i-1]-l[i]) <= 3:
                        dir = -1
                    elif l[i-1] < l[i] and 1 <= abs(l[i-1]-l[i]) <= 3:
                        dir = 1
                    else:
                        ok = False 
                        break
                elif i > 1:
                    if (l[i-1] < l[i] and dir == -1) or (l[i-1] > l[i] and dir == 1) or 1 > abs(l[i-1]-l[i]) or abs(l[i-1]-l[i]) > 3:
                        ok = False
                        break
                last = l[i]
            if ok:
                res += 1
                break
print(res)     