#! /usr/bin/env python
# -*- coding: utf-8 -*-

import tcmodemstats

def main():
    forwarder = tcmodemstats.ModemStatsForwarder()
    forwarder.timer()

if __name__ == '__main__':
    main()