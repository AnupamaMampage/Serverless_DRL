import re
import sys

import random
import tensorflow as tf
import numpy as np

# from ipython_genutils.py3compat import xrange
# from pygments import formatter
#
# import definitions as df
#
# # # Creating an empty dictionary
# # myDict = {}
# #
# # # Adding list as value
# # myDict["key1"] = [1, 2]
# #
# # # # creating a list
# # lst = ['Geeks', 'For', 'Geeks']
# # print(lst[0])
# # #
# # # # Adding this list as sublist in myDict
# # myDict = {}
# # myDict["key1"] = []
# # myDict["key1"].append('Geeks')
# # myDict["key1"].append('For')
# # print(myDict["key1"][0])
#
#
# # x = 3.3
# # print(round(x))
#
#
# # myDict["key1"] = [1]
# # # myDict["key1"].append(100)
# # # print(myDict)
# # #
# # # f1 = 100
# # # i = 1
# # # print("f" + str(i))
# #
# # for i in range(1,5):
# #     print(i)
# #
# # from sortedcontainers import SortedList, SortedSet, SortedDict
# #
# # # initializing a sorted list with parameters
# # # it takes an iterable as a parameter.
# # sorted_list = SortedList([1, 2, 3, 4])
# #
# # # initializing a sorted list using default constructor
# # sorted_list = SortedList()
# #
# # # inserting values one by one using add()
# # for i in range(5, 0, -1):
# #     sorted_list.add(i)
# #
# # # prints the elements in sorted order
# # print('list after adding 5 elements: ', sorted_list)
# #
# # global events
# #
# # events= []
# # events.append(df.EVENT(50, "fn_exec"))
# # events.append(df.EVENT(25, "scale"))
# # events.append(df.EVENT(70, "fn_exec"))
# #
# # def sorter(item):
# #     time = item.time
# #     return time
# #
# # sorted_list = sorted(events, key=sorter)
# #
# # for ob in sorted_list:
# #     print(ob.event_name + " " + str(ob.time))
#
# # Nested list of student's info in a Science Olympiad
# # List elements: (Student's Name, Marks out of 100 , Age)
# # participant_list = [
# #     ('Alison', 50, 18),
# #     ('Terence', 75, 12),
# #     ('David', 75, 20),
# #     ('Jimmy', 90, 22),
# #     ('John', 45, 12)
# # ]
# #
# #
# # def sorter(item):
# #     # Since highest marks first, least error = most marks
# #     error = 100 - item[1]
# #     age = item[2]
# #     return (error, age)
# #
# #
# # sorted_list = sorted(participant_list, key=sorter)
# # print(sorted_list)
#
# # pod_info = {}
# # PODS = []
# #
# # PODS.append('a')
# # PODS.append('b')
# # PODS.append('c')
# #
# # PODS.pop(0)
# # print(PODS)
# # for x in range(3):
# #     if 'float' in pod_info:
# #         pod_info['float']['pod_cpu_util_total'] += 2
# #         pod_info['float']['pod_count'] += 1
# #
# #     else:
# #         pod_info['float'] = {}
# #         pod_info['float']['pod_cpu_util_total'] = 2
# #         pod_info['float']['pod_count'] = 1
# #
# #
# # for pod_type, pod_data in pod_info.items():
# #     print(pod_data['pod_cpu_util_total'])
# #     print(pod_data['pod_count'])
# #     print(pod_type)
#
#
# # for x in range(3):
# #     pod_info['float'] = 2
# #     pod_info['load'] = 2
# #
# #
# # print(pod_info)
#
#
# # people = {}
# #
# # people[3] = {}
# #
# # people[3]['name'] = 'Luna'
# # people[3]['age'] = '24'
# # people[3]['sex'] = 'Female'
# # people[3]['married'] = 'No'
# #
# # print(people[3])
#
# # for i in range(40):
# #     print(str(i % 20))
#
# # x = {}
# # ty = "fn"
# # x["fn"] = []
# # x[ty].append("cd")
# #
# # if ty in x:
# #     print("Y")
#
#
# import threading
# import logging
# import logging.config
#
#
# class ThreadLogFilter(logging.Filter):
#     """
#     This filter only show log entries for specified thread name
#     """
#
#     def __init__(self, thread_name, *args, **kwargs):
#         logging.Filter.__init__(self, *args, **kwargs)
#         self.thread_name = thread_name
#
#     def filter(self, record):
#         return record.threadName == self.thread_name
#
#
# def start_thread_logging():
#     """
#     Add a log handler to separate file for current thread
#     """
#     thread_name = threading.Thread.getName(threading.current_thread())
#     log_file = 'perThreadLogging-{}.log'.format(thread_name)
#     log_handler = logging.FileHandler(log_file)
#
#     log_handler.setLevel(logging.DEBUG)
#
#     formatter = logging.Formatter(
#         "%(asctime)-15s"
#         "| %(threadName)-11s"
#         "| %(levelname)-5s"
#         "| %(message)s")
#     log_handler.setFormatter(formatter)
#
#     log_filter = ThreadLogFilter(thread_name)
#     log_handler.addFilter(log_filter)
#
#     logger = logging.getLogger()
#     logger.addHandler(log_handler)
#
#     return log_handler
#
#
# def stop_thread_logging(log_handler):
#     # Remove thread log handler from root logger
#     logging.getLogger().removeHandler(log_handler)
#
#     # Close the thread log handler so that the lock on log file can be released
#     log_handler.close()
#
#
# def worker():
#     thread_log_handler = start_thread_logging()
#     logging.info('Info log entry in sub thread.')
#     logging.debug('Debug log entry in sub thread.')
#     stop_thread_logging(thread_log_handler)
#
#
# # def config_root_logger():
# #     log_file = '/tmp/perThreadLogging.log'
# #
# #     formatter = "%(asctime)-15s"
# #                 "| %(threadName)-11s"
# #                 "| %(levelname)-5s"
# #                 "| %(message)s"
# #
# #     logging.config.dictConfig({
# #         'version': 1,
# #         'formatters': {
# #             'root_formatter': {
# #                 'format': formatter
# #             }
# #         },
# #         'handlers': {
# #             'console': {
# #                 'level': 'INFO',
# #                 'class': 'logging.StreamHandler',
# #                 'formatter': 'root_formatter'
# #             },
# #             'log_file': {
# #                 'class': 'logging.FileHandler',
# #                 'level': 'DEBUG',
# #                 'filename': '/tmp/perThreadLogging.log',
# #                 'formatter': 'root_formatter',
# #             }
# #         },
# #         'loggers': {
# #             '': {
# #                 'handlers': [
# #                     'console',
# #                     'log_file',
# #                 ],
# #                 'level': 'DEBUG',
# #                 'propagate': True
# #             }
# #         }
# #     })
#
#
# if __name__ == '__main__':
#     # config_root_logger()
#
#     logging.info('Info log entry in main thread.')
#     logging.debug('Debug log entry in main thread.')
#
#     for i in xrange(3):
#         t = threading.Thread(target=worker,
#                              name='Thread-{}'.format(i),
#                              args=[])
#         t.start()


