class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        s = sorted(s, key=lambda x:int(x[-1]))
        output = []
        for x in s:
            output.append(x[:-1])
        return " ".join(output)