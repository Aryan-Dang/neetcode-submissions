class Solution:
    """
    Remembered that this is basic 2 pointer problem ans we can iterate from back and front at the same time and if the values aren't equal then we bvreak!

    forgot about important edge case which ios not considering the case vs considering - important for string porbems!!!

    also important here that we should be skipping the spaces/non-alphanumeric chars!!
    """
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1

        stripped_string = s.lower()

        print(stripped_string)

        while i < j:
            while not stripped_string[i].isalnum() and i < j:
                i += 1
            while not stripped_string[j].isalnum() and i < j:
                j -= 1
            if stripped_string[i] != stripped_string[j]:
                return False
            i += 1
            j -= 1
        return True