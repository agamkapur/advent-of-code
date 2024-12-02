def is_safe(report):
    increasing = True
    decreasing = True

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]

        if not -3 <= diff <= -1:
            decreasing = False

        if not 1 <= diff <= 3:
            increasing = False

    if increasing or decreasing:
        return True

def main():
    reports = []

    with open('input.txt', 'r') as file:
        for line in file:
            reports.append(list(map(int, line.strip().split())))

    result = 0

    for report in reports:
        for i in range(len(report)):
            report_with_one_item_skipped = report[:i] + report[i + 1:]
            if is_safe(report_with_one_item_skipped):
                result += 1
                break

    print(result)


if __name__ == '__main__':
    main()
