def move0End(arr):
    i = 0
    for i in range(len(arr)):
        if(arr[i] != 0):
            temp.append(arr[i])

    noOfZeros = len(arr) - len(temp)

    for i in range(noOfZeros):
        temp.append(0)
    return temp

arr = [0,2,3,0,5,27,0,1]
move0End(arr)

