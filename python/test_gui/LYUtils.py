# Author: Jason Lu
def format_time(ttime):
    hours = int(ttime / (60*60))
    left_m = ttime-hours*3600
    minutes = int(left_m / 60)
    left_s = left_m - minutes*60
    seconds = int(left_s % 60)

    str_time = ''

    if hours > 10:
        str_time += str(hours)
    else:
        str_time += '0' + str(hours)
    str_time += ':'

    if minutes > 10:
        str_time += str(minutes)
    else:
        str_time += '0' + str(minutes)
    str_time += ':'

    if seconds > 10:
        str_time += str(seconds)
    else:
        str_time += '0' + str(seconds)

    return str_time

