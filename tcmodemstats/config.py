# -*- coding: utf-8 -*-

import os
import os.path
import yaml

class Config(object):
    config_filename = "config.yaml"

    def __init__(self, config_filename=None):
        self.config_filename = config_filename or self.config_filename
        if os.path.isfile(self.config_filename):
            with open(self.config_filename, "r") as f:
                self.config = yaml.load(f)
        else:
            self.config = []

    def __getattr__(self, attrname):
        # prioritize environment variables for configuration over the
        # configuration file
        if attrname in os.environ:
            return os.environ[attrname]
        else:
            if self.config_filename and attrname in self.config:
                return self.config[attrname]
            else:
                return None