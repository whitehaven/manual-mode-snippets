import sympy as sy

# Sympy is used here for compatibility with sympy symbols, but will return numeric answers.
# If performance problematic, obviously would use numpy or math instead.

def combinations_w_replacement(n,k):
    return sy.binomial(n+k-1,k)

def combinations_no_replacement(n,k):
    return sy.binomial(n,k)

def permutations_w_replacement(n,k):
    return n**k

def permutations_no_replacement(n,k):
    return sy.factorial(n)/sy.factorial(n-k)

def probability_to_odds(p):
    return p/(1-p)

def odds_to_probability(o):
    return o/(o+1)