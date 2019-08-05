# is_square(-1), False, "-1: Negative numbers cannot be square numbers"
# is_square( 0), True, "0 is a square number"
# is_square( 3), False, "3 is not a square number"
# is_square( 4), True, "4 is a square number"
# is_square(25), True, "25 is a square number"
# is_square(26), False, "26 is not a square number"

def is_square(n):
    if n<0:
        return False
    else:
        a=round(n**0.5,2)
    
    b=(a)**2

    # print(a)
    # print(b)

    if b == n:
        # print(b)
        bool=True
        
    else :
        # print(b)
        bool=False

    return bool



# is_square( 0)
print(is_square( 1454521440))
print(is_square( -1))
# print(is_square( 25))
# print(is_square(26))

#比較餘數
# print(3.33333 % 1)
# print(3 % 1)