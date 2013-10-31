# -*- coding: utf-8 -*-
import datetime
import os
import sys


def system_uptime():
    """ Return uptime of the system
        linux only

        :rtype: datetime.timedelta
    """
    try:
        import uptime
        uptime_seconds = uptime.uptime()
    except ImportError:
        if sys.platform.startswith('linux') and os.path.exists('/proc/uptime'):
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
        else:
            raise ValueError('Using uptime in non-linux environments needs uptime module to be installed')
    return datetime.timedelta(seconds=uptime_seconds)
