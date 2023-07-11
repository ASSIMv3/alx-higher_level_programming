#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys


def print_statistics(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status, count in sorted(status_counts.items()):
        print("{}: {}".format(status, count))


def parse_line(line):
    parts = line.split()
    status_code = parts[-2]
    file_size = int(parts[-1])
    return status_code, file_size


def main():
    total_size = 0
    status_counts = {}

    try:
        line_count = 0
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
