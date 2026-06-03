class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_frequency = dict()
        flag = True

        if len(s) != len(t):
            return False

        for letter in s:
            letter_frequency[letter] = s.count(letter)
        
        for letter in t:
            if s.find(letter) == -1:
                flag = False
            elif not letter_frequency[letter] == t.count(letter):
                flag = False
        return flag