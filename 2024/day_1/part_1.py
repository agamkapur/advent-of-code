def main():
    left_list = []
    right_list = []

    with open('input.txt', 'r') as f:
        for line in f:
            left, right = line.strip().split()
            left_list.append(left)
            right_list.append(right)

    left_list.sort()
    right_list.sort()

    result = 0

    for left, right in zip(left_list, right_list):
        result += abs(int(left) - int(right))

    print(result)



if __name__ == '__main__':
    main()