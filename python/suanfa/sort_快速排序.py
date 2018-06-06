def sort_quick(array):
    if array is None:
        print("sort array can't be None!!")
        return None

    if len(array) < 2:
        return array
    else:
        pivot = array[0]

        # 所有小于基准值
        less = [i for i in array[1:] if i <= pivot]

        # 所有大于基准值
        greater = [i for i in array[1:] if i > pivot]

        return sort_quick(less) + [pivot] + sort_quick(greater)



from datetime import datetime as dt
start = dt.now()
arr = sort_quick([3,42,10,2,130,20])
print(arr)
delta = dt.now() - start
print("elapsed time:", delta.microseconds)

print('----------------------------------------------------')

def sort_quick2(array):
    if array is None:
        print("sort array can't be None!!")
        return None

    if len(array) < 2:
        return array
    else:
        pivot = int(array[0]['RxKBytes'])
        # 所有小于基准值
        less = [device for device in array[1:] if int(device['RxKBytes']) <= pivot]
        # 所有大于基准值
        greater = [device for device in array[1:] if int(device['RxKBytes']) > pivot]
        return sort_quick2(less) + [array[0]] + sort_quick2(greater)


arr_devices = [{'HostName': 'JasonLukiiPhone', 'RxKBytes': '1316335'}, {'HostName': 'JasontekiiPhone', 'RxKBytes': '8832243'}, {'HostName': 'luyangs-MBP', 'RxKBytes': '19683026'}, {'HostName': 'YangLus-iPad', 'RxKBytes': '320728'}, {'HostName': 'luyangde-iPhone', 'RxKBytes': '2486014'}, {'HostName': '28-F3-66-C2-72-17', 'RxKBytes': '21946'}]
#pivot = arr_devices[0]['RxKBytes']
#print(type(pivot))
#less = [device for device in arr_devices[1:] if int(device['RxKBytes']) > 4000000]
#print("less")
#print(less)

arr_sorted_devices = sort_quick2(arr_devices)
for device in arr_sorted_devices:
        print("联网设备名称:" + device['HostName'] + ", 接受速度:" + device['RxKBytes'])


