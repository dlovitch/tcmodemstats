# -*- coding: utf-8 -*-

import pytest

import os
import tcmodemstats

class TestConfig(object):

    def test_good_login(self):
        self.config = tcmodemstats.Config()

        scraper = tcmodemstats.Scraper(
            host=self.config.tcmodem_host,
            username=self.config.tcmodem_username,
            password=self.config.tcmodem_password
            )
        login_result = scraper.login()
        assert login_result == 200

    def test_bad_login(self):
        self.config = tcmodemstats.Config()

        with pytest.raises(ValueError) as excinfo:
            scraper = tcmodemstats.Scraper(
                host=self.config.tcmodem_host,
                username="badusername",
                password="badpassword"
                )
        assert str(excinfo.value) == "Username or password not correct"