'''
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.
'''

def permute(nums: list[int]) -> list[list[int]]:
    permutations = []
    n = len(nums)
    
    def perm(start, res):
        
        if start == n:
            permutations.append(res[:])
        else:
            for i in range(start,n):
                nums[start], nums[i] = nums[i], nums[start]
                
                res.append(nums[start])
                perm(start+1,res)
                res.pop()
                
                nums[start], nums[i] = nums[i], nums[start]       
    
    perm(0,[])    
    
    return permutations

# test permute
nums = [1,2,3]
print(permute(nums))
