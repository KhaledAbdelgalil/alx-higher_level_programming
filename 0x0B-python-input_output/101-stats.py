#!/usr/bin/python3
"""
Task: 101-stats
Write a function that returns
the number of lines in a text file
By Khaled Mansour
"""
import sys
import signal

# Initialize a dictionary to hold the status codes and total size
# Possible status codes
status_codes = {str(code): 0 for code in [200, 301,
                                          400, 401, 403, 404, 405, 500]}
total_size = 0  # Total size of all files
line_count = 0  # Line count


def print_stats():
    """Prints the statistics of status codes and total file size."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys(), key=int):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(signum, frame):
    """Signal handler for SIGINT (CTRL + C)."""
    print_stats()
    sys.exit(0)


# Register the signal handler for SIGINT (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        status_code = parts[-2]
        file_size = int(parts[-1])

        if status_code in status_codes:
            status_codes[status_code] += 1
            total_size += file_size

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
