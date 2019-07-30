# min_value([1, 3, 1]), 13
# min_value([4, 7, 5, 7]), 457
# min_value([4, 8, 1, 4]), 148

def min_value(digits):
    j=0
    while j < len(digits):
        if digits.count(digits[j]) != 1:
            digits.remove(digits[j])
            j=0
        j += 1    
    # print(digits)    
    sort_digits=sorted(digits)

    num=''
    for i in range(len(sort_digits)):
        # print(type(sort_digits[i]))
        str_digits=str(sort_digits[i])
        # print(type(str_digits))
        num += str_digits
    
    print(int(num))
    return int(num)
        

min_value([1, 3, 1])
min_value([4, 7, 5, 7])
min_value([4, 8, 1, 4])