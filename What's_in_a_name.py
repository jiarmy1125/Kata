# name_in_str("Across the rivers", "chris"), True
# name_in_str("Next to a lake", "chris"), False

def name_in_str(str, name):
    bool=False
    x=[]
    i = []
    a=[]

    str=str.lower()
    # print(str)
    name=name.lower()
    # print(name)

    for num in str:
        i.append(num)

    for str_name in name:
        x.append(str_name)
    
    # print(i)
    # print(x)

    for str_name in i:    
        if str_name in x:
            a.append(str_name)

        else:
            bool=False

    # print(a)

    if (len(a) != len(x)) :
        for a1 in a:
            # print(a,":",a1)
            if len(x) != 0:
                if a1 == x[0]:
                    x = x[1:]
            else:
                break
        if len(x) == 0:
            bool = True
        else:
            bool = False

    else:
        for a1 in a:
            if a[0]==x[0]:
                bool=True
                a=a[1:]
                x=x[1:]
                
            else:
                bool=False
            
    return bool


# def name_in_str(str, name):
#     str=str.lower()
#     x=name.lower()

#     for a1 in str:
        
#         if len(x) != 0:
#             if a1 == x[0]:
#                 x = x[1:]
#         else:
#             break
#     if len(x) == 0:
#         return True
#     else:
#         return False


print(name_in_str("a.KvlhidlSSPp.XX oliGLblQaW;LDMq K!QMV","rIb")) 
print(name_in_str("Across the rivers", "chris")) #t
print(name_in_str("Next to a lake", "chris")) #False
print(name_in_str("Under a sea", "chris"))  #False
print(name_in_str("A live son", "Allison")) #False
print(name_in_str("Just enough nice friends","Jennifer")) 
print(name_in_str("z!apWEhB G ZWbyo,varAEJvN", "iRnQ")) #f
print(name_in_str("b!sJo  TkCkTFkgGCDYDthQDl: RcLLL eggo O", "KDr")) #t
print(name_in_str("IP?Np;!AekPmUmxSOOkPu yr? oS", "oo")) #t