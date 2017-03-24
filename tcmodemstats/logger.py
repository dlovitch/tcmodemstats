# -*- coding: utf-8 -*-

import logging

class Logger(object):
    def __init__(self, log_level="INFO"):
        if log_level.upper() == "DEBUG":
            log_level = logging.DEBUG
        else:
            log_level = logging.INFO
        self.configure_logger(log_level)

    def configure_logger(self, log_level):
        self.logger = logging.getLogger("tcmodemstats")

        # Ensure console_logger is only configured and setup once
        stream_handler_count = 0
        if len(self.logger.handlers) > 0:
            for handler in self.logger.handlers:
                if isinstance(handler, logging.StreamHandler):
                    stream_handler_count += 1
        if stream_handler_count >= 1:
            return

        # Console Logger
        console_logger = logging.StreamHandler()
        self.logger.setLevel(log_level)
        console_logger.setLevel(log_level)
        formatter = logging.Formatter("%(asctime)s||%(levelname)s||%(name)s|| %(message)s")
        console_logger.setFormatter(formatter)
        self.logger.addHandler(console_logger)
