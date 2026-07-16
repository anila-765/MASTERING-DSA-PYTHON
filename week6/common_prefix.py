class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first=strs[0]
        print(first)
        n=len(strs)
        last=strs[n-1]

        index=-1
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                break
            index=i
        if index==-1:
            return ""
        else:
            return first[:index+1]
        
