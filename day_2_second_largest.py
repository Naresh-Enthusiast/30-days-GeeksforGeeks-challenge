class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        first,second = -1, -1
        
        for num in arr:
            if num > first:
                second = first
                first = num
                
            elif num > second and second != first:
                second = num
            
        return second if second != -1 else -1