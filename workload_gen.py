import math
import random
import csv

import xlrd
import xlwt
from xlwt import Workbook

fn_array = {0: [0, 1, 2], 1: [3, 4, 5], 2: [6, 7, 8],  3: [9, 10, 11], 4: [12, 13, 14]}
arrivalTime = 1
interArrivalTime = 0
noRateChanges = 4
wl_duration = 50
episodes = 20
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
for z in range(3, 5):
    for y in range(episodes):
        wb = Workbook()
        req_wl = wb.add_sheet('Requests')
        req_wl.write(0, 0, 'Fn_type')
        req_wl.write(0, 1, 'Time')
        req_wl.write(0, 2, 'Rate')
        req_wl.write(0, 3, 'Req_ID')
        c = 1
        req_id = 1
        wl_no += 1
        for x in range(3):
            fn = fn_array[z][x]
            # if x != 0:
            #     arrivalTime = random.randint(1, 5)
            # else:
            arrivalTime = 1

            # for c in range(noRateChanges):
            step = 1
            poisson_lambda = random.randint(10, 60)
            # while arrivalTime < wl_duration:
            while step <= no_steps:
                while arrivalTime < step_duration*step + wl_stop_time*(step - 1):
                    req_wl.write(c, 0, fn)
                    req_wl.write(c, 1, float(arrivalTime))
                    req_wl.write(c, 2, int(poisson_lambda))
                    req_wl.write(c, 3, int(req_id))
                    wb.save("D:/WL generation/Third_work/Simulator/WL/multi_agent/New folder/" + str(z) + "/wl"+str(y) + ".xls")
                    req_id += 1
                    c += 1
                    probability = random.random()
                    interArrivalTime = round((-math.log(1.0 - probability) / poisson_lambda), 2)
                    arrivalTime = round(arrivalTime + interArrivalTime, 2)
                arrivalTime += wl_stop_time
                step += 1



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
