class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def countChars(string : str) -> str:
            stringCounter = [0]*26
            for c in string : #c is a str!
                index = ord(c) - 97
                stringCounter[index] += 1 
            return stringCounter
        
        return countChars(s) == countChars(t)