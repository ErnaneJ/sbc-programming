"""
# Given two integers  M  and  N , with 1  ≤   M   ≤   N   ≤  5000, 
# you must determine the integer numbers  X  and  Y such that

A. M   ≤   X   ≤   N ; and 
B. Y  is the number of divisors of  X ; and 
C. Y  is the largest possible; and 
D. X  is the largest possible.
"""

# 90 = 2¹ * 3² * 5¹ => 4 + 1 = 5 divisors

# 27 -> 1, 3, 9, 270
# 26 -> 1, 2, 13, 26
# 25 -> 1, 5, 25
# 16 -> 1, 2, 4, 8, 16

# Inputs: M, N
# Output: X, Y

# m = 20
# n = 30


def problem(m,n):
    
    if 1 <= n and n <= 5000:
        if 1 <= m and m <= n:
            x = range(n,m)
        for tryz in x:
            
        else:
    else:
        return None
     


problem(1, 5000)