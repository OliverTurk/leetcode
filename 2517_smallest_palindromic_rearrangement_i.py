class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)

        front = ""
        back = ""
        middle = ""

        for i in range(26):
            c = chr(97 + i)
            if c in freq:
                x = freq[c]
                front = front + (x // 2 * c)
                back = (x // 2 * c) + back
                middle += (x % 2) * c 
                

        return front + middle + back

