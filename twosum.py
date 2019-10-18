
def twoSum( nums, target: int):
        #Vaule = {}.fromkeys
        for i in range(len(nums)):
            a = target - nums[i]
            for j in range(i+1,len(nums),1):
                if a == nums[j]:
                    return [i,j]


findSum = twoSum(nums = [1,2,3,4,5,6,8],target=14)
print(findSum)
