#!/usr/bin/python3
"""
This module provides function to parse a line and print summary
in required format.
"""
import sys
import re
import signal
from collections import Counter


pattern = re.compile(r"(.*)(?P<code>\d{3,})\s+(?P<size>\d{1,})$")


def parse_line(line):
    """
    Parses a line of text using a regular expression pattern.

    Parameters:
    - line (str): The line of text.

    Returns:
    - dict or None: A dictionary containing named groups  or None
    """
    match = re.match(pattern, line)
    if match:
        return match.groupdict()
    return None


def count_codes_acc_size(info_list):
    """
    Count the occurrences of specific codes in a list of dictionaries.
    Calculate the total size.

    Parameters:
    info_list (list): A list of dictionaries containing information.
      Each dictionary must have keys "code" and "size".

    Returns:
    codes_count (Counter): A Counter object
    size_counter (int): The total size accumulated from the "size" values.
    """
    CODES_LIST = ["200", "301", "400", "401", "403", "404", "405", "500"]
    codes_count = [
        d["code"] for d in info_list if "code" in d if d["code"] in CODES_LIST
    ]
    codes_count = Counter(codes_count)
    size_counter = sum([int(d["size"]) for d in info_list if "size" in d])
    return codes_count, size_counter


def print_codes(codes_counter):
    """
    Print codes in format described
    Returns: None
    """
    for d in sorted(codes_counter):
        print(f"{d}: {codes_counter[d]}")


def main():
    """
    Run the main code

    Returns None
    """
    counter = 0
    codes_counter = Counter({})
    size_counter = 0
    info_list = []

    def summary(info_list, codes_counter, size_counter):
        """
        Print final output/summary

        Return None
        """
        if info_list:
            cc, sc = count_codes_acc_size(info_list)
            codes_counter.update(cc)
            size_counter += sc
            print(f"File size: {size_counter}")
            print_codes(codes_counter)

    def sig_handler(sig, frame):
        """
        Signal handler for ctrl-c

        Handles ctrl-c, prints summary
        """
        nonlocal info_list, codes_counter, size_counter
        summary(info_list, codes_counter, size_counter)
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)

    try:
        for line in sys.stdin:
            counter += 1
            pl = parse_line(line)
            if pl:
                info_list.append(parse_line(line))
            if counter == 10:
                summary(info_list, codes_counter, size_counter)
                info_list = []
                counter = 0
    except KeyboardInterrupt:
        pass
    finally:
        summary(info_list, codes_counter, size_counter)


if __name__ == "__main__":
    main()
