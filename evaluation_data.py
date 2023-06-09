import math
import random
import csv

import xlrd
import xlwt
from xlwt import Workbook

fn_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
arrivalTime = 1
interArrivalTime = 0
noRateChanges = 4
wl_duration = 50
episodes = 60
#duration that one rate for a fn prevails
rate_interval = 20
poisson_lambda = 0
probability = 0
no_steps = 6
step_duration = 6
wl_stop_time = 3

wb = Workbook()
req_wl = wb.add_sheet('Requests')
req_wl.write(0, 0, 'Fn_type')
req_wl.write(0, 1, 'Time')
req_wl.write(0, 2, 'Rate')
req_wl.write(0, 3, 'Req_ID')

# filename = ("D:\WL generation\Third_work\WL.csv")
# f = open(filename, "wrread from+")
# writer = csv.writer(f)
c = 1
req_id = 1

#when having multiplw rate changes for a fn in one file
# for z in range(3):
#
#     #ini_arrivalTime = 1
#     # noArrivals = 40
#     # poisson_lambda = 8
#     # print(fn_array[x])
#     for x in range(noRateChanges):
#         ini_arrivalTime = arrivalTime
#         poisson_lambda = random.randint(1, 5)
#         while arrivalTime < ini_arrivalTime + rate_interval:
#             probability = random.random()
#
#             req_wl.write(c, 0, fn_array[z])
#             req_wl.write(c, 1, float(arrivalTime))
#             req_wl.write(c, 2, int(poisson_lambda))
#             req_wl.write(c, 3, int(req_id))
#             wb.save("D:\WL generation\Third_work\WL1.xls")
#             req_id += 1
#             c += 1
#             interArrivalTime = round((-math.log(1.0 - probability) / poisson_lambda), 2)
#             arrivalTime = round(arrivalTime + interArrivalTime, 2)
#
#         arrivalTime += 20
#     arrivalTime = random.randint(1, 5)



#creating separate episodes
wl_no = 0
wbr = xlrd.open_workbook("D:/OneDrive - The University of Melbourne/UniMelb/Studying/Third work/Data/Single_fn_arrival_40-60.xls")
sheet = wbr.sheet_by_index(0)
row = sheet.nrows
for y in range(15, episodes):
    wb = Workbook()
    req_wl = wb.add_sheet('Requests')
    req_wl.write(0, 0, 'Fn_type')
    req_wl.write(0, 1, 'Fns')
    req_wl.write(0, 2, 'Time')
    req_wl.write(0, 3, 'Rate')
    req_wl.write(0, 4, 'Req_ID')
    c = 1
    req_id = 1
    wl_no += 1
    fn_list = []
    fn = ""
    fn_type = ""
    while len(fn_list) < 4:
        value = random.choice(fn_array)
        if value not in fn_list:
            fn_list.append(value)
    for x in range(5):
        if x < 3:
            fn = fn_list[x]
            fn_type = "single"
        elif x == 3:
            fn = [fn_list[0], fn_list[1]]
            fn_type = "multiple"
        elif x == 4:
            fn = [fn_list[0], fn_list[2]]
            fn_type = "multiple"
        # if x != 0:
        #     arrivalTime = random.randint(1, 5)
        # else:
        arrivalTime = 1

        # for c in range(noRateChanges):
        step = 1

        # while arrivalTime < wl_duration:
        column = 1
        while step <= no_steps:
            while row < sheet.nrows:
                poisson_lambda = int(sheet.cell_value(row, column))
            else:
                poisson_lambda = random.randint(40, 60)
            column += 1
            while arrivalTime < step_duration*step + wl_stop_time*(step - 1):
                req_wl.write(c, 0, str(fn_type))
                req_wl.write(c, 1, str(fn))
                req_wl.write(c, 2, float(arrivalTime))
                req_wl.write(c, 3, int(poisson_lambda))
                req_wl.write(c, 4, int(req_id))
                wb.save("D:/WL generation/Third_work/Simulator/WL/multi_agent/Testing/New folder/wl" + str(y) + ".xls")
                req_id += 1
                c += 1
                probability = random.random()
                interArrivalTime = round((-math.log(1.0 - probability) / poisson_lambda), 2)
                arrivalTime = round(arrivalTime + interArrivalTime, 2)
            arrivalTime += wl_stop_time
            step += 1
        row += 1



    #ini_arrivalTime = 1
    # noArrivals = 40
    # poisson_lambda = 8
    # print(fn_array[x])
    # for x in range(noRateChanges):
    #     ini_arrivalTime = arrivalTime
    #     poisson_lambda = random.randint(1, 5)
    #     while arrivalTime < ini_arrivalTime + rate_interval:
    #         probability = random.random()
    #
    #         req_wl.write(c, 0, fn_array[z])
    #         req_wl.write(c, 1, float(arrivalTime))
    #         req_wl.write(c, 2, int(poisson_lambda))
    #         req_wl.write(c, 3, int(req_id))
    #         wb.save("D:\WL generation\Third_work\WL1.xls")
    #         req_id += 1
    #         c += 1
    #         interArrivalTime = round((-math.log(1.0 - probability) / poisson_lambda), 2)
    #         arrivalTime = round(arrivalTime + interArrivalTime, 2)
    #
    #     arrivalTime += 20
    # arrivalTime = random.randint(1, 5)

    # for x in range(noRateChanges):
    #     # poisson_lambda = random.randint(5, 10)
    #     poisson_lambda = random.randint(1, 5)
    #     for y in range(noArrivals):
    #         probability = random.random()
    #         interArrivalTime = round((-math.log(1.0 - probability) / poisson_lambda), 2)
    #         arrivalTime = round(arrivalTime + interArrivalTime, 2)
    #
    #         req_wl.write(c, 0, fn_array[z])
    #         req_wl.write(c, 1, float(arrivalTime))
    #         req_wl.write(c, 2, int(poisson_lambda))
    #         req_wl.write(c, 3, int(req_id))
    #         wb.save("D:\WL generation\Third_work\WL.xls")
    #         req_id += 1
    #         c += 1
    #
    #     arrivalTime += 20

# f.close()

#
# wb = xlrd.open_workbook("D:\WL generation\Third_work\WL.xls")
# sheet = wb.sheet_by_index(0)
# print(sheet.nrows)
# for i in range(sheet.nrows):
#     print(i)
#     fn_name = sheet.cell_value(i + 1, 0)
#     arr_time = sheet.cell_value(i + 1, 1)
#     print(fn_name)
#     print(arr_time)
