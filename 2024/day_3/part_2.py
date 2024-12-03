import re


def sum_valid_multiplications(data):
    mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    tokens = re.findall(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", data)

    mul_enabled = True
    total = 0

    for token in tokens:
        token = token.strip()
        if re.match(do_pattern, token):
            mul_enabled = True
        elif re.match(dont_pattern, token):
            mul_enabled = False
        elif re.match(mul_pattern, token) and mul_enabled:
            x, y = map(int, re.findall(r"\d{1,3}", token))
            total += x * y

    return total


def main():
    with open('input.txt') as f:
        data = ''.join(f.readlines())

    print(sum_valid_multiplications(data))


if __name__ == '__main__':
    main()