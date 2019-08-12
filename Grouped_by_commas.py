# group_by_commas(1),  '1'
# group_by_commas(10), '10'
# group_by_commas(100), '100'
# group_by_commas(1000), '1,000'
# group_by_commas(10000), '10,000'
# group_by_commas(100000), '100,000'
# group_by_commas(1000000), '1,000,000'
# group_by_commas(35235235), '35,235,235'

def group_by_commas(n):
    n=str(n)
    # print(n,type(n))
    
    # print(len(n))
    if len(n) <= 3:
        return n
        
    else:
        if (len(n)%3)==1:
            a=''
            for i in range(1,len(n),3):
                a += ','+ n[i:i+3]

            # print(n[0]+a)
            return n[0]+a

        elif (len(n)%3)==2:

            a=''
            for i in range(2,len(n),3):
                a += ','+ n[i:i+3]
            # print(n[0]+n[1]+a)
            return n[0]+n[1]+a

        else:
            a=''
            for i in range(3,len(n),3):
                a += ','+ n[i:i+3]
            # print(n[0]+n[1]+n[2]+a)
            return n[0]+n[1]+n[2]+a


group_by_commas(1),         '1'
group_by_commas(100),       '100'
group_by_commas(1000),      '1,000'
group_by_commas(1000000), '1,000,000'
group_by_commas(35235235),'35,235,235'
group_by_commas(359235235)