# p = {"a": 0.2, "b": 0.1, "c": 0.4, "d": [0, 2]}
# # p.pop("b")
#
# if "b" in p:
#     print(p)
#
# print(len(p))
# p = np.array(p)
#
# p /= p.sum()
# print(p)
# print(p.sum())


# print(sys.maxsize)

# print(str(random.randint(1,899999)+100000))

#
# logits_action = [1, 2,3, 4, 5, 6, 7, 8, 9, 10]
# action_size = [2, 5, 3]
# logits_c = []
# logits_m = []
# logits_r = []
# for x in range(0, action_size[0]):
#     logits_c.append(logits_action[x])
#
# for x in range(action_size[0], (action_size[0]+action_size[1])):
#     logits_m.append(logits_action[x])
#
# for x in range((action_size[0]+action_size[1]), (action_size[0]+action_size[1] + action_size[2])):
#     logits_r.append(logits_action[x])
#
# print(logits_c)
# print(logits_m)
# print(logits_r)
#
# fn_types = [0, 1, 2]
#
# if not (3 in fn_types):
#     print("yes")

# fn_array = {0: [0, 1, 2], 1: [3, 4, 5], 2: [6, 7, 8]}
#
# fn_array[3] = [7, 8]
# print(fn_array)

import gym
# import numpy as np
# from gym import spaces
# from gym.utils import seeding
#
# import constants
# from gym.spaces import Discrete, Box, MultiDiscrete
# from tensorboard.compat.tensorflow_stub.dtypes import float32
#
# prob = ([[[2.7544087e-02, 3.4344189e-03, 7.2938432e-03, 6.9254474e-04, 3.9807409e-03,
#    9.4923395e-01, 2.4455441e-03, 1.0158926e-03, 1.1184372e-03, 1.5106717e-03,
#    1.7298773e-03]]], shape=(1, 1, 11), dtype=float32)
#
# probs_c = prob.numpy()[0].flatten()
#
# print(probs_c)
# print(np.argmax(probs_c))

import numpy
# fn_list = [50, 6]
# fns = str(fn_list[0]) + "," + str(fn_list[1])
# print(fns)
# fn1, fn2 = fns.split(',')
# print(fn1)
# print(fn2)
from pandas.tests.io.excel.test_xlrd import xlrd

wbr = xlrd.open_workbook("D:\WL generation\Third_work\Simulator\WL\multi_agent\Testing\wl0.xls")
sheet = wbr.sheet_by_index(0)
for i in range(sheet.nrows - 1):
    fn_type = str(sheet.cell_value(i + 1, 0))
    # for i in range(500):
    if fn_type == 'multiple':
        fn_list = sheet.cell_value(i + 1, 1)
        fn_list = re.split("; |, |\]|\[|,", fn_list)
        print(fn_list)
        # fns = str(fn_list[0]) + "," + str(fn_list[1])
        # fn1_name, fn2_name = fns.split(',')
        print(fn_list[1])
        print(fn_list[2])
