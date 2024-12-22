class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            letterArr = [0] * 26
            for letter in string:
                letterArr[ord(letter) - ord('a')] += 1

            if tuple(letterArr) not in groups: 
                groups[tuple(letterArr)] = [str(string)]
            else:
                groups[tuple(letterArr)].append(str(string))
        output = []
        for key in groups:
            print(groups[key])
            output.append(groups[key])
        return output
