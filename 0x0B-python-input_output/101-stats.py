#!/usr/bin/python3
"""
Task: 101-stats
Write a function that returns
the number of lines in a text file
By Khaled Mansour
"""


def print_metrics(accumulated_size, status_code_counts):
    """
    Display the current file size and count of status codes.
    """
    print("Total file size: {}".format(accumulated_size))
    # Print the count for each status code in ascending order
    for key in sorted(status_code_counts):
        print("Status code {}: {}".format(key, status_code_counts[key]))


if __name__ == "__main__":
    import sys

    # Initialize the total size and a dictionary for status code counts
    total_size = 0
    status_code_counts = {}
    # List of valid HTTP status codes to track
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_counter = 0

    try:
        for line in sys.stdin:
            # Every 10 lines, print the metrics
            if line_counter == 10:
                print_metrics(total_size, status_code_counts)
                line_counter = 1
            else:
                line_counter += 1

            # Split the line into parts to process status code and size
            parts = line.split()

            # Safely convert and add the file size
            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass  # If there's an error, skip adding the size

            # Check for a valid status code and increment its count
            try:
                if parts[-2] in valid_codes:
                    status_code_counts[
                        parts[-2]] = status_code_counts.get(parts[-2], 0) + 1
            except IndexError:
                pass  # If there's an error, skip counting the status code

        # Print the final metrics after processing all lines
        print_metrics(total_size, status_code_counts)

    except KeyboardInterrupt:
        # Handle Ctrl+C interruption and print the metrics gathered so far
        print_metrics(total_size, status_code_counts)
        raise
