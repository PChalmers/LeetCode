import unittest 

class Solution(unittest.TestCase):
    def addBinary(self, a: str, b: str) -> str:
        listA = list(a)
        listB = list(b)
        result = []
        value = carry = 0
        for index in range(max(len(listA), len(listB))):
            value = 0 if index >= len(a) else int(listA.pop(-1)) 
            value += 0 if index >= len(b) else int(listB.pop(-1)) 
            value += carry
            carry = 0
            if(value == 0):
                result.insert(0,'0')
            elif(value == 1):
                result.insert(0,'1')
            elif(value == 2):
                result.insert(0,'0')
                carry += 1
            else:
                result.insert(0,'1')
                carry += 1
        if(carry >0):
            result.insert(0,'1')
        self.assertEqual(''.join(result),'1101011101111001101110100')
        return ''.join(result)

s = Solution()
#print(s.addBinary('110', '1011'))
#print(s.addBinary('10101010', '11001100')) # 0101110110
print(s.addBinary('101010101110101010011', '1100110011001011000100001')) # 01101011101111001101110100