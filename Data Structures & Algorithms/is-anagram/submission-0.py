class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashforS = {}
        hashforT = {}
        for i in s:
            hashforS[i] = hashforS.get(i,0)+1
        for n in t:
            hashforT[n] = hashforT.get(n,0)+1
        
        if hashforT == hashforS:
            return True
        return False