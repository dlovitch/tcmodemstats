# -*- coding: utf-8 -*-

import pytest

import os
import tcmodemstats

class TestConfig(object):

    def test_default_config_filename(self):
        config = tcmodemstats.Config()
        assert config.config_filename == "config.yaml"

    def test_custom_config_filename(self):
        config = tcmodemstats.Config("custom")
        assert config.config_filename == "custom"

    def test_key(self):
        config = tcmodemstats.Config()
        os.environ["pytest_tcmodemstats_testkey"] = "testvalue"
        assert config.pytest_tcmodemstats_testkey == os.getenv("pytest_tcmodemstats_testkey")

    def test_non_existent_key(self):
        config = tcmodemstats.Config()
        assert config.key == None

