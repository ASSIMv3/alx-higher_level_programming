#!/usr/bin/python3
import sys

status_counts = {}
total_file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        # Extract the relevant information from the input line
        parts = line.split()
        status_code = parts[-2]
        file_size = int(parts[-1])

        # Update the total file size
        total_file_size += file_size

        # Update the status code count
        if status_code in status_counts:
            status_counts[status_code] += 1
        else:
            status_counts[status_code] = 1

        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print("Total file size: {}".format(total_file_size))
            for code in sorted(status_counts.keys()):
                print("{}: {}".format(code, status_counts[code]))

except KeyboardInterrupt:
    # Print the final statistics on keyboard interruption
    print("Total file size: {}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))
