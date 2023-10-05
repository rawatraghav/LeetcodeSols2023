# https://leetcode.com/problems/queue-reconstruction-by-height/submissions/

class Solution:
      def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
            ans=[]
            people.sort(key= lambda x: (-x[0],x[1]))
            # [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
            for item in people:
                ans.insert(item[1],item)
            return ans