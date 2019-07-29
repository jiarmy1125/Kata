# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890"
# create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111"
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890"
# create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890"
# create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000"

def create_phone_number(n):
    num=[]
    num_1=''
    num_2=''
    num_3=''
    # a=str(n)
    # print(a)

    for i in n:
        a=str(i)
        num.append(a)

    for j in range(len(num)):
        if j < 3:
            num_1 += num[j]
        elif 2<j<6:
            num_2 += num[j]
        else:
            num_3 += num[j]


    x=("(" + num_1 + ")"+" ")
    y=num_2+"-"
    z=num_3
    
    sol=x+y+z
    print(sol)
        


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])