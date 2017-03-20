# -*- coding: utf-8 -*-

import pytest

import tcmodemstats

class TestConfig(object):

    def test_default_config_filename(self):
        config = tcmodemstats.Config()
        assert config.config_filename == "config.yaml"

    def test_custom_config_filename(self):
        config = tcmodemstats.Config("custom")
        print("in testing: {}".format(config.config_filename))
        assert config.config_filename == "custom"