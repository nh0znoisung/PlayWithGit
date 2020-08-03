
def numIdenticalPairs(nums):
    
    
    ans = 0
    # for i in range(0,len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if(nums[i] == nums[j]): 
    #             ans+= 1
    dict = {}
    for i in range(0,len(nums)):
        if nums[i] not in dict.keys():
            # x ={nums[i]:1}
            dict.update({nums[i]:1})
        else:
            dict[nums[i]] += 1
    for ele in dict:
        ans+= dict[nums[i]]*(dict[nums[i]]-1)/2

    print(ans)
    return

def add(x,y):
    return x+y

if __name__ == "__main__":
    numIdenticalPairs([1,1,2,3]) 




