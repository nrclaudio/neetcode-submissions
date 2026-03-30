class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string))
            encoded += "#"
            encoded += string
        return encoded


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        j = 0
        while j < len(s):
            if s[j] == '#':
                length = int(s[i:j])
                word = s[j+1:j+1+length]
                result.append(word)
                j = j + length + 2
                i = j - 1
            else:
                j +=1
                
        return result        
