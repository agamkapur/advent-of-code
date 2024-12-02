def main():
    left_list = []
    right_list = []

    with open('input.txt', 'r') as f:
        for line in f:
            left, right = line.strip().split()
            left_list.append(left)
            right_list.append(right)

    frequency_dict = {}

    for item in right_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1

    result = 0

    for item in left_list:
        if item in frequency_dict:
            result += int(item)*frequency_dict[item]

    print(result)


if __name__ == '__main__':
    main()