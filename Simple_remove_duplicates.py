# solve([3,4,4,3,6,3]),[4,6,3]
# solve([1,2,1,2,1,2,3]),[1,2,3]
# solve([1,2,3,4]),[1,2,3,4]
# solve([1,1,4,5,1,2,1]),[4,5,2,1]

def solve(arr):
    j=0
    while j < len(arr):
        # print(arr,arr[j])
        if arr.count(arr[j]) != 1:
            arr.remove(arr[j])
            j=0
        
        j += 1    
        
    print(arr)    
    return arr


    # for j in arr:
    #     # print(j,arr.count(j))
    #     print(arr,j)
    #     if arr.count(j) != 1:
    #         arr.remove(j)

        
    # print(arr)


solve([3,4,4,3,6,3])
solve([1,2,1,2,1,2,3])
solve([1,2,3,4])
solve([1,1,4,5,1,2,1])
