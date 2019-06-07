import sys, string, math

# Function to return max sum such that no two elements are adjacent
def find_max_sum(arr):
    incl = 0
    excl = 0

    for i in arr:
        # Current max excluding i == C ? : opr
        new_excl = excl if excl > incl else incl

        # Current max including i
        incl = excl + i
        excl = new_excl

        # return max of incl and excl
    return (excl if excl > incl else incl)


# Driver program to test above function
n = int(input())
L = [ int(x) for x in input().split()]
print(find_max_sum(L))
