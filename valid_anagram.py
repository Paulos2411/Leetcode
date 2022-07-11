class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dummy = dict()
        dummy2 = dict()
        
        for i in s: # doesnt matter if s or t both have the same length
            dummy[i] = 1 + dummy.get(i,0)
        for i in t:
            dummy2[i] = 1 + dummy2.get(i,0)

        for j in dummy:
            if dummy[j] != dummy2.get(j,0):
                return False
        return True
            

