# -*- coding: utf-8 -*-
import sys
from mods_available.uptime_monitor import UptimeMonitor


def run_modules():
    # TODO: to be extracted to config files
    modules = [
        {'class': UptimeMonitor, 'servers': ['localhost']}
    ]

    # Running Module Scans
    count = {'mods': 0, 'scans': 0, 'failed_scans': 0}
    for mod in modules:
        klass = mod['class']
        servers = mod.get('servers', [None])
        for server in servers:
            try:
                mod_instance = klass(server=server)
                mod_instance.run()
            except Exception as e:
                print >> sys.stderr, str(e)
                count['failed_scans'] += 1
            count['scans'] += 1
        count['mods'] += 1
    print('Run Summary: {mods} modules, {scans} total scans, {failed_scans} failed.'.format(**count))


if __name__ == '__main__':
    run_modules()
