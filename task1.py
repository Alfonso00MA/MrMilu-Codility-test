def solution(S):
    """
    Given a string S, this function returns the maximum number of moves
    that can be applied to S, where each move involves deleting the letters
    in the word "BANANA" from S.
    """
    
    # Counting occurrences for each of the 3 letters
    b_count = 0
    a_count = 0
    n_count = 0
    
    for char in S:
        if char == 'B':
            b_count += 1
        elif char == 'A':
            a_count += 1
        elif char == 'N':
            n_count += 1
    
    # Calculate the maximum number of moves
    return min(b_count, n_count//2, a_count//3)
