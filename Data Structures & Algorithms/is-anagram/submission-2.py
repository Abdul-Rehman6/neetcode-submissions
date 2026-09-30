class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # s_list = sorted(s)
        # t_list = sorted(t)

        # for i in range(len(s)):
        #     if s_list[i] != t_list[i]:
        #         return False

        # return True

        hash_map_s = {}
        hash_map_t = {}

        for i in s:
            if i in hash_map_s:
                hash_map_s[i] += 1
            else:
                hash_map_s[i] = 1

        for i in t:
            if i in hash_map_t:
                hash_map_t[i] += 1
            else:
                hash_map_t[i] = 1

        if hash_map_s.items() == hash_map_t.items():
            return True
        else:
            return False

