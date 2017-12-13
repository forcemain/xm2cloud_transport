#! -*- coding: utf-8 -*-


class Task(object):
    @staticmethod
    def create_from_conf(sobj, conf_list, method):
        task_list = []
        if not (conf_list and getattr(sobj, 'create_engine', None)):
            return task_list

        for conf_item in conf_list:
            engine, conf = conf_item['engine'], conf_item['conf']
            engine_ins = sobj.create_engine(engine, conf)
            engine_fun = getattr(engine_ins, method)
            task_list.append(engine_fun)

        return task_list




