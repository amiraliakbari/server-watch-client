# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE

SERVICES = {
    'apache2': {
        'running-msg': 'Apache2 is running',
    },
    'ssh': {
        'running-msg': 'ssh start/running',
    },
    'mysql': {
        'running-msg': 'mysql start/running',
    },
    'postgresql-9.1': {
        'running-msg': '9.1/main',
        'service-id': 'postgresql',
    },
    'neo4j': {
        'running-msg': 'neo4j is running',
        'service-id': 'neo4j-service',
    },
    'prosody': {
        'running-msg': 'Prosody is running with PID',
        'status-command': ['prosodyctl', 'status'],
    },
}


def service_is_running(service):
    if not service in SERVICES:
        raise ValueError('Unknown service: {0}.'.format(service))
    srv = SERVICES[service]
    if 'status-command' in srv:
        cmd = srv['status-command']
    else:
        cmd = ['service', srv.get('service-id', service), 'status']
    status_msg = Popen(cmd, stdout=PIPE).stdout.read()
    return srv['running-msg'] in status_msg

