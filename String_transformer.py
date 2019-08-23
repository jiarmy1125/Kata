# "Example Input" ==> "iNPUT eXAMPLE"

def string_transformer(s):
    x=s.split(" ")
    
    b=x[::-1]

    sort_1=''

    for i in range(len(b)-1):
        sort_1 += b[i] + " "

    sort_1 += b[len(b)-1]
    
    # print(sort_1.strip(" "))
    print(sort_1.strip(" ").swapcase(),len(sort_1.strip(" ").swapcase()))
    print(sort_1.swapcase(),len(sort_1.swapcase()))
    return sort_1.swapcase()

string_transformer("Example string"), "STRING eXAMPLE"
# string_transformer("Example Input"), "iNPUT eXAMPLE"
# string_transformer("To be OR not to be That is the Question"), "qUESTION THE IS tHAT BE TO NOT or BE tO"
# # Should handle empty string
# string_transformer(""), ""
# # Should handle multiple spaces
string_transformer("You Know When  THAT  Hotline Bling"), "bLING hOTLINE  that  wHEN kNOW yOU"
# # Should handle leading space
string_transformer(" A b C d E f G "), " g F e D c B a "