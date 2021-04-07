from collections import deque
# Get all the middle elements of a tuple
def drop_first_last(data):
    first, *middle, last = data
    return middle


# A cool recursive algorithm
def cool_sum(lst):
    head, *tail = lst
    return head + sum(tail) if tail else head


# Return the matching line with he previous line before matching
# Adding or popping from the deque O(1)
def search_pattern_with_history(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
