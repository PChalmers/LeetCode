import numpy as np

class solution:

    def __init__(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2
        self.prevAns = np.full((len(self.seq1), len(self.seq2)), -1)
        self.numFound = 0

    def computeLCS(self):
        result = self.LCS(self.seq1,len(self.seq1)-1,self.seq2,len(self.seq2)-1)
        print('numfound = ', self.numFound, 'result = ', result)

    def LCS(self,s1,n,s2,m):
        if (n<0 or m<0):
            return 0
        if(self.prevAns[n][m] != -1):
            self.numFound += 1
            return self.prevAns[n][m]
        if (s1[n] == s2[m]):
            result = 1 + self.LCS(s1,n-1,s2,m-1) # no harm in matching up
        else: 
            result = max( self.LCS(s1,n-1,s2,m), self.LCS(s1,n,s2,m-1) )
        self.prevAns[n][m] = result
        return result

s = solution("ABAZDC", "BACBAD")
print(s.computeLCS())
