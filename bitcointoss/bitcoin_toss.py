#! /usr/bin/python3

import sys
import itertools

def all_combinations_length(n):
    """
    Returns the total number of possible combinations of length n.
    """
    return 2**n

def can_fit(line, remaining_combinations_length, p, n):
    """
    This function is a precheck and returns whether or not
    it'd be possible, based on the length of the line and the arguments,
    to find a solution.
    """
    res = len(line) >= (remaining_combinations_length * n + p)
    return res

def find_solution(line):
    # n is the combination length, as stated in the problem
    for n in range(len(line), 0, -1):
        # p is the start index to check for combinations.
        for p in range(0, len(line)):
            total = all_combinations_length(n)
            if not can_fit(line, total, p, n):
                break
            curr_idx = p
            # All the combinations previously seen, to avoid repeats.
            seen_combinations = set()
            while len(seen_combinations) < total and curr_idx+n <= len(line):
                chunk = line[curr_idx:curr_idx+n] # Current combination
                if chunk in seen_combinations:
                    break
                seen_combinations.add(chunk)
                curr_idx = curr_idx + n
            if len(seen_combinations) == total:
                # success! return the resulting n and p
                return n, p
    raise ValueError("There is no solution for line " + str(line))

line_n = 0
n_cases = 0
for line in sys.stdin:
    line_n = line_n+1
    if line_n == 1:
        # First line
        n_cases = int(line)
        continue
    if n_cases+1 < line_n:
        sys.exit(0)
    # The last character on line is a newline
    n, p = find_solution(line[:-1])
    print(str(n) + " " + str(p))
