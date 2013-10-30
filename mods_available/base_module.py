# -*- coding: utf-8 -*-
import datetime
from logger import Logger


class BaseModule(object):
    LOG_FORMAT = '[{mod}] {dt} {msg}'

    def __init__(self, server=None):
        self.server = server if server is not None else 'local'
        self.logger = Logger.get().get_logger(self.server)
        self.mod_name = self.__class__.__name__

    def log(self, message, *args, **kwargs):
        m = self.LOG_FORMAT.format(mod=self.mod_name,
                                   dt=str(datetime.datetime.now()),
                                   msg=message.format(*args, **kwargs))
        self.logger.log(m)

    def run(self):
        raise NotImplementedError()
