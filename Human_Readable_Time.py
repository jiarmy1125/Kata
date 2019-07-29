# make_readable(0), "00:00:00"
# make_readable(5), "00:00:05"
# make_readable(60), "00:01:00"
# make_readable(86399), "23:59:59"
# make_readable(359999), "99:59:59"

def make_readable(seconds):
    sec_time = seconds%60
    # print(sec_time)

    minutes = (seconds-sec_time)//60
    min_time = minutes%60
    # print(min_time)

    hours = (minutes-min_time)//60
    # print(hours)
    
    x = "%02d" % hours + ":" + "%02d" % min_time + ":" + "%02d" % sec_time #純數字，用格式化的方式來補0，s = "%05d" % n -->s == "00123"
    return x


print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))