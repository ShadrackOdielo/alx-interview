#!/usr/bin/python3

import sys
import re


def extract_status_code(line):
    """Extracts and returns the status code from a log line."""
    match = re.search(r"\s(\d{3})\s", line)
    if match:
        return match.group(1)
    else:
        return None


def main():
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }
    total_size = 0
    counter = 0

    try:
        for line in sys.stdin:
            counter += 1
            status_code = extract_status_code(line)

            if status_code in status_codes:
                status_codes[status_code] += 1

            # Extract the file size using a regular expression
            file_size_match = re.search(r"(\d+)$", line)
            if file_size_match:
                file_size = int(file_size_match.group(1))
                total_size += file_size

            if counter == 10:
                print("File size: {}".format(total_size))
                for key, value in sorted(status_codes.items()):
                    if value != 0:
                        print("{}: {}".format(key, value))
                counter = 0

    except KeyboardInterrupt:
        print("File size: {}".format(total_size))
        for key, value in sorted(status_codes.items()):
            if value != 0:
                print("{}: {}".format(key, value))
        raise


if __name__ == "__main__":
    main()
