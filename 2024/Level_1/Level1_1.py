a = []
b = []

file = open("input.txt", "r")
for x in file:
    number1 = ""
    number2 = ""
    index = 0;
    for i in x:
        if(index < 5):
            number1 += i
        elif(index> 7):
            number2 += i
        index += 1
    a.append(int(number1))
    b.append(int(number2))

        
file.close()

a.sort()
b.sort()

result = 0
for i in range(0,len(a)):
    result += abs(a[i] - b[i])

print(result)