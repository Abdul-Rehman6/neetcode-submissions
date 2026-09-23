class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list) 

        for s in strs:
            count_arr = [0] * 26 # a ... z

            for c in s:
                count_arr[ord(c) - ord('a')] += 1 #asci of current char - asci of 'a' to get the index like 0..25 to put the relevent char count
            
            hash_map[tuple(count_arr)].append(s) # because we cannot have list as key so we need tuple yeah
        
        return list(hash_map.values())