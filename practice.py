def find_majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1

        elif num == candidate:
            count +=1
        else:
            count -=1 

    actual_count = 0
    for num in nums:
        if num == candidate:
            actual_count +=1
    
    if actual_count > len(nums) //2:
        return candidate
    else:
        return "no majority element exitsts"

arr = [2,2,1,1,2,2]
print(f"mojority element :{find_majority_element(arr)}")
