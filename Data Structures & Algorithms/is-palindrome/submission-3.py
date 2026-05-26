class Solution:
    """
    Remembered that this is basic 2 pointer problem ans we can iterate from back and front at the same time and if the values aren't equal then we bvreak!

    forgot about important edge case which ios not considering the case vs considering - important for string porbems!!!

    also important here that we should be skipping the spaces/non-alphanumeric chars!!
    -> cool thing that we can do this in place by moving the 2 pointers till we're at an alpha numeric character and then checking lowercase comparison in place!
    """
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1

        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True