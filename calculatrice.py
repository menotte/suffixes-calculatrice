def parse_number(num_str):
    suffixes = {'k': 1e3, 'm': 1e6, 'b': 1e9, 't': 1e12, 'q': 1e15}

    for suffix, value in suffixes.items():
        if num_str.endswith(suffix):
            number = float(num_str[:-1])
            return number * value

    return float(num_str)

def format_number(num):
    suffixes = ['', 'k', 'm', 'b', 't', 'q']

    suffix_index = 0
    while num >= 1000 and suffix_index < len(suffixes) - 1:
        num /= 1000
        suffix_index += 1

    formatted_num = '{:.2f}{}'.format(num, suffixes[suffix_index])
    return formatted_num

while True:
    operation = input("Operation : ")

    if operation.lower() == 'exit':
        print("Bye")
        break

    if '+' in operation:
        operator = '+'
    elif '-' in operation:
        operator = '-'
    elif '*' in operation:
        operator = '*'
    elif '/' in operation:
        operator = '/'
    else:
        print("Wrong operator")
        continue

    operands = operation.split(operator)
    operand1 = parse_number(operands[0].strip())
    operand2 = parse_number(operands[1].strip())

    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2

    formatted_result = format_number(result)
    print("Result :", formatted_result)
    print()
