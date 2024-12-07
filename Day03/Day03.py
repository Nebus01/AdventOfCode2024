import re

file_path = "Your file path"


#Input string
input_string = ""
    
with open(file_path,'r') as file:
	input_string = " ".join(line.rstrip() for line in file)

#Regex patterns
mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

#PART1:
def part1():

    matches = re.findall(mul_pattern, input_string)

    #print("Matches:", matches)

    numberspattern = r"mul\((\d+),(\d+)\)"

    total_sum = 0
    for item in matches:
        match = re.match(numberspattern, item)
        if match:
            x, y = map(int, match.groups())  
            total_sum += x * y  

    print("Part 1:", total_sum)
    
part1()


#PART2:
def part2():
    
    tokens = re.findall(mul_pattern+"|"+do_pattern+"|"+dont_pattern, input_string)
    
    #print("Tokens: ", tokens)

    mul_enabled = True
    total_sum = 0

    for token in tokens:
        if token == "do()":
            mul_enabled = True
        elif token == "don't()":
            mul_enabled = False
        elif mul_enabled and token.startswith("mul(") and token.endswith(")"):
            x, y = map(int, token[4:-1].split(","))
            total_sum += x * y

    print("Part 2:", total_sum)

part2()
