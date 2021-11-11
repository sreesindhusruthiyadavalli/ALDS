class Solution:
    def firstMissingPositive(self, nums) -> int:
        
        for x in range(len(nums)):
            if nums[x] < 0:
                nums[x] = 0
                
                
        for x in range(len(nums)):
            val = abs(num)
	    if 1 <= num <= len(nums):
                if nums[val - 1] > 0:
                   nums[val -1 ] *= -1
                elif nums[val -1] == 0:
                    nums[val -1] = -1 * (len(nums) + 1)
                    
        print(nums)            
                    
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1 
        return len(nums) + 1        
                    
                
                
sol = Solution()
num = list([1,2,0])
sol.firstMissingPositive(num)
                            
