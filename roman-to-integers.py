# https://leetcode.com/problems/roman-to-integer/submissions/


class Solution:
    def romanToInt(self, s: str) -> int:
        dic_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        dic_roman2 = {'IV': 2, 'IX': 2, 'XL': 20, 'XC': 20, 'CD': 200, 'CM': 200}

        res = 0
        for ch in s:
            res += dic_roman[ch]

        for key, value in dic_roman2.items():
            count = s.count(key)

            res = res - value*count

        return res


    # method two
    def romanToInt(self, s: str) -> int:

        i=0
        Sum=0
        h={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}

        while i<len(s):
            
            if(i+1<len(s)):
                
                if(s[i]+s[i+1] in h):
                    Sum+=h[s[i]+s[i+1]]
                    i+=2
                    
                else:
                    Sum+=h[s[i]]
                    i+=1
                    
            else:
                Sum+=h[s[i]]
                i+=1
                
        return Sum