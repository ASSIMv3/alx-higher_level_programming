#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys


size = 0
status_codes = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
count = 0


def print_statistics(file_size, status_codes):
    """Print accumulated metrics"""
    print("File size: {}".format(file_size))
    for k in sorted(status_codes):
        print("{}: {}".format(k, status_codes[k]))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            if num_lines == 10:
                print_statistics(file_size, status_codes)
                num_lines = 1
            else:
                num_lines += 1

            line = line.split()

            try:
                file_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_statistics(file_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(file_size, status_codes)
        raise
