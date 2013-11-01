# -*- coding: utf-8 -*-
from modules.base_module import BaseModule
from monitoring.services import service_is_running
from monitoring.system import system_load, system_uptime, system_resources_summary


class UptimeMonitor(BaseModule):
    def run(self):
        self.log(system_uptime())


class LoadMonitor(BaseModule):
    def run(self):
        self.log('{avg1} {avg5} {avg15} {runnable}/{existing}', **system_load())


class ServiceMonitor(BaseModule):
    def run(self):
        ups = []
        downs = []
        for srv in self.params or []:
            if service_is_running(srv):
                ups.append(srv)
            else:
                downs.append(srv)
        self.log('up: {0}, down: {1}', ups, downs)


class ResourceMonitor(BaseModule):
    def run(self):
        self.log('RAM: {ram}, SWAP: {swap}, DISK: {disk}, NET: -{net-recv}/+{net-sent}',
                 **system_resources_summary())
