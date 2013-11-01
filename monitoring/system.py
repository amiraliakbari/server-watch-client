# -*- coding: utf-8 -*-
import datetime
import os
import sys
import psutil


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


def system_load():
    if sys.platform.startswith('linux') and os.path.exists('/proc/uptime'):
        with open('/proc/loadavg', 'r') as f:
            p = f.readline().split()
            r, e = p[3].split('/')
            return {'avg1': p[0], 'avg5': p[1], 'avg15': p[2], 'runnable': r, 'existing': e}
    raise ValueError('Load info is only available in linux')


def system_resources_summary():
    nt = psutil.net_io_counters()
    return {
        'ram': psutil.virtual_memory().percent,
        'swap': psutil.swap_memory().percent,
        'disk': psutil.disk_usage('/').percent,
        'net-sent': nt.bytes_sent,
        'net-recv': nt.bytes_recv,
    }
