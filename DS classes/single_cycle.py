def has_single_cycle(array):
    elem_visited = 0
    curr_idx = 0

    while elem_visited < len(array):
        if elem_visited > 0 and curr_idx == 0:
            return False

        elem_visited += 1
        curr_idx = get_next_idx(curr_idx, array)

    return curr_idx == 0


def get_next_idx(curr_idx, array):
    jump = array[curr_idx]
    next_idx = (curr_idx + jump) % len(array)
    return next_idx if next_idx >= 0 else next_idx + len(array)
