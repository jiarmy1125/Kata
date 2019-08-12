# product_array([12,20]), [20,12])
# product_array([3,27,4,2]), [216,24,162,324])
# product_array([13,10,5,2,9]), [900,1170,2340,5850,1300])
# product_array([16,17,4,3,5,2]), [2040,1920,8160,10880,6528,16320])

def product_array(numbers):
    sum = 1
    total = 1
    x=[]

    for num in numbers:
        sum = sum * num
    
    # print(sum)
    
    for num_1 in numbers:
        total = sum // num_1
        # print(num_1,total)
        x.append(total)

    print(x)
    return x

product_array([1,5,2]), [10,2,5]