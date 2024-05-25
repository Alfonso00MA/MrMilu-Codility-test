def solution(S):
    """    
    A string S made of uppercase Eglish letters is given. 
    In one move, six letters forming the word BANANA can be deleted from S.
    What is the maximum number of times such a move can be applied to S?
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
    
    print("B: {} A: {} N: {}".format(b_count, a_count, n_count))
    # Calculate the maximum number of moves
    return min(b_count, n_count//2, a_count//3)
    
    
    
def test_solution():
    assert(solution("NAABXXAN")==1)
    assert(solution("NAANAAXNABABYNNBZ")==2)
    assert(solution("QABAAAWOBL")==0)

test_solution()