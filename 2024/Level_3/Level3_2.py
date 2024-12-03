import re

def multPattern(text):
    enabled = True
    total = 0

    tokens = re.findall(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", text)

    for token in tokens:
        if(token == "do()"):
            enabled = True
        elif(token == "don't()"):
            enabled = False
        elif(token.startswith("mul(") and enabled):
            match = re.match(r'mul\((\d+),(\d+)\)', token)
            if(match):
                x = int(match.group(1))
                y = int(match.group(2))
                total += x * y

    return total

file = open("input.txt", "r")
text = file.read()
result = multPattern(text)
print(result)

