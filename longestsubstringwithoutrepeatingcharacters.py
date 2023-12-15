class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        if s == "":
            return ""
        substrings = []
        
        for i in range(len(s)):  #start from each letter
            usedletters = []  
            for letter in s[i:]:  #check each letter
                sslen = 0         # current substring length
                print(letter," in ", s[i:]," used letters:",usedletters)
                if letter in usedletters:
                    substrings.append(s[i:i+sslen])
                    break
                else:
                    usedletters.append(letter)
                    sslen += 1
        
        longestsubstring = ""
        for substring in substrings:
            if len(substring)>len(longestsubstring):
                longestsubstring = substring
        return len(longestsubstring)
            

print(Solution.lengthOfLongestSubstring("helloworld"))
