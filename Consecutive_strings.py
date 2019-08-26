# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta"
# longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh"
# longest_consec([], 3), ""
# longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
# longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu"
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), ""
# longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz"
# longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), ""
# longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), ""

def longest_consec(strarr, k):
    if k <= 0:
        return ""
    
    elif len(strarr) < k:
        return ""

    elif len(strarr) == 0:
        return ""
    
    else:
        x=[]
        y=[]
        z=[]

        for i in strarr:
            print(len(i))
            x.append(len(i))
        print(x)

        sum = ''
        for j1 in range(len(strarr)-k+1):
            # if len(strarr) > 1:
            sum=''
            for j in range(k):
                sum += strarr[j]
                
            print(sum)
            y.append(sum)
            
            strarr.pop(0)
            print(strarr)

        for y1 in y:
            z.append(len(y1))

        z=sorted(z,reverse=True)
        print(y)
        print(z)

        for y2 in y:
            if len(y2) == z[0]:
                print(y2)
                return y2



longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta"
longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh"
longest_consec([], 3), ""
longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu"
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), ""
longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "ixoyx3452zzzzzzzzzzzz"

