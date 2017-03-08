#! /usr/bin/env python
# -*- coding: utf-8 -*-

#stats_destination = "influxdb"
stats_destination = "datadog"

if stats_destination == "influxdb":
    from influxdb import InfluxDBClient
if stats_destination == "datadog":
    import datadog

import datetime
import time

import config
import logging
import modemstats

#log_level = logging.INFO
log_level  = logging.DEBUG

class ModemStatsForwarder(object):
    def __init__(self):
        self.config = config.Config()
        self.configure_logger()

    def configure_logger(self):
        self.logger = logging.getLogger(__name__)
        console_logger = logging.StreamHandler()
        self.logger.setLevel(log_level)
        console_logger.setLevel(log_level)
        formatter = logging.Formatter("%(asctime)s//%(levelname)s//%(name)s//%(message)s")
        console_logger.setFormatter(formatter)
        self.logger.addHandler(console_logger)

    def log_and_exit(self, message):
        self.logger.critical(message)
        exit(message)

    def get_modem_stats(self):
        self.modem_stats = modemstats.ModemStats(
            host=self.config.tcmodem_host,
            username=self.config.tcmodem_username,
            password=self.config.tcmodem_password
            )


    def send_to_influxdb(self):
        # WIP
        return

        influxdb_port = 8086

        now = datetime.datetime.today()
        series = []
        for stream in self.modem_status.downstream:
            logger.info("ds: {}".format(stream))
            point_values = {
                "time": int(now.strftime('%s')),
                "measurement": "power",
                "fields":  {
                    "value": stream.power,
                },
                "tags": {
                    "host": self.config.tcmodem_name,
                    "stream": "downstream",
                    "index": stream.index,
                },
            }
            series.append(point_values)

        self.logger.debug("Attempting to connect to InfluxDB server {} on port {}".format(self.config.influxdb_host, influxdb_port))
        if self.config.influxdb_connection_timeout:
            influxdb_connection_timeout = influxdb_connection_timeout
        else:
            influxdb_connection_timeout = 5
        client = InfluxDBClient(host=self.config.influxdb_host, port=influxdb_port, timeout=influxdb_connection_timeout)

        result = client.query("SHOW DATABASES")
        self.logger.debug("SHOW DATABASES: {}".format(result))
        if not any(("name" in d) and (d["name"] == self.config.influxdb_dbname) for d in result["databases"]):
            try:
                self.logger.info("Creating database {}...".format(self.config.influxdb_dbname))
                client.create_database(self.config.influxdb_dbname)
            except InfluxDBClientError:
                self.logger.critical("Failed to create InfluxDB database {}...".format(self.config.influxdb_dbname))
                exit("Failed to create InfluxDB database {}".format(self.config.influxdb_dbname))
        client.switch_database(self.config.influxdb_dbname)
        client.write_points(series)

    def send_to_datadog(self):
        options = {
            'api_key': self.config.datadog_api_key,
            'app_key': self.config.datadog_app_key
        }
        datadog.initialize(**options)

        now = time.time()
        metrics = []
        for stream in self.modem_stats.downstream:
            metrics.append({"metric": "cablemodem.downstream.frequency", "points": (now, stream.frequency), "host": self.config.tcmodem_name, "tags": ["index:{}".format(stream.index)]})
            metrics.append({"metric": "cablemodem.downstream.power", "points": (now, stream.power), "host": self.config.tcmodem_name, "tags": ["index:{}".format(stream.index)]})
            metrics.append({"metric": "cablemodem.downstream.snr", "points": (now, stream.snr), "host": self.config.tcmodem_name, "tags": ["index:{}".format(stream.index)]})
        for stream in self.modem_stats.upstream:
            metrics.append({"metric": "cablemodem.upstream.frequency", "points": (now, stream.frequency), "host": self.config.tcmodem_name, "tags": ["index:{}".format(stream.index)]})
            metrics.append({"metric": "cablemodem.upstream.power_level", "points": (now, stream.power_level), "host": self.config.tcmodem_name, "tags": ["index:{}".format(stream.index)]})
            metrics.append({"metric": "cablemodem.upstream.symbol_rate", "points": (now, stream.symbol_rate), "host": self.config.tcmodem_name, "tags": ["index:{}".format(stream.index)]})
        self.logger.debug(metrics)
        self.logger.debug("Sending metrics to Datadog.")
        datadog.api.Metric.send(metrics)
        self.logger.info("Metrics sent to Datadog.")

    def main(self):

        if (self.config.tcmodem_host is None
            or self.config.tcmodem_username is None
            or self.config.tcmodem_password is None
            or self.config.tcmodem_name is None):
            self.log_and_exit("Missing a required tcmodem configuration setting")

        if (self.config.stats_destination is None):
            self.log_and_exit("Missing stats_destination configuration setting.")
            
        if (self.config.influxdb_host is None
            or self.config.influxdb_dbname is None):
            self.log_and_exit("Missing a required influxdb configuration setting.")

        self.get_modem_stats()

        if stats_destination == "influxdb":
            self.send_to_influxdb()
        elif stats_destination == "datadog":
            self.send_to_datadog()
        else:
            self.log_and_exit("Unknown stats destination.")



if __name__ == "__main__":
    forwarder = ModemStatsForwarder()
    while True:
        forwarder.main()
        time.sleep(10)