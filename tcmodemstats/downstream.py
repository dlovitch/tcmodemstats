# -*- coding: utf-8 -*-

class Downstream(object):
    def __init__(self, 
            index=None,
            frequency=None,
            lock_status=None,
            modulation=None,
            power=None,
            snr=None):
        self.index = index
        self.frequency = frequency
        self.lock_status = lock_status
        self.modulation = modulation
        self.power = power
        self.snr = snr

    def __str__(self):
        return "Index: {}, Frequency: {} MHz, Lock Status: {}, Modulation: {} QAM, Power: {} dBmV, SNR: {} dB".format(
            self.index, self.frequency, self.lock_status, self.modulation, self.power, self.snr)