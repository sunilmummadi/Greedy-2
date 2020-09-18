# Leetcode 621. Task Scheduler

# Time Complexity :  O(n) where n is the size of the string

# Space Complexity : O(1) as hashmap can have no more than 26 charecters

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach: calculate the maxfrequency and count of elements with max frequency using a hashmap. Calculate the
# partitions based on the maxfreq. The pending spots after filling all the maxfrequency elements in each partition
# can be used to calculate the overall empty spots which might take the idle value. The difference between the
# empty spots and pending values gives the minimum no.of idle spots needed. Sum of all the input characters and idle
# values gives the total length.

# Your code here along with comments explaining your approach

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks or len(tasks) == 0:
            return 0
        
        freq = dict()
        
        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1 
                
        maxfreq = -1
        for task in freq:
            maxfreq = max(maxfreq, freq[task] )
        
        maxCount = 0    
        for task in freq:
            if freq[task] == maxfreq:
                maxCount +=1
        
        partitions = maxfreq-1
        pending =len(tasks)-(maxfreq * maxCount)
        empty = partitions*(n-maxCount+1)
        idle = max(0,empty - pending)
        
        return len(tasks) + idle