

# https://leetcode.com/problems/decode-string/description/?envType=study-plan-v2&envId=leetcode-75




class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for ch in s:

            if ch != ']':
                stack.append(ch)
            else:
                string = ""
                while stack[-1] != '[':
                    string = stack.pop() + string        # order is important
                stack.pop()

                nums = ""
                while stack and stack[-1].isdigit():
                    nums = stack.pop() + nums            # order is important
                stack.append(int(nums)*string)

        return "".join(stack)