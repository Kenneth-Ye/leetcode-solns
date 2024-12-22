class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            encoded += str(len(strs[i])) + "#" + strs[i]
        return encoded

    def decode(self, s: str) -> List[str]:
        arr = []
        while(s != ""):
            length = int(s.split("#")[0])
            if length < 10:
                print(s[2:])
                s = s[2:]
            elif length < 100:
                s = s[3:]
            else:
                s = s[4:]
            arr.append(s[0:length])
            s = s[length:]
        return arr
