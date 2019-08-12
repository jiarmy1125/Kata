# nth_smallest([3,1,2],2),2
# nth_smallest([15,20,7,10,4,3],3),7
# nth_smallest([-5,-1,-6,-18],4),-1
# nth_smallest([-102,-16,-1,-2,-367,-9],5),-2
# nth_smallest([2,169,13,-5,0,-1],4),2

def nth_smallest(arr, pos):
    sort_arr=sorted(arr)
    # print(sort_arr)
    # print(sort_arr[pos-1])
    return sort_arr[pos-1]
    # return sorted(arr)[pos-1]



# nth_smallest([3,1,2],2)
print(nth_smallest([15,20,7,10,4,3],3))