# Author: Jason Lu

"""Train tickets query via command-line.

 Usage:
    tickets [-gdtkz] <from> <to> <date>

 Options:
    -h --help           显示帮助菜单
    -g                  高铁
    -d                  动车
    -t                  特快
    -k                  快速
    -z                  直达

 Example:
    tickets 南京 北京 2016-07-01
    tickets -dg 南京 北京 2016-07-01

"""

# https://kyfw.12306.cn/otn/leftTicket/init
# from docopt import docopt
#
# # print(docopt(__doc__))
#
#
# def cli():
#     tips = '''command-line interface'''
#     arguments = docopt(__doc__)
#     print(arguments)
#
# if __name__ == '__main__':
#     arguments = docopt(__doc__)
#     print(arguments)

import urllib3
import time, os
import urllib, json
from urllib import request
from prettytable import PrettyTable


# print("\n============读取文件的内容============\n")
# f_stations = open("stations", "r", encoding="utf-8")
# str_list = f_stations.read()
# list_stations = str_list.split("@")
# f_stations.close()


# f_stations_bak = open("stations.bak", "w", encoding="utf-8")
# for station in list_stations:
#     # oneStation = station.replace("\n", "").replace(" ", "").replace("\t", "").strip()
#     f_stations_bak.write(station)
#     f_stations_bak.write("\n")
# f_stations_bak.close()


list_station_titles = ["No.", "Station name"]
list_avaliableTrain_titles = ["Date", "Train", "Start time", "Arrival time",
                              "Duration",
                              "First",
                              "Second",
                              "SoftSleep",
                              "HardSleep",
                              "HardSeat",
                              "Standing",
                              "LuxurySoftSleep"]

# 根据关键字搜索车站名称
def do_searchStationWithKeyworkd(str_keyword):
    list_stations = []
    # 读取车站文件
    with open("stations.bak", "r", encoding="utf-8") as f_stations:
        for station in f_stations:
            str_line_station = station.strip()

            if str_line_station.find(str_keyword) > 0:
                list_stations.append(str_line_station)

    return list_stations

# 打印车站列表
def do_printStations(list_stations, list_titles):
    x = PrettyTable(list_titles)
    index = 1
    for station in list_stations:
        row_station = station.split("|")
        list_row_info = [index, row_station[1]]
        index += 1

        x.add_row(list_row_info)

    x.align["Station name"] = "l"
    print(x.get_string(sortby="No."))

# 根据分割分割字符串
def do_getListInfo(str_info, str_split):
    list_info = str_info.split(str_split)
    return list_info


# 打印列车信息表
def do_printAvaliableTrains(list_trains, list_titles=list_avaliableTrain_titles):

    x = PrettyTable(list_titles)

    for data in list_trains:
        str_oneTrainInfo = data

        data_row = str_oneTrainInfo.split("|")
        list_row_info = [data_row[13],
                         data_row[3],
                         data_row[8],
                         data_row[9],
                         data_row[10],
                         data_row[31],
                         data_row[30],
                         data_row[23],
                         data_row[28],
                         data_row[29],
                         data_row[26],
                         data_row[21]]
        x.add_row(list_row_info)

    print(x.get_string(sortby="Duration"))


# 获取输入地址的信息
def do_getLocationInfo(str_location_title):
    # 输入起始地址
    bool_waitInputFrom = True
    str_locationInfo = ""
    while bool_waitInputFrom:
        input_from = input(str_location_title)

        # 对起始地址进行检索
        list_stations = do_searchStationWithKeyworkd(input_from)
        do_printStations(list_stations, list_station_titles)

        bool_waitToInputIndex = True
        while bool_waitToInputIndex:
            input_from_id = input(">>>请选择地址编号或者按Q重新输入:")

            if input_from_id == 'Q' or input_from_id == 'q':
                print(">>重新选择地址")
                bool_waitToInputIndex = False
                continue

            if int(input_from_id) > len(list_stations):
                print(">>输入无效目的地序号")
                bool_waitToInputIndex = False
                continue

            print(list_stations[int(input_from_id) - 1])
            str_locationInfo = list_stations[int(input_from_id) - 1]
            bool_waitToInputIndex = False
            bool_waitInputFrom = False

    return str_locationInfo


############主循环##############
def main():
    while True:

        print("欢迎来到车票订阅系统...")

        while True:

            str_fromInfo = do_getLocationInfo(">>>请输入起始地:")
            str_toInfo = do_getLocationInfo(">>>请输入目的地:")

            print("from: ", str_fromInfo)
            print("to: ", str_toInfo)

            str_date = input(">>>请输入日期(xxxx-xx-xx):")
            str_from = do_getListInfo(str_fromInfo, "|")[2]
            str_to = do_getListInfo(str_toInfo, "|")[2]

            print(str_from, str_to, str_date)
            while True:

                print("开始请求数据...")

                # str_url = "https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-01-15&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=BOP&purpose_codes=ADULT"
                str_url = "https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=" + str_date + "&leftTicketDTO.from_station=" + str_from + "&leftTicketDTO.to_station=" + str_to + "&purpose_codes=ADULT"
                print(str_url)
                # http = urllib3.PoolManager()
                # content = http.request(
                #                 "GET",
                #                  str_url)
                # print(content.read().decode())

                content = urllib.request.urlopen(str_url, timeout=30)
                str_json = content.read().decode()
                try:
                    json_res = json.loads(str_json)

                    arr_result = json_res["data"]["result"]
                    do_printAvaliableTrains(arr_result)
                    break
                except Exception as e:
                    print(e)
                    time.sleep(0.25)


if __name__ == "__main__":
    main()
