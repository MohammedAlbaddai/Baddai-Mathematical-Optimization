def albadai_permutation_rule(n, r):
    """
    Calculates the number of r-digit numbers that can be formed 
    from n digits (0-9) without repetition, ensuring the first 
    digit is non-zero.
    
    Formula by: Mohammed Al-Badai
    """
    import math
    permutations = math.perm(n, r)
    return ((n - 1) * permutations) // n
