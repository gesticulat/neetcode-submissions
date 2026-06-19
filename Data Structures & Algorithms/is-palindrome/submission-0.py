class Solution:
    def isPalindrome(self, s: str) -> bool:
        characters = ''
        s = s.lower()
        print(f"lowercase string: {s}")
        for char in s:
            if ord(char) >= 97 and ord(char) <= 122 or ord(char) >= 48 and ord(char) <= 57:
                characters += char
        print(f"alphanumeric characters: {characters}")
        return characters == characters[::-1]