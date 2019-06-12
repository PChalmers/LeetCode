class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for x in range(numRows)]
        index=0
        try:
            while(True):
                for i in rows:
                    i.append(s[index])
                    index += 1
                for i in rows[-2:0:-1]:
                    i.append(s[index])
                    index += 1
        except:
            pass
        result = ''
        for i in rows:
            result = result + ''.join(i)
        return result
            


s = Solution()
print(s.convert('PAYPALISHIRING', 3)) # PAHNAPLSIIGYIR
print(s.convert('PAYPALISHIRING', 4)) # PINALSIGYAHRPI
print(s.convert('PAYPALISHIRING', 1)) # PAYPALISHIRING