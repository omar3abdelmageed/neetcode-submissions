class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def checkAnagram(str1, str2) -> bool:

            return sorted(str1) == sorted(str2)

        grouped = []
        
        current_group = []

        looked_at = []

        for i in range(len(strs)):
            
            if strs[i] not in looked_at:

                looked_at.append(strs[i])
                current_group.append(strs[i])

                for j in range(len(strs)):

                    if i!=j and checkAnagram(strs[i],strs[j]):

                        current_group.append(strs[j])
                        looked_at.append(strs[j])
                
                grouped.append(current_group)
                current_group = []

        return grouped
