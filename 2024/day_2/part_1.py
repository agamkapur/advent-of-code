def main():
    reports = []

    with open('input.txt', 'r') as file:
        for line in file:
            reports.append(list(map(int, line.strip().split())))

    result = 0

    for report in reports:
        increasing = True
        decreasing = True

        for i in range(len(report) - 1):
            diff = report[i+1] - report[i]

            if not -3 <= diff <= -1:
                decreasing = False

            if not 1 <= diff <= 3:
                increasing = False

        if increasing or decreasing:
            result += 1

    print(result)


if __name__ == '__main__':
    main()
