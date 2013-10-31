# -*- coding: utf-8 -*-
from modules.base_module import BaseModule
from monitoring.system import system_load, system_uptime


class UptimeMonitor(BaseModule):
    def run(self):
        self.log(system_uptime())


class LoadMonitor(BaseModule):
    def run(self):
        self.log('{avg1} {avg5} {avg15} {runnable}/{existing}', **system_load())
