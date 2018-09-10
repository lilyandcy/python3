class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        count = 1
        start = 0
        while i < len(chars) - 1:
            if chars[i + 1] == chars[i]:
                count = count + 1
                i = i + 1
                # Boundary check
                if i == len(chars) - 1 and count > 1:
                    for r in range(count - 1):
                        chars.pop(start + 1)
                    # move count number to char list
                    ncount = count
                    scount = str(ncount)
                    for j in range(len(scount)):
                        chars.insert(start + 1, scount[len(scount) - j - 1])
                    i = start + len(scount) + 1
            else:
                if i > start:
                    # Remove all following same char
                    for r in range(count - 1):
                        chars.pop(start + 1)
                    # move count number to char list
                    ncount = count
                    scount = str(ncount)
                    for j in range(len(scount)):
                        chars.insert(start + 1, scount[len(scount) - j - 1])
                    i = start + len(scount) + 1
                    start = i
                    count = 1
                else:
                    i = start + 1
                    start = i
                    count = 1
        return len(chars)
