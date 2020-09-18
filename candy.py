# Leetcode 135. Candy

# Time Complexity :  O(n) where n is the size of the array

# Space Complexity : O(1)

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach: In forward pass compare current with left neighbour and if it has greater rating current gets 
# gets 1 candy more than that of left neighbour. IN backward pass compare current with right neighbour and 
# if it has greater rating current gets 1 candy more than that of right neighbour if it is greater than 
# current's present candy.

# Your code here along with comments explaining your approach

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings or len(ratings) == 0:
            return []
        
        candy = [1]*len(ratings)
        # forward
        for i in range(1,len(ratings)):
            # if ratings of left neighbour is greater than current
            if ratings[i] > ratings[i-1]:
                # current gets 1 candy more than that of left neighbour
                candy[i] = candy[i-1]+1
        # backward
        for i in range(len(ratings)-2,-1,-1):
            # if the right neighbour has less candy than current
            if ratings[i] > ratings[i+1]:
                # current gets 1 candy more than that of right neighbour if it is greater than 
                # current's present candy
                candy[i] = max(candy[i],candy[i+1]+1)
                
        result = 0
        for i in candy:
            result += i
        return result