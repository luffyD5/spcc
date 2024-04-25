import re
TOKENS = {
    '=': 'Assignment op', '+': 'Addition op', '-': 'Subtraction op', '/': 'Division op',
    '*': 'Multiplication op', '<': 'Lessthan op', '>': 'Greaterthan op',
    'int': 'integer type', 'float': 'Floating point', 'char': 'Character type', 'long': 'long int',
    ':': 'colon', ';': 'semi-colon', '.': 'dot', ',': 'comma',
    'a': 'Identifier', 'b': 'Identifier', 'c': 'Identifier', 'd': 'Identifier'
}
tokens_key = TOKENS.keys()
dataFlag = False
program = []
while True:
    line = input("Enter a line of code (or type 'exit' to quit): ")
    if line.lower() == 'exit':
        break
    program.append(line)
count = 0
for line in program:
    count += 1
    print("line#", count, "\n", line)
    tokens = re.findall(r'[a-zA-Z_]\w*|[+\-*/<>=(),.]', line)
    print("Tokens are ", tokens)
    print("Line#", count, "properties \n")
    for token in tokens:
        if token in tokens_key:
            print(token, ":", TOKENS[token])
    dataFlag = False
