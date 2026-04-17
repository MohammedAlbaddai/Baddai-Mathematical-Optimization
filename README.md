import math

def baddai_quadratic_solver(a, b, c):
    """
    Optimized Quadratic Equation Solver by Mohammed Al-Baddai.
    Reduced operations for computational efficiency.
    """
    K = b / (2 * a)  # The Key 'K' as defined by Baddai
    discriminant = K**2 - (c / a)
    
    if discriminant < 0:
        return "Complex Roots"
    
    root_part = math.sqrt(discriminant)
    x1 = -K + root_part
    x2 = -K - root_part
    return x1, x2

# Example
print(f"Solving x^2 + 5x + 6: {baddai_quadratic_solver(1, 5, 6)}")
