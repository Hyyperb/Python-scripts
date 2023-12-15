values = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0

        if "IV" in s:
            count+=4
            s = s.replace("IV","") 
        elif "IX" in s:
            count+=9
            s = s.replace("IX","")
        if "XL" in s:
            count+=40
            s = s.replace("XL","")
        elif "XC" in s:
            count+=90
            s = s.replace("XC","")
        if "CD" in s:
            count+=400
            s = s.replace("CD","")
        elif "CM" in s:
            count+=900
            s = s.replace("CM","")
        
        for l in s:
            count += values[l]
        
        return count

tests = [input()]

for test in tests:
    print(Solution().romanToInt(test))
