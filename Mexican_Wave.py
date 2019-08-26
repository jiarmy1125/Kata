# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

def wave(str):
    print(str)
    x=[]
    for i in range(len(str)):
        # print(i,str[i])
        a=str[i].upper()
        x.append(a)

    # print(x)

    str_str=[]
    str2=''
    y=[]

    for str1 in str:
        if str1 == ' ':
            pass
        else:
            str_str.append(str1)

    # print(str_str)

    for j in range(len(str)):
        str2=''
        if str[j] == ' ':
            str2 += ' '

        else:

            if j==0:
                str2 += x[j] + str[j+1:len(str)]
                y.append(str2)

            elif j==(len(str)-1):
                str2 += str[0:j] + x[j]
                y.append(str2)

            else:
                str2 += str[0:j] + x[j] + str[j+1:len(str)]
                y.append(str2)
        

    print(y)
    return y

wave("hello")
wave(" gap ")