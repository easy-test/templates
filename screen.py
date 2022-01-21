#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-01-06 19:07:31
# @Author  : zzz {easy-quest@vk.com}
# @Link    : https://github.com/easy-quest/
# @Version : 1.0.0
from ft import Ft
from playwright.sync_api import sync_playwright

### current bpython session - make changes and save to reevaluate session.
### lines beginning with ### will be ignored.
### To return to bpython without reevaluating make no changes to this file
### or save an empty file.

def Screen():
    # browser = chromium.launch(['--proxy-server=socks5://127.0.0.1:9050'])
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("http://whatsmyuseragent.org/")
    # OUT: <Response url='http://whatsmyuseragent.org/' request=<Request url='http://whatsmyuseragent.org/' method='GET'>>
    page.screenshot(path="./img/"+(Ft()+".png"))
    browser.close()
    playwright.stop()
###