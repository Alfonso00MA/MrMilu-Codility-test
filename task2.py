def solution(A,P,B,E):
    """
    Give two arrays of integers, and two integers B, E the function returns True if:
    a package can be moved from B to E using cranes described by the two arrays.
    False otherwise
    """
    ranges = []
    for i,j in zip(A,P):
        ranges.append([j-i, j+i])

    merged_ranges = merge_ranges(ranges)

    if B > E:
        B, E = E, B

    for merged_range in merged_ranges:
        if (merged_range[0] <= B <= merged_range[1]) and (merged_range[0] <= E <= merged_range[1]):
            return True
            
    return False


def merge_ranges(ranges):
    """
    Given a list of intervals it returns the merged version of them: the result has only mutually exclusive intervals
    """
    ranges.sort(key = lambda x:x[0])
    merged_ranges = [ranges[0]]
    for range_loop in ranges[1:]:
        if merged_ranges[-1][1] >= range_loop[0]:
            # If upper bound of the last merged_range is higher than low bound of the range in the loop, 
            # override upper bound of last merged range with max of previous value and upper bound of range in loop
            merged_ranges[-1][1] = max(merged_ranges[-1][1], range_loop[1])
        else:
            merged_ranges.append(range_loop)
    return merged_ranges
