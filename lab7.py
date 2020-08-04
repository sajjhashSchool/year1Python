def Kseq(start, stop, step):
    """ (int,int,int) -> list of integers

    Input: This function is passed start (>= 0), stop (>start), and step (>= 1) values that define a sequence of numbers.
    Output: This function returns a list of the corresponding K sequence.

    >>>Kseq(0,6,1)
    [2, 1, 9, 100, 11881, 141419664]
    >>>Kseq(2,6,2)
    [9, 11881]
    """
    range_of_inputs = range(start, stop, step)
    output = []
    def k(n):
        if n == 0:
            return 2
        elif n == 1:
            return 1
        else:
            return ((k(n-1) + k(n-2))**2)
    for number in range_of_inputs:
        k_of_n = k(number)
        output.append(k_of_n)            
    return output        
