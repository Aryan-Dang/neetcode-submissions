class Solution:
    """
    list of strings -> one string
    one string -> list of string

    brute force would be to separate with a delimiter like a ","

    easy solution : runtime - O(N) space ; O(N*M)

    followup : breaks if we have the delimiter in the string, 
    possible option : encode each string into ASCII value + delimiter and then use this to reconstruct the value
    thought of this solution based on the constraint given that the value is a valid ASCII character

    maybe to not rely on the ASCII value we could try simply hashing each character separating with a delimiter and then reconstructing?

    hmm seems like the hashing isn't reliable as it's outcome would be different each time the machine is restarted which is where the different machine thing comes into play which means that we can't rely on tradiitonal hashng techniques...

    thinking through the tools avalible to me like sets, hash maps - they wouldn't work because we need to preserbe the order of the words... the order matters so sets is out
    so sequencing matters in this encoding...

    what happened is that it broke because we didn't separate the chars from the strings, not separating the words with the delimiters, only separating the letters....
    good though that we debugged and found that we weren't differentiating the chars from the words

    debugging allowed me to find the break by seeing the results etc
    now the problem was edge case of empty str... didn't think through that even though it was mentioned in the example... this is a little bad as i should be thinking of this when it's given to me in the example especially....

    edge case that ord("") will raise error apparently
    """

    def encode(self, strs: List[str]) -> str:
        res = []
        if len(strs) == 0:
            return "killme"
        for string in strs:
            word = []
            for c in string:
                word.append(str(ord(c)))
            res.append(",".join(word))
        return ";".join(res)


    def decode(self, s: str) -> List[str]:
        if s == "killme":
            return []
        print(s)
        encodedWords = s.split(";")
        print(encodedWords)
        words = []
        for encodedWord in encodedWords:
            print(encodedWord)
            splitEncodedWord = encodedWord.split(",")
            word = []
            for encodedCharStr in splitEncodedWord:
                if encodedCharStr == "":
                    continue
                encodedChar = int(encodedCharStr)
                print(encodedChar)
                word.append(chr(encodedChar))
            print(word)
            words.append("".join(word))
        return words


