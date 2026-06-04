class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            sorted_str = sorted(word)
            key = "".join(sorted_str)

            groups[key].append(word)

        return list(groups.values())


        