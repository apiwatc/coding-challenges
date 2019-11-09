"""
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
"""


def countCharacters(words, chars):
    new = ''
    for word in words:
        for w in word:
            if word.count(w) > chars.count(w):
                break
        else:
            new += word
    return len(new)


words = ["hello", "world", "leetcode"]
chars = "welldonehoneyr"
print(countCharacters(words, chars))
