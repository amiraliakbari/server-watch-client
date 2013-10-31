# -*- coding: utf-8 -*-
import os


class Logger(object):
    instance = None

    def __init__(self):
        self.loggers = {}

    def get_logger(self, name):
        """
            :rtype: ServerLogger
        """
        if name not in self.loggers:
            self.loggers[name] = ServerLogger(name)
        return self.loggers[name]

    def close_all(self):
        for logger in self.loggers.values():
            logger.close()

    @classmethod
    def get(cls):
        """
            :rtype: Logger
        """
        if cls.instance is None:
            cls.instance = Logger()
        return cls.instance


class ServerLogger(object):
    def __init__(self, name):
        self.server_name = name
        self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'logs', self.server_name)
        if not os.path.isdir(self.path):
            os.makedirs(self.path)
        self.log_file = open(os.path.join(self.path, 'latest'), 'a', 1)

    def log(self, message):
        self.log_file.write(message)
        self.log_file.write('\n')

    def close(self):
        self.log_file.close()
