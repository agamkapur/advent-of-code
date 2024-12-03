import re


def sum_valid_multiplications(memory):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, memory)
    total = sum(int(x) * int(y) for x, y in matches)

    return total


def main():
    with open('input.txt') as f:
        data = ''.join(f.readlines())

    print(sum_valid_multiplications(data))


if __name__ == '__main__':
    main()

