# -*- coding: utf-8 -*-
from mods_available.base_module import BaseModule
from monitoring.system import system_uptime


class UptimeMonitor(BaseModule):
    def run(self):
        self.log(system_uptime())
        self.finish()
