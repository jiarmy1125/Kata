# max_tri_sum([3,2,6,8,2,3]),17
# max_tri_sum([2,9,13,10,5,2,9,5]),32
# max_tri_sum([2,1,8,0,6,4,8,6,2,4]),18
# max_tri_sum([-3,-27,-4,-2,-27,-2]),-9
# max_tri_sum([-14,-12,-7,-42,-809,-14,-12]),-33
# max_tri_sum([-13,-50,57,13,67,-13,57,108,67]),232

def max_tri_sum(numbers):
    set_num=set(numbers)
    # print(set_num)
    reverse_num=sorted(set_num, reverse=True)
    # print(reverse_num)

    sum = 0
    # for num in range(len(reverse_num)):
    sum = reverse_num[0] + reverse_num[1] + reverse_num[2]

    # print(sum)
    return sum

max_tri_sum([3,2,6,8,2,3]),17