class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Requirements:
        all lowercase
        short circuit : differing lengths can't be anagrams
        output in any order
        could just find the characterRepr of each string and then create hashmap of countCharacter : vals 
        return .items()
        will need to convert the list into a string/tuple as the key of a dict needs to be immutable datatype 
        let's use tuple as the keys because seems like it's faster than using the string as the keys...
        """

        def getCharRepr(string : str) -> str:
            charCount = [0] * 26
            for char in string:
                charIndex = ord(char) - ord("a")
                charCount[charIndex] += 1
            return tuple(charCount)
        
        anagrams = {}

        for string in strs:
            charRepr = getCharRepr(string)
            if charRepr not in anagrams:
                anagrams[charRepr] = []
            anagrams[charRepr].append(string)
        
        return list(anagrams.values())

