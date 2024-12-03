def rule1(a):
    value = 0
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            if value == 0:
                value = -1
            elif value == 1:
                return False
        elif a[i] < a[i+1]:
            if value == 0:
                value = 1
            elif value == -1:
                return False
    return True

def rule2(a):
    for i in range(len(a)-1):
        diff = abs(a[i] - a[i+1])
        if diff < 1 or diff > 3:
            return False
    return True


safe = 0
file = open("input.txt", "r")
for x in file:
    report = [int(n) for n in x.split()]
    
    r1 = rule1(report)
    r2 = rule2(report)

    if(r1 and r2):
        safe += 1
   
file.close()
print(safe)