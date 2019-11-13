"""
Given an array A of strings made only from lowercase letters,
return a list of all characters that show up in all strings within the list (including duplicates).
For example, if a character occurs 3 times in all strings but not 4 times,
you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]
"""


def commonChars(A):
    # unique char
    ch_list = set(A[0])
    common = []
    for one in ch_list:
        count_min = []
        for w in A:
            count_min.append(w.count(one))
        # minimum of unique char appears in word
        n = min(count_min)
        if n:
            # add # of char to list
            common += [one]*n
    return common


A = ["bella", "label", "roller"]
print(commonChars(A))
