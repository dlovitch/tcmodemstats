# -*- coding: utf-8 -*-

import bs4
import logging
import requests

class Scraper(object):
    def __init__(self, host, username, password):
        self.logger = logging.getLogger("tcmodemstats")
        #print("got here")
        #exit(1)
        self.host = host
        self.username = username
        self.password = password
        self.login()

    def process_columnar_table(self, table):
        #print(table.text)
        data = []
        for tr in table.findAll("tr")[1:]:
            header = tr.findNext("th")
            for td in range(0,len(tr.findAll("td"))):
                if len(data) < td+1:
                    data.append({header.text: tr.findAll("td")[td].text})
                else:
                    data[td][header.text] = tr.findAll("td")[td].text
        return data

    def process_table(self, table, unique_key=True):
        if unique_key:
            data = {}
            range_start = 1
        else:
            data = []
            range_start = 0
        headers = [td.text for td in table[0].findAll("td")]
        self.logger.debug("scraper/process_table/headers: {}".format(headers))
        for tr in table[1:]:
            if tr.findAll("td"):
                row = [td.text for td in tr.findAll("td")]
                self.logger.debug("scraper/process_table/row: {}".format(row))
                processed_row = {}
                for i in range(range_start, len(headers)):
                    processed_row[headers[i]] = row[i]
                self.logger.debug("scraper/process_table/processed_row: {}".format(processed_row))
                if unique_key:
                    data[row[0]] = processed_row
                else:
                    data.append(processed_row)
        return data

    def process_kv_table(self, table):
        data = {}
        #print(table)
        for tr in table:
            if tr.findAll("td"):
                data[tr.findNext("td").text.strip()[:-1]] = tr.findNext("td").findNext("td").text.strip()
        return data

    def login(self):
        login = {"loginUsername": self.username, "loginPassword": self.password}
        r = requests.post("http://{}/goform/home_loggedout".format(self.host), data=login)
        if "<!-- $Id: at_a_glance.asp" not in r.text: # login was not successful
            if "<!-- $Id: home_loggedout.php" in r.text:
                raise ValueError("Username or password not correct")
            else:
                raise ValueError("Unknown error while attempting to login")
        return r.status_code


    def get_vendor_network(self):
        status = {}
        r = requests.get("http://{}/vendor_network.asp".format(self.host))
        if r.status_code == 200:
            souped = bs4.BeautifulSoup(r.content, "lxml")
            for table in souped.findAll("table"):
                if table.findNext("thead") and table.findNext("thead").findNext("tr").findNext("th").text.strip() == "Downstream":
                    status["Downstream"] = self.process_columnar_table(table)
                if table.findNext("thead") and table.findNext("thead").findNext("tr").findNext("th").text.strip() == "Upstream":
                    status["Upstream"] = self.process_columnar_table(table)
        return status
