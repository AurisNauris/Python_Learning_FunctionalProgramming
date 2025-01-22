"""
Problem 2: Using Mutable Variables Correctly
Problem: Permutations of a List
Write a recursive function to generate all permutations of a given list.
Use a mutable list to store the intermediate results, but ensure no unintended side effects occur between recursive calls.
Examples:
permute([1, 2])  # Output: [[1, 2], [2, 1]]
permute([1, 2, 3])  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""
def permute_1(ns):
    if len(ns) <= 1:
        return [ns]
    
    result = []
    for i, n in enumerate(ns):
        # Exclude current number and find permutations of the rest
        rest = ns[:i] + ns[i+1:]
        for perm in permute_1(rest):
            result.append([n]+perm)

    return result

print(permute_1([1,2,3,4]))

