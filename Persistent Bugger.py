#  persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
#                        # 1*2*6 = 12, and finally 1*2 = 2.
#  persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
#                        # and 4 has only one digit.

def persistence(n):
    # print(type(n))
    nn=str(n)
    # print(type(nn))

    if len(nn) == 1:
        print(0)
        return 0
    
    else:

        arr_n=[]
        arr_n.append(nn)
        # print(arr_n)

        for i in arr_n:
            if len(i) != 1:
                x=[]
                sum=1
                for n1 in i:
                    x.append(n1)

                for n2 in x:
                    n2=int(n2)
                    sum *= n2

                # print(sum)
                arr_n.append(str(sum))
                # print(arr_n)

            
        print(len(arr_n)-1)
        return len(arr_n)-1


persistence(39), 3
persistence(4), 0
persistence(25), 2
persistence(999), 4