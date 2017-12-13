#! -*- coding: utf-8 -*-


import time
import logging
import threading
import multiprocessing

from agent.task import Task
from agent.input.base import input_ins
from multiprocessing.queues import Queue
from agent.output.base import output_ins
from agent.filter.base import filter_ins
from agent.settings import AGENT_INPUT, AGENT_OUTPUT, AGENT_FILTER


class Agent(object):
    def __init__(self, pull_interval=5):

        self.input = None
        self.filter = None
        self.output = None

        # for input write and filter read
        self.iqueue = Queue()
        # for filter write and output read
        self.oqueue = Queue()

        self.pull_interval = pull_interval

        self.__init_all()

    def __init_all(self):
        self.__set_filter()
        self.__set_output()
        self.__set_input()

    def __set_input(self):
        input_ins.set_res_queue(self.iqueue)

        def target():
            while True:
                # pull_data must be realized in input handler
                task_list = Task.create_from_conf(input_ins, AGENT_INPUT, 'pull_data')
                if not task_list:
                    time.sleep(self.pull_interval)
                list_task = []
                for task in task_list:
                    t = threading.Thread(target=task)
                    t.setDaemon(True)
                    t.start()
                    list_task.append(t)
                for task in list_task:
                    task.join()
                time.sleep(self.pull_interval)

        p = multiprocessing.Process(target=target)
        p.daemon = True
        p.start()

        logging.debug('{0} start input handlers ...'.format(self.__class__.__name__))

    def __set_output(self):
        def target():
            while True:
                data = self.oqueue.get()
                # push_data must be realized in output handler
                task_list = Task.create_from_conf(output_ins, AGENT_OUTPUT, 'push_data')
                if not task_list:
                    continue
                list_task = []
                for task in task_list:
                    t = threading.Thread(target=task, args=(data,))
                    t.setDaemon(True)
                    t.start()
                for task in list_task:
                    task.join()

        p = multiprocessing.Process(target=target)
        p.daemon = True
        p.start()

        logging.debug('{0} start out handlers ...'.format(self.__class__.__name__))

    def __set_filter(self):
        def target():
            while True:
                data = self.iqueue.get()
                task_list = Task.create_from_conf(filter_ins, AGENT_FILTER, 'filter_data')
                filtered_data = data
                for task in task_list:
                    filtered_data = task(filtered_data)

                self.oqueue.put(filtered_data)

        p = multiprocessing.Process(target=target)
        p.daemon = True
        p.start()

        logging.debug('{0} start filter handlers ...'.format(self.__class__.__name__))

    def loop(self):
        logging.debug('{0} start successfully!'.format(self.__class__.__name__))
        # as main block process
        while True:
            time.sleep(1)

