#! /usr/bin/env python
# -*- coding: utf-8 -*-

import click
import json

import tcmodemstats

@click.command()
@click.option("-d", "--debug", count=True)
@click.option("-h", "--host", required=True)
@click.option("-u", "--username", required=True)
@click.option("-p", "--password", required=True)
def main(debug, host, username, password):
    if debug:
        log_level = "DEBUG"
    else:
        log_level = "INFO"
    modemstats = tcmodemstats.ModemStats(host, username, password, log_level)
    modemstats.get_stats()
    print(json.dumps(modemstats.stats, sort_keys=True, indent=4))
    #s = tcmodemstats.Scraper(host, username, password)
    #print(json.dumps(s.get_vendor_network(), sort_keys=True, indent=4))

if __name__ == "__main__":
    main()
