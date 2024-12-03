import re

def multPattern(text):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, text)
    total = 0
    for match in matches:
        x, y = int(match[0]), int(match[1])
        total += x * y
    
    return total

file = open("input.txt", "r")
text = file.read()
result = multPattern(text)
print(result)

