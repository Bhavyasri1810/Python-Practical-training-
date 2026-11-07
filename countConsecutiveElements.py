def countConsecutiveElements(arr):
    count =  0
    maxCount = 0
    for i in range(len(arr)):
        if(arr[i] == 1):
            count += 1
        else:
            maxCount = max(maxCount,count)
            count = 0
    maxCount = max(maxCount,count)
    return maxCount

arr = [1,1,1,0,1,0,0,1,1,1,1]
print(countConsecutiveElements(arr))
