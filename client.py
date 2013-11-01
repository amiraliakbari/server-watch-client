# -*- coding: utf-8 -*-
import sys
from logger import Logger


def run_modules():
    import conf.scans

    # Running Module Scans
    count = {'mods': 0, 'scans': 0, 'failed_scans': 0}
    for mod in conf.scans.enabled_modules:
        klass = mod['class']
        servers = mod.get('servers', [None])
        params = mod.get('params')
        for server in servers:
            try:
                mod_instance = klass(server=server, params=params)
                mod_instance.run()
            except Exception as e:
                print >> sys.stderr, str(e)
                count['failed_scans'] += 1
            count['scans'] += 1
        count['mods'] += 1
    print('Run Summary: {mods} modules, {scans} total scans, {failed_scans} failed.'.format(**count))

    # closing log files
    Logger.get().close_all()


if __name__ == '__main__':
    run_modules()
