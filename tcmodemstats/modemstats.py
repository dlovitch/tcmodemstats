# -*- coding: utf-8 -*-

import re

import scraper
import downstream
import upstream

class ModemStats(object):
    def __init__(self, host, username, password, scraper_verbosity=0):

        non_decimal = re.compile(r'[^\d.]+')

        self.scraper = scraper.Scraper(scraper_verbosity, host, username, password)
        stats = self.scraper.get_vendor_network()
        self.downstream = []
        self.upstream = []
        for s in stats["Downstream"]:
            new_stream = downstream.Downstream()
            if "Index"       in s: new_stream.index = s["Index"]
            if "Frequency"   in s: new_stream.frequency = non_decimal.sub('', s["Frequency"])
            if "Lock Status" in s: new_stream.lock_status = s["Lock Status"]
            if "Modulation"  in s: new_stream.modulation = non_decimal.sub('', s["Modulation"])
            if "Power"       in s: new_stream.power = non_decimal.sub('', s["Power"])
            if "SNR"         in s: new_stream.snr = non_decimal.sub('', s["SNR"])
            self.downstream.append(new_stream)
        for s in stats["Upstream"]:
            new_stream = upstream.Upstream()
            if "Index"       in s: new_stream.index = s["Index"]
            if "Channel ID"  in s: new_stream.channel_id = s["Channel ID"]
            if "Frequency"   in s: new_stream.frequency = non_decimal.sub('', s["Frequency"])
            if "Lock Status" in s: new_stream.lock_status = s["Lock Status"]
            if "Modulation"  in s: new_stream.modulation = s["Modulation"]
            if "Power Level" in s: new_stream.power_level = non_decimal.sub('', s["Power Level"])
            if "Symbol Rate" in s: new_stream.symbol_rate = non_decimal.sub('', s["Symbol Rate"])
            self.upstream.append(new_stream)

