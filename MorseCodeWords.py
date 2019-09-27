"""
    International Morse Code defines a standard encoding where each letter 
    is mapped to a series of dots and dashes, as follows: "a" maps to ".-", 
    "b" maps to "-...", "c" maps to "-.-.", and so on.
"""


class Solution:
    def uniqueMorseRepresentations(self, words: list()) -> int:
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                      "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                      "...-", ".--", "-..-", "-.--", "--.."]

        if len(words) <= 100:
            w1 = []
            for word in words:
                code = ''
                if 1 <= len(word) < 12:
                    for c in word.lower():
                        # use ord() to represent int of Unicode point of char
                        code = code + morse_code[ord(c) - ord('a')]
                    if code not in w1:
                        w1.append(code)
            return len(w1)
        else:
            return -1


words = ["tmwsslt", "oabhx", "mysiuu", "hayri", "hwpb", "hpqs", "kswj", "nniatj",
         "csttj", "tlsj", "csittt", "nbvm", "tleso", "khum", "chj", "ciij", "chj",
         "khum", "chj", "chj", "cham", "tlsj", "chj", "csej", "chj", "ksso", "ndho",
         "ndho", "qmvmg", "qzjg", "qzjg", "aiojl", "lojl", "sttuq", "vxq", "euxq",
         "vxq", "vxq", "vxq", "vdoa", "smuq", "vxq", "djqgi", "bmmkgi", "jkcu", "atqcu",
         "jyav", "xnvy", "xnsqt", "xdunm", "npipm", "dzuy", "xduy", "xdimat", "nwrmwx",
         "xcqtx", "tbaovi", "zutzed", "skzb", "vwxs", "vjib", "zdkf", "glcr", "gafnr",
         "ksnw", "cuew", "cfw", "cuim", "tasnw", "tlrw", "cfw", "cfw", "nbdm", "kefw",
         "cfw", "hhsr", "issif", "hssin", "shhr", "ihhf", "mnfaj", "ovuj", "bpdn", "nvkf",
         "qyxv", "gqgav", "kxmmi", "yuod", "ktejz", "tpjz", "yumz", "tpjtd", "tbaovi",
         "zutzed", "smdba", "vzdu", "vgrv", "ekgpwx", "aagpju", "zpqd"]
print(len(words))
s1 = Solution()
print(s1.uniqueMorseRepresentations(words))
