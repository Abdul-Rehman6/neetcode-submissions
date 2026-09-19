class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_list = sorted(s)
        t_list = sorted(t)

        for i in range(len(s)):
            if s_list[i] != t_list[i]:
                return False

        return True
