class Solution:
    def is_anagram(self, string1, string2):
        used_letters = {}
        if len(string1) != len(string2):
            return False
        for char in string1:
            used_letters[char] = string1.count(char)
        for key in used_letters.keys():
            if used_letters[key] != string2.count(key):
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        i = 0
        while strs:
            out.append([])
            out[i].append(strs.pop(0))
            j = 0
            while j < len(strs):
                if self.is_anagram(out[i][0], strs[j]):
                    out[i].append(strs.pop(j))
                else:
                    j += 1
            i += 1
        return out