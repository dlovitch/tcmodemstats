# -*- coding: utf-8 -*-

import logging
import re

from . import downstream
from . import logger
from . import scraper
from . import upstream

class ModemStats(object):
    def __init__(self, host, username, password, log_level="INFO"):
        self.logger_base = logger.Logger(log_level)
        self.logger = logging.getLogger("tcmodemstats")
        self.scraper = scraper.Scraper(host, username, password)

    def get_stats(self):
        non_decimal = re.compile(r'[^\d.]+')

        self.stats = self.scraper.get_vendor_network()
        self.downstream = []
        self.upstream = []
        for s in self.stats["Downstream"]:
            new_stream = downstream.Downstream()
            if "Index"       in s: new_stream.index = s["Index"]
            if "Frequency"   in s: new_stream.frequency = non_decimal.sub('', s["Frequency"])
            if "Lock Status" in s: new_stream.lock_status = s["Lock Status"]
            if "Modulation"  in s: new_stream.modulation = non_decimal.sub('', s["Modulation"])
            if "Power"       in s: new_stream.power = non_decimal.sub('', s["Power"])
            if "SNR"         in s: new_stream.snr = non_decimal.sub('', s["SNR"])
            self.downstream.append(new_stream)
        for s in self.stats["Upstream"]:
            new_stream = upstream.Upstream()
            if "Index"       in s: new_stream.index = s["Index"]
            if "Channel ID"  in s: new_stream.channel_id = s["Channel ID"]
            if "Frequency"   in s: new_stream.frequency = non_decimal.sub('', s["Frequency"])
            if "Lock Status" in s: new_stream.lock_status = s["Lock Status"]
            if "Modulation"  in s: new_stream.modulation = s["Modulation"]
            if "Power Level" in s: new_stream.power_level = non_decimal.sub('', s["Power Level"])
            if "Symbol Rate" in s: new_stream.symbol_rate = non_decimal.sub('', s["Symbol Rate"])
            self.upstream.append(new_stream)
