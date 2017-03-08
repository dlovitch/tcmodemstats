# -*- coding: utf-8 -*-

class Upstream(object):
    def __init__(self,
            index=None,
            channel_id=None,
            frequency=None,
            lock_status=None,
            modulation=None,
            power_level=None,
            symbol_rate=None):
        self.index = index
        self.channel_id = channel_id
        self.frequency = frequency
        self.lock_status = lock_status
        self.modulation = modulation
        self.power_level = power_level
        self.symbol_rate = symbol_rate

    def __str__(self):
        return "Index: {}, Channel ID: {}, Frequency: {} MHz, Lock Status: {}, Modulation: {}, Power Level: {} dBmV, Symbol Rate: {} Ksym/sec".format(
            self.index, self.channel_id, self.frequency, self.lock_status, self.modulation, self.power_level, self.symbol_rate)