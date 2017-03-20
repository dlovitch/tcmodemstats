#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time

import tcmodemstats

def main():
    forwarder = tcmodemstats.ModemStatsForwarder()
    while True:
        forwarder.main()
        time.sleep(10)

if __name__ == '__main__':
    main()