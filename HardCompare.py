import math

def compare_exponents(A, B, C, D):
    # Use logarithmic comparison to avoid overflow
    left = B * math.log(A)
    right = D * math.log(C)
    
    if left > right:
        print("YES")
    else:
        print("NO")

# Example usage:
A, B, C, D = map(int, input().split())
compare_exponents(A, B, C, D)