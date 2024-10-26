#!/usr/bin/python3

"""Write a script that reads stdin line by line and computes metrics
Log parsing

After every ten lines or upon keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point
    - Count of read status codes up to that point
"""


def print_stats(size, status_codes):
    """Print accumulated metrics

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys
    import signal

    # Initialize metrics
    size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
    }
    count = 0

    def signal_handler(sig, frame):
        """Handle keyboard interruption and print final stats."""
        print_stats(size, status_codes)
        sys.exit(0)

    # Register signal handler for keyboard interrupt
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 0

            line = line.split()

            try:
                # Accumulate file size
                size += int(line[-1])
            except (IndexError, ValueError):
                # Skip lines that don't conform to the expected format
                continue

            try:
                # Accumulate status code counts
                status_code = int(line[-2])
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except (IndexError, ValueError):
                # Skip lines with invalid or missing status codes
                continue

            count += 1

        # Print final statistics after EOF
        print_stats(size, status_codes)

    except KeyboardInterrupt:
        # Handle keyboard interrupt and print stats
        print_stats(size, status_codes)
        sys.exit(0)
