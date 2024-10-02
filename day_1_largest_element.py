from typing import List


class Solution:
    def largest(self, arr : List[int]) -> int:
        # code here
        if len(arr) == 0:
            return none
            
        largest = arr[0]
        
        for num in arr:
            if num > largest:
                largest = num
                
        return largest