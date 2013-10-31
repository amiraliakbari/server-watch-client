# -*- coding: utf-8 -*-
import datetime
import pytz
from logger import Logger


class BaseModule(object):
    LOG_FORMAT = '[{server}] [{mod}] [{dt}] {msg}'

    def __init__(self, server=None):
        self.server = server if server is not None else 'localhost'
        self.logger = Logger.get().get_logger(self.server)
        self.mod_name = self.__class__.__name__

        if self.server != 'localhost' and not self.can_scan_remotes():
            raise ValueError('{0} module can not perform remote scan!'.format(self.mod_name))

    def log(self, message, *args, **kwargs):
        if not args and not kwargs and not isinstance(message, basestring):
            message = str(message)
        now = datetime.datetime.now(pytz.utc)
        local_now = now.astimezone(pytz.timezone('Asia/Tehran'))
        m = self.LOG_FORMAT.format(mod=self.mod_name,
                                   dt=local_now.strftime('%d/%b/%Y:%H:%M:%S %z'),
                                   server=self.server,
                                   msg=message.format(*args, **kwargs))
        self.logger.log(m)

    def can_scan_remotes(cls):
        return False

    def finish(self):
        self.logger.close()

    def run(self):
        raise NotImplementedError()
