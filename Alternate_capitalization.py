# capitalize("abcdef"),['AbCdEf', 'aBcDeF']
# capitalize("codewars"),['CoDeWaRs', 'cOdEwArS']
# capitalize("abracadabra"),['AbRaCaDaBrA', 'aBrAcAdAbRa']
# capitalize("codewarriors"),['CoDeWaRrIoRs', 'cOdEwArRiOrS']

def capitalize(s):
    odd_up=[]
    even_up=[]
    

    for i in range(len(s)):
        if i%2 == 1:
            odd_up.append(s[i].upper())
            even_up.append(" ")
        else:
            odd_up.append(" ")
            even_up.append(s[i].upper())

    # print(odd_up)
    # print(even_up)

    sum_odd=''
    sum_even=''
    for j in range(len(s)):
        if j%2 == 1:
            sum_odd += odd_up[j]
            sum_even += s[j]
        
        else:
            sum_odd += s[j]
            sum_even += even_up[j]
        
    total=[sum_even,sum_odd]

    # print(total)
    return total

    
    




capitalize("abcdef"),['AbCdEf', 'aBcDeF